import ast  # Import ast (Abstract Syntax Tree) to parse Python code / 导入 ast (抽象语法树) 以解析 Python 代码
import json  # Import json for JSON parsing / 导入 json 用于 JSON 解析
import os  # Import os for file system operations / 导入 os 用于文件系统操作
from typing import Any, Dict, List, Optional, Tuple, Callable  # Import type hints / 导入类型提示

from dotenv import load_dotenv  # Import load_dotenv / 导入 load_dotenv
from ollama import chat  # Import chat / 导入 chat

load_dotenv()

NUM_RUNS_TIMES = 3


# ==========================
# Tool implementation (the "executor")
# 工具实现（"执行器"）
# ==========================
def _annotation_to_str(annotation: Optional[ast.AST]) -> str:
    """Helper to convert an AST type annotation node back to a string.
    将 AST 类型注释节点转换回字符串的辅助函数。
    """
    if annotation is None:
        return "None"
    try:
        # ast.unparse converts the AST node back to source code string (Python 3.9+)
        # ast.unparse 将 AST 节点转换回源代码字符串 (Python 3.9+)
        return ast.unparse(annotation)  # type: ignore[attr-defined]
    except Exception:
        # Fallback best-effort if unparse fails
        # 如果 unparse 失败，尽力回退
        if isinstance(annotation, ast.Name):
            return annotation.id
        return type(annotation).__name__


def _list_function_return_types(file_path: str) -> List[Tuple[str, str]]:
    """Parse a Python file and list all top-level functions and their return type annotations.
    解析 Python 文件并列出所有顶级函数及其返回类型注释。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    
    # Parse the source code into an AST
    # 将源代码解析为 AST
    tree = ast.parse(source)
    results: List[Tuple[str, str]] = []
    
    # Iterate over top-level nodes in the AST
    # 遍历 AST 中的顶级节点
    for node in tree.body:
        # If the node is a function definition
        # 如果节点是函数定义
        if isinstance(node, ast.FunctionDef):
            return_str = _annotation_to_str(node.returns)
            results.append((node.name, return_str))
    
    # Sort for stable output
    # 排序以获得稳定的输出
    results.sort(key=lambda x: x[0])
    return results


def output_every_func_return_type(file_path: str = None) -> str:
    """Tool: Return a newline-delimited list of "name: return_type" for each top-level function.
    工具：返回每个顶级函数的 "name: return_type" 列表，以换行符分隔。
    """
    # Use the provided path or default to the current file
    # 使用提供的路径或默认为当前文件
    path = file_path or __file__
    
    if not os.path.isabs(path):
        # Try file relative to this script if not absolute
        # 如果不是绝对路径，尝试相对于此脚本的文件
        candidate = os.path.join(os.path.dirname(__file__), path)
        if os.path.exists(candidate):
            path = candidate
            
    pairs = _list_function_return_types(path)
    return "\n".join(f"{name}: {ret}" for name, ret in pairs)


# Sample functions to ensure there is something to analyze
# 示例函数，以确保有内容可供分析
def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"

# Tool registry for dynamic execution by name
# 用于按名称动态执行的工具注册表
# Maps tool names (strings) to actual Python functions
# 将工具名称（字符串）映射到实际的 Python 函数
TOOL_REGISTRY: Dict[str, Callable[..., str]] = {
    "output_every_func_return_type": output_every_func_return_type,
}

# ==========================
# Prompt scaffolding
# 提示词脚手架
# ==========================

# TODO: Fill this in! / 请填写这里！
YOUR_SYSTEM_PROMPT = ""


def resolve_path(p: str) -> str:
    """Resolve a file path relative to the current script."""
    if os.path.isabs(p):
        return p
    here = os.path.dirname(__file__)
    c1 = os.path.join(here, p)
    if os.path.exists(c1):
        return c1
    # Try sibling of project root if needed
    # 如果需要，尝试项目根目录的兄弟目录
    return p


def extract_tool_call(text: str) -> Dict[str, Any]:
    """Parse a single JSON object from the model output.
    从模型输出中解析单个 JSON 对象。
    """
    text = text.strip()
    # Some models wrap JSON in code fences; attempt to strip
    # 一些模型将 JSON 包装在代码围栏中；尝试去除
    if text.startswith("```") and text.endswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json\n"):
            text = text[5:]
    try:
        obj = json.loads(text)
        return obj
    except json.JSONDecodeError:
        raise ValueError("Model did not return valid JSON for the tool call")


def run_model_for_tool_call(system_prompt: str) -> Dict[str, Any]:
    """Send the prompt to the model and parse the response as a tool call."""
    response = chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Call the tool now."},
        ],
        options={"temperature": 0.3},
    )
    content = response.message.content
    return extract_tool_call(content)


def execute_tool_call(call: Dict[str, Any]) -> str:
    """Execute the tool call described by the JSON object.
    执行 JSON 对象描述的工具调用。
    """
    name = call.get("tool")
    if not isinstance(name, str):
        raise ValueError("Tool call JSON missing 'tool' string")
    
    # Look up the function in the registry
    # 在注册表中查找函数
    func = TOOL_REGISTRY.get(name)
    if func is None:
        raise ValueError(f"Unknown tool: {name}")
    
    args = call.get("args", {})
    if not isinstance(args, dict):
        raise ValueError("Tool call JSON 'args' must be an object")

    # Best-effort path resolution if a file_path arg is present
    # 如果存在 file_path 参数，则尽力解析路径
    if "file_path" in args and isinstance(args["file_path"], str):
        args["file_path"] = resolve_path(args["file_path"]) if str(args["file_path"]) != "" else __file__
    elif "file_path" not in args:
        # Provide default for tools expecting file_path
        # 为期望 file_path 的工具提供默认值
        args["file_path"] = __file__

    # Call the function with unpacked arguments
    # 使用解包的参数调用函数
    return func(**args)


def compute_expected_output() -> str:
    # Ground-truth expected output based on the actual file contents
    # 基于实际文件内容的真实预期输出
    return output_every_func_return_type(__file__)


def test_your_prompt(system_prompt: str) -> bool:
    """Run once: require the model to produce a valid tool call; compare tool output to expected.
    运行一次：要求模型生成有效的工具调用；比较工具输出与预期输出。
    """
    expected = compute_expected_output()
    for _ in range(NUM_RUNS_TIMES):
        try:
            # Step 1: Get the tool call from the model
            # 步骤 1：从模型获取工具调用
            call = run_model_for_tool_call(system_prompt)
        except Exception as exc:
            print(f"Failed to parse tool call: {exc}")
            continue
        print(call)
        
        try:
            # Step 2: Execute the tool call
            # 步骤 2：执行工具调用
            actual = execute_tool_call(call)
        except Exception as exc:
            print(f"Tool execution failed: {exc}")
            continue
            
        # Step 3: Compare actual output with expected output
        # 步骤 3：比较实际输出与预期输出
        if actual.strip() == expected.strip():
            print(f"Generated tool call: {call}")
            print(f"Generated output: {actual}")
            print("SUCCESS")
            return True
        else:
            print("Expected output:\n" + expected)
            print("Actual output:\n" + actual)
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
