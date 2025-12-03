import os  # Import os module / 导入 os 模块
import re  # Import re module for regex / 导入 re 模块用于正则表达式
from collections import Counter  # Import Counter to count occurrences of elements / 导入 Counter 以统计元素出现的次数
from dotenv import load_dotenv  # Import load_dotenv to manage environment variables / 导入 load_dotenv 以管理环境变量
from ollama import chat  # Import chat function from ollama / 从 ollama 导入 chat 函数

# Load environment variables
# 加载环境变量
load_dotenv()

# Number of times to run the prompt for majority voting
# 运行提示词以进行多数投票的次数
NUM_RUNS_TIMES = 5

# TODO: Fill this in! Try to get as close to 100% correctness across all runs as possible.
# TODO: 请填写这里！尝试在所有运行中尽可能接近 100% 的正确率。
YOUR_SYSTEM_PROMPT = ""

# The user prompt containing a math word problem
# 包含数学应用题的用户提示词
USER_PROMPT = """
Solve this problem, then give the final answer on the last line as "Answer: <number>".

Henry made two stops during his 60-mile bike trip. He first stopped after 20
miles. His second stop was 15 miles before the end of the trip. How many miles
did he travel between his first and second stops?
"""
# 中文说明：
# 解决这个问题，然后在最后一行给出最终答案，格式为 "Answer: <数字>"。
# 亨利在他 60 英里的自行车旅行中停了两次。他第一次停是在 20 英里后。
# 他的第二次停是在旅行结束前 15 英里。他在第一次和第二次停车之间走了多少英里？


# The expected correct answer
# 预期的正确答案
EXPECTED_OUTPUT = "Answer: 25"


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
    # Find all lines matching "Answer: ..."
    # 查找所有匹配 "Answer: ..." 的行
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        # Try to find a number in the answer string
        # 尝试在答案字符串中查找数字
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        if num_match:
            return f"Answer: {num_match.group(0)}"
        return f"Answer: {value}"
    return text.strip()


def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt NUM_RUNS_TIMES, majority-vote on the extracted 'Answer: ...' lines.
    运行提示词 NUM_RUNS_TIMES 次，对提取的 'Answer: ...' 行进行多数投票。

    Prints "SUCCESS" if the majority answer equals EXPECTED_OUTPUT.
    如果多数答案等于 EXPECTED_OUTPUT，则打印 "SUCCESS"。
    """
    answers: list[str] = []  # List to store answers from each run / 用于存储每次运行答案的列表
    
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        
        # Call the model with high temperature to encourage diversity in reasoning paths
        # 使用高温度调用模型，以鼓励推理路径的多样性
        # Self-consistency relies on sampling different reasoning paths
        # 自洽性依赖于采样不同的推理路径
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 1},  # High temperature for diversity / 高温度以增加多样性
        )
        output_text = response.message.content
        final_answer = extract_final_answer(output_text)
        print(f"Run {idx + 1} answer: {final_answer}")
        answers.append(final_answer.strip())

    if not answers:
        print("No answers produced.")
        return False

    # Count the frequency of each answer
    # 统计每个答案的频率
    counts = Counter(answers)
    
    # Get the most common answer (majority vote)
    # 获取最常见的答案（多数投票）
    majority_answer, majority_count = counts.most_common(1)[0]
    print(f"Majority answer: {majority_answer} ({majority_count}/{len(answers)})")

    # Check if the majority answer matches the expected output
    # 检查多数答案是否与预期输出匹配
    if majority_answer.strip() == EXPECTED_OUTPUT.strip():
        print("SUCCESS")
        return True

    # Print distribution for debugging when majority does not match expected
    # 当多数答案不匹配预期时，打印分布以供调试
    print(f"Expected output: {EXPECTED_OUTPUT}")
    print("Answer distribution:")
    for answer, count in counts.most_common():
        print(f"  {answer}: {count}")
    return False


if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
