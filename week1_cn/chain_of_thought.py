import os  # Import the os module to interact with the operating system / 导入 os 模块以与操作系统交互
import re  # Import the re module for regular expressions / 导入 re 模块以使用正则表达式
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file / 从 dotenv 导入 load_dotenv 以从 .env 文件加载环境变量
from ollama import chat  # Import the chat function from the ollama library / 从 ollama 库导入 chat 函数

# Load environment variables from the .env file
# 从 .env 文件加载环境变量
load_dotenv()

# Define a constant for the number of times to run the test
# 定义一个常量，表示运行测试的次数
NUM_RUNS_TIMES = 5

# TODO: Fill this in! / 请填写这里！
# The system prompt defines the behavior and persona of the AI model
# 系统提示词定义了 AI 模型的行为和角色
YOUR_SYSTEM_PROMPT = ""


# Define the user prompt, which is the specific task or question for the model
# 定义用户提示词，这是给模型的具体任务或问题
USER_PROMPT = """
Solve this problem, then give the final answer on the last line as "Answer: <number>".

what is 3^{12345} (mod 100)?
"""
# 中文说明：
# 解决这个问题，然后在最后一行给出最终答案，格式为 "Answer: <数字>"。
# 3^{12345} (mod 100) 是多少？


# For this simple example, we expect the final numeric answer only
# 对于这个简单的例子，我们只期望最终的数字答案
EXPECTED_OUTPUT = "Answer: 43"


def extract_final_answer(text: str) -> str:
    """Extract the final 'Answer: ...' line from a verbose reasoning trace.
    从详细的推理过程中提取最后的 'Answer: ...' 行。

    - Finds the LAST line that starts with 'Answer:' (case-insensitive)
      找到最后一行以 'Answer:' 开头的行（不区分大小写）
    - Normalizes to 'Answer: <number>' when a number is present
      当存在数字时，标准化为 'Answer: <number>'
    - Falls back to returning the matched content if no number is detected
      如果未检测到数字，则回退到返回匹配的内容
    """
    # Use regex to find all lines starting with 'Answer:'. (?mi) flags mean multiline and case-insensitive.
    # 使用正则表达式查找所有以 'Answer:' 开头的行。(?mi) 标志表示多行模式和不区分大小写。
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    
    # If any matches were found
    # 如果找到了任何匹配项
    if matches:
        # Get the last match found
        # 获取找到的最后一个匹配项
        value = matches[-1].strip()
        
        # Prefer a numeric normalization when possible (supports integers/decimals)
        # 尽可能使用数字标准化（支持整数/小数）
        # re.search looks for a number pattern in the string
        # re.search 在字符串中查找数字模式
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        
        # If a number is found, format it as "Answer: <number>"
        # 如果找到了数字，将其格式化为 "Answer: <数字>"
        if num_match:
            return f"Answer: {num_match.group(0)}"
        
        # If no number found, return the original value
        # 如果没找到数字，返回原始值
        return f"Answer: {value}"
    
    # If no "Answer:" line found, return the whole text stripped of whitespace
    # 如果没有找到 "Answer:" 行，返回去除空白字符的整段文本
    return text.strip()


def test_your_prompt(system_prompt: str) -> bool:
    """Run up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.
    运行最多 NUM_RUNS_TIMES 次，如果有任何输出匹配 EXPECTED_OUTPUT，则返回 True。

    Prints "SUCCESS" when a match is found.
    找到匹配项时打印 "SUCCESS"。
    """
    # Loop NUM_RUNS_TIMES times
    # 循环 NUM_RUNS_TIMES 次
    for idx in range(NUM_RUNS_TIMES):
        # Print the current run number (f-string allows embedding variables)
        # 打印当前运行次数（f-string 允许嵌入变量）
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        
        # Call the chat function from ollama
        # 调用 ollama 的 chat 函数
        response = chat(
            model="llama3.1:8b",  # Specify the model to use / 指定要使用的模型
            messages=[
                {"role": "system", "content": system_prompt},  # Pass the system prompt / 传递系统提示词
                {"role": "user", "content": USER_PROMPT},      # Pass the user prompt / 传递用户提示词
            ],
            options={"temperature": 0.3},  # Set temperature (randomness) / 设置温度（随机性）
        )
        
        # Extract the content from the response message
        # 从响应消息中提取内容
        output_text = response.message.content
        
        # Extract the final answer using our helper function
        # 使用我们的辅助函数提取最终答案
        final_answer = extract_final_answer(output_text)
        
        # Check if the extracted answer matches the expected output
        # 检查提取的答案是否与预期输出匹配
        if final_answer.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True  # Return True if successful / 如果成功则返回 True
        else:
            # Print expected vs actual output for debugging
            # 打印预期输出和实际输出以供调试
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {final_answer}")
            
    return False  # Return False if all runs failed / 如果所有运行都失败则返回 False


# This block ensures the code runs only if executed directly, not when imported
# 此代码块确保代码仅在直接执行时运行，而不是在被导入时运行
if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
