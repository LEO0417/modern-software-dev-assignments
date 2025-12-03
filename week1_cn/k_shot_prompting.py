import os  # Import the os module / 导入 os 模块
from dotenv import load_dotenv  # Import load_dotenv to manage environment variables / 导入 load_dotenv 以管理环境变量
from ollama import chat  # Import the chat function from ollama / 从 ollama 导入 chat 函数

# Load environment variables from .env file
# 从 .env 文件加载环境变量
load_dotenv()

# Define how many times to retry the test
# 定义重试测试的次数
NUM_RUNS_TIMES = 5

# TODO: Fill this in! / 请填写这里！
YOUR_SYSTEM_PROMPT = ""

# Define the user prompt for the task
# 定义任务的用户提示词
USER_PROMPT = """
Reverse the order of letters in the following word. Only output the reversed word, no other text:

httpstatus
"""
# 中文说明：
# 反转以下单词中的字母顺序。仅输出反转后的单词，不输出其他文本：
# httpstatus


# The expected correct output
# 预期的正确输出
EXPECTED_OUTPUT = "sutatsptth"

def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.
    运行提示词最多 NUM_RUNS_TIMES 次，如果有任何输出匹配 EXPECTED_OUTPUT，则返回 True。

    Prints "SUCCESS" when a match is found.
    找到匹配项时打印 "SUCCESS"。
    """
    # Iterate through the number of allowed runs
    # 遍历允许的运行次数
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        
        # Send the request to the LLM
        # 向 LLM 发送请求
        response = chat(
            model="mistral-nemo:12b",  # Using a specific model / 使用特定模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},  # Moderate creativity/randomness / 中等的创造性/随机性
        )
        
        # Get the content and strip whitespace
        # 获取内容并去除空白字符
        output_text = response.message.content.strip()
        
        # Compare with expected output
        # 与预期输出进行比较
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {output_text}")
            
    return False

# Entry point of the script
# 脚本入口点
if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
