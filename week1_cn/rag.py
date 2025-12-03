import os  # Import os for file path handling / 导入 os 用于文件路径处理
import re  # Import re for regular expressions / 导入 re 用于正则表达式
from typing import List, Callable  # Import type hints for better code clarity / 导入类型提示以提高代码清晰度
from dotenv import load_dotenv  # Import load_dotenv to load .env variables / 导入 load_dotenv 以加载 .env 变量
from ollama import chat  # Import chat function from ollama / 从 ollama 导入 chat 函数

# Load environment variables
# 加载环境变量
load_dotenv()

# Number of times to run the test
# 运行测试的次数
NUM_RUNS_TIMES = 5

# Define the path to the data files using os.path.join for cross-platform compatibility
# 使用 os.path.join 定义数据文件的路径，以实现跨平台兼容性
# __file__ refers to the current script file
# __file__ 指的是当前脚本文件
DATA_FILES: List[str] = [
    os.path.join(os.path.dirname(__file__), "data", "api_docs.txt"),
]


def load_corpus_from_files(paths: List[str]) -> List[str]:
    """Load the content of text files into a list of strings.
    将文本文件的内容加载到字符串列表中。
    """
    corpus: List[str] = []  # Initialize an empty list / 初始化一个空列表
    for p in paths:  # Iterate over each path / 遍历每个路径
        if os.path.exists(p):  # Check if file exists / 检查文件是否存在
            try:
                # Open file in read mode with utf-8 encoding
                # 以 utf-8 编码的读取模式打开文件
                with open(p, "r", encoding="utf-8") as f:
                    corpus.append(f.read())  # Read content and add to list / 读取内容并添加到列表
            except Exception as exc:  # Catch any errors during reading / 捕获读取过程中的任何错误
                corpus.append(f"[load_error] {p}: {exc}")
        else:
            corpus.append(f"[missing_file] {p}")
    return corpus


# Load corpus from external files (simple API docs). If missing, fall back to inline snippet
# 从外部文件加载语料库（简单的 API 文档）。如果缺失，则回退到内联片段
CORPUS: List[str] = load_corpus_from_files(DATA_FILES)

# The question/task for the LLM
# LLM 的问题/任务
QUESTION = (
    "Write a Python function `fetch_user_name(user_id: str, api_key: str) -> str` that calls the documented API "
    "to fetch a user by id and returns only the user's name as a string."
)
# 中文说明：
# 编写一个 Python 函数 `fetch_user_name(user_id: str, api_key: str) -> str`，调用文档中的 API
# 根据 id 获取用户，并仅返回用户的名称（字符串）。


# TODO: Fill this in! / 请填写这里！
YOUR_SYSTEM_PROMPT = ""


# For this simple example
# For this coding task, validate by required snippets rather than exact string
# 对于这个简单的例子
# 对于这个编码任务，通过所需的代码片段而不是精确的字符串来验证
REQUIRED_SNIPPETS = [
    "def fetch_user_name(",
    "requests.get",
    "/users/",
    "X-API-Key",
    "return",
]


def YOUR_CONTEXT_PROVIDER(corpus: List[str]) -> List[str]:
    """TODO: Select and return the relevant subset of documents from CORPUS for this task.
    TODO: 为此任务从 CORPUS 中选择并返回相关的文档子集。

    For example, return [] to simulate missing context, or [corpus[0]] to include the API docs.
    例如，返回 [] 以模拟缺少上下文，或返回 [corpus[0]] 以包含 API 文档。
    """
    return []


def make_user_prompt(question: str, context_docs: List[str]) -> str:
    """Construct the final user prompt by combining the question and the retrieved context.
    通过结合问题和检索到的上下文来构建最终的用户提示词。
    """
    if context_docs:
        # Join all context documents with newlines and bullet points
        # 用换行符和项目符号连接所有上下文文档
        context_block = "\n".join(f"- {d}" for d in context_docs)
    else:
        context_block = "(no context provided)"
    
    # Return a formatted string (f-string)
    # 返回格式化字符串 (f-string)
    return (
        f"Context (use ONLY this information):\n{context_block}\n\n"
        f"Task: {question}\n\n"
        "Requirements:\n"
        "- Use the documented Base URL and endpoint.\n"
        "- Send the documented authentication header.\n"
        "- Raise for non-200 responses.\n"
        "- Return only the user's name string.\n\n"
        "Output: A single fenced Python code block with the function and necessary imports.\n"
    )


def extract_code_block(text: str) -> str:
    """Extract the last fenced Python code block, or any fenced code block, else return text.
    提取最后一个围栏 Python 代码块，或任何围栏代码块，否则返回文本。
    """
    # Try ```python ... ``` first (case-insensitive)
    # 首先尝试 ```python ... ``` (不区分大小写)
    # [\s\S]*? matches any character including newlines, non-greedily
    # [\s\S]*? 匹配包括换行符在内的任何字符，非贪婪模式
    m = re.findall(r"```python\n([\s\S]*?)```", text, flags=re.IGNORECASE)
    if m:
        return m[-1].strip()  # Return the content of the last match / 返回最后一个匹配项的内容
    
    # Fallback to any fenced code block ``` ... ```
    # 回退到任何围栏代码块 ``` ... ```
    m = re.findall(r"```\n([\s\S]*?)```", text)
    if m:
        return m[-1].strip()
    return text.strip()


def test_your_prompt(system_prompt: str, context_provider: Callable[[List[str]], List[str]]) -> bool:
    """Run up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.
    运行最多 NUM_RUNS_TIMES 次，如果有任何输出匹配 EXPECTED_OUTPUT，则返回 True。
    """
    # Get context using the provider function
    # 使用提供者函数获取上下文
    context_docs = context_provider(CORPUS)
    
    # Create the full user prompt
    # 创建完整的用户提示词
    user_prompt = make_user_prompt(QUESTION, context_docs)

    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            options={"temperature": 0.0},  # Zero temperature for deterministic output / 零温度以获得确定性输出
        )
        output_text = response.message.content
        
        # Extract code from the response
        # 从响应中提取代码
        code = extract_code_block(output_text)
        
        # Check if all required snippets are present in the code
        # 检查代码中是否包含所有必需的片段
        # List comprehension to find missing snippets
        # 列表推导式用于查找缺失的片段
        missing = [s for s in REQUIRED_SNIPPETS if s not in code]
        
        if not missing:
            print(output_text)
            print("SUCCESS")
            return True
        else:
            print("Missing required snippets:")
            for s in missing:
                print(f"  - {s}")
            print("Generated code:\n" + code)
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT, YOUR_CONTEXT_PROVIDER)
