import os
import re
from typing import Callable, List, Tuple  # Import types for type hinting / 导入类型用于类型提示
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 1  # Reflexion usually involves iterative improvement, so we might run the flow once / Reflexion 通常涉及迭代改进，所以我们可能只运行一次流程

# The initial system prompt to generate the first version of the code
# 用于生成代码第一个版本的初始系统提示词
SYSTEM_PROMPT = """
You are a coding assistant. Output ONLY a single fenced Python code block that defines
the function is_valid_password(password: str) -> bool. No prose or comments.
Keep the implementation minimal.
"""
# 中文说明：
# 你是一个编码助手。仅输出一个定义了函数 is_valid_password(password: str) -> bool 的围栏 Python 代码块。
# 不要包含散文或注释。保持实现最小化。

# TODO: Fill this in! / 请填写这里！
# This prompt will be used to ask the model to fix its mistakes based on feedback
# 此提示词将用于要求模型根据反馈修正其错误
YOUR_REFLEXION_PROMPT = ""


# Ground-truth test suite used to evaluate generated code
# 用于评估生成代码的真实测试套件
# Set of special characters required
# 所需的特殊字符集合
SPECIALS = set("!@#$%^&*()-_")

# List of test cases: (input_password, expected_result)
# 测试用例列表：(输入密码, 预期结果)
TEST_CASES: List[Tuple[str, bool]] = [
    ("Password1!", True),       # valid / 有效
    ("password1!", False),      # missing uppercase / 缺少大写字母
    ("Password!", False),       # missing digit / 缺少数字
    ("Password1", False),       # missing special / 缺少特殊字符
]


def extract_code_block(text: str) -> str:
    """Extract code block from text."""
    m = re.findall(r"```python\n([\s\S]*?)```", text, flags=re.IGNORECASE)
    if m:
        return m[-1].strip()
    m = re.findall(r"```\n([\s\S]*?)```", text)
    if m:
        return m[-1].strip()
    return text.strip()


def load_function_from_code(code_str: str) -> Callable[[str], bool]:
    """Dynamically load a function from a string of code.
    从代码字符串动态加载函数。
    WARNING: exec() is dangerous if code source is untrusted.
    警告：如果代码来源不可信，exec() 是危险的。
    """
    namespace: dict = {}
    # Execute the code string in the given namespace dictionary
    # 在给定的命名空间字典中执行代码字符串
    exec(code_str, namespace)  # noqa: S102 (executing controlled code from model for exercise)
    
    # Retrieve the function object by name
    # 按名称检索函数对象
    func = namespace.get("is_valid_password")
    if not callable(func):
        raise ValueError("No callable is_valid_password found in generated code")
    return func


def evaluate_function(func: Callable[[str], bool]) -> Tuple[bool, List[str]]:
    """Run the function against the test suite and return pass/fail status and failure messages.
    针对测试套件运行函数，并返回通过/失败状态和失败消息。
    """
    failures: List[str] = []
    for pw, expected in TEST_CASES:
        try:
            # Call the dynamically loaded function
            # 调用动态加载的函数
            result = bool(func(pw))
        except Exception as exc:
            failures.append(f"Input: {pw} → raised exception: {exc}")
            continue

        if result != expected:
            # Compute diagnostic based on ground-truth rules to give specific feedback
            # 根据真实规则计算诊断信息，以提供具体的反馈
            reasons = []
            if len(pw) < 8:
                reasons.append("length < 8")
            if not any(c.islower() for c in pw):
                reasons.append("missing lowercase")
            if not any(c.isupper() for c in pw):
                reasons.append("missing uppercase")
            if not any(c.isdigit() for c in pw):
                reasons.append("missing digit")
            if not any(c in SPECIALS for c in pw):
                reasons.append("missing special")
            if any(c.isspace() for c in pw):
                reasons.append("has whitespace")

            failures.append(
                f"Input: {pw} → expected {expected}, got {result}. Failing checks: {', '.join(reasons) or 'unknown'}"
            )

    # Return True if no failures, and the list of failure messages
    # 如果没有失败则返回 True，以及失败消息列表
    return (len(failures) == 0, failures)


def generate_initial_function(system_prompt: str) -> str:
    """Generate the first attempt at the code."""
    response = chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Provide the implementation now."},
        ],
        options={"temperature": 0.2},
    )
    return extract_code_block(response.message.content)


def your_build_reflexion_context(prev_code: str, failures: List[str]) -> str:
    """TODO: Build the user message for the reflexion step using prev_code and failures.
    TODO: 使用 prev_code 和 failures 构建反思步骤的用户消息。

    Return a string that will be sent as the user content alongside the reflexion system prompt.
    返回一个字符串，该字符串将作为用户内容与反思系统提示词一起发送。
    """
    return ""


def apply_reflexion(
    reflexion_prompt: str,
    build_context: Callable[[str, List[str]], str],
    prev_code: str,
    failures: List[str],
) -> str:
    """Ask the model to improve the code based on the failures."""
    # Build the context message containing code and error feedback
    # 构建包含代码和错误反馈的上下文消息
    reflection_context = build_context(prev_code, failures)
    print(f"REFLECTION CONTEXT: {reflection_context}, {reflexion_prompt}")
    
    response = chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": reflexion_prompt},
            {"role": "user", "content": reflection_context},
        ],
        options={"temperature": 0.2},
    )
    return extract_code_block(response.message.content)


def run_reflexion_flow(
    system_prompt: str,
    reflexion_prompt: str,
    build_context: Callable[[str, List[str]], str],
) -> bool:
    # 1) Generate initial function
    # 1) 生成初始函数
    initial_code = generate_initial_function(system_prompt)
    print("Initial code:\n" + initial_code)
    
    # Load and test the initial function
    # 加载并测试初始函数
    func = load_function_from_code(initial_code)
    passed, failures = evaluate_function(func)
    
    if passed:
        print("SUCCESS (initial implementation passed all tests)")
        return True
    else:
        print(f"FAILURE (initial implementation failed some tests): {failures}")

    # 2) Single reflexion iteration
    # 2) 单次反思迭代
    # Use the failures to ask for a better version
    # 使用失败信息请求更好的版本
    improved_code = apply_reflexion(reflexion_prompt, build_context, initial_code, failures)
    print("\nImproved code:\n" + improved_code)
    
    # Load and test the improved function
    # 加载并测试改进后的函数
    improved_func = load_function_from_code(improved_code)
    passed2, failures2 = evaluate_function(improved_func)
    if passed2:
        print("SUCCESS")
        return True

    print("Tests still failing after reflexion:")
    for f in failures2:
        print("- " + f)
    return False


if __name__ == "__main__":
    run_reflexion_flow(SYSTEM_PROMPT, YOUR_REFLEXION_PROMPT, your_build_reflexion_context)
