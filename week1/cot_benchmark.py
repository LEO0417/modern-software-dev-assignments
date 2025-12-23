import os
import re
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

MODEL = "ministral-3:3b"
TARGET_WORD = "httpstatus"
EXPECTED_ANSWER = "sutatsptth"

# 定义 10 种不同的思维链策略 (Zero-shot CoT variants)
STRATEGIES = [
    {
        "name": "Strategy 1: 基础步骤 (Basic Step-by-Step)",
        "prompt": f"""
Task: Reverse the string "{TARGET_WORD}".
Please think step by step:
1. Break the string into a list of individual characters.
2. Output the characters in reverse order.
3. Join them back into a single string.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 2: 连字符法 (Hyphenation) - 破除 Tokenizer",
        "prompt": f"""
Task: Reverse the string "{TARGET_WORD}".
Steps:
1. First, write out the word with hyphens between EVERY letter (e.g., a-b-c). This is crucial.
2. Then, read the hyphenated string backwards character by character.
3. Write out the reversed characters with hyphens.
4. Finally remove hyphens to get the result.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 3: 垂直列表法 (Vertical List)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
Steps:
1. Write each letter of the word on a separate line, numbered 1 to 10.
2. Write a new list starting from number 10 down to 1.
3. Combine the letters from the new list.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 4: 索引表格法 (Index Table)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
Make a table with two columns: Index and Letter.
Row 1: Index 0, Letter h
Row 2: Index 1, Letter t
...
Then output the letters represented by Index 9, Index 8, ... down to 0.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 5: 栈模拟法 (Stack Simulation)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}" using a Stack data structure.
1. Push 'h' into stack.
2. Push 't' into stack.
... Continue for all letters.
3. Pop from stack one by one and write them down.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 6: Python 解释器模拟 (Python Interpreter)",
        "prompt": f"""
Act as a Python interpreter.
Execute this code mentally:
word = "{TARGET_WORD}"
reversed_list = []
for i in range(len(word) - 1, -1, -1):
    letter = word[i]
    print(f"Index {{i}} is {{letter}}")
    reversed_list.append(letter)

Output the logs of the loop, then result.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 7: 单词分块 (Chunking)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
1. Split the word into two halves: "http" and "status".
2. Reverse "http" to get part A.
3. Reverse "status" to get part B.
4. The result should be Part B + Part A. (Wait, think carefully, is it B+A? Yes, because suffix comes first in reverse).
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 8: JSON 数组法 (JSON Array)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
1. Output the word as a JSON list of single characters: ["h", "t", ...]
2. Create a new JSON list which is the reverse of the first one.
3. Concatenate the elements.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 9: 双重检查 (Double Check)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
Draft a result.
Then, reverse your draft back to see if it matches "{TARGET_WORD}".
If it doesn't match, fix your draft.
Keep trying until the re-reversed draft matches perfectly.
Format your final answer as: Answer: <string>
"""
    },
    {
        "name": "Strategy 10: 拼写教学法 (Spelling Bee)",
        "prompt": f"""
Task: Reverse "{TARGET_WORD}".
Imagine you are a teacher spelling the word backwards to a student.
"The last letter is... s"
"The second to last letter is... u"
...
Write down the letters as you say them.
Format your final answer as: Answer: <string>
"""
    }
]

def extract_answer(text: str) -> str:
    # 尝试多种格式
    match = re.search(r"Answer:\s*[*]*([a-zA-Z]+)[*]*", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def run_benchmark():
    print(f"🔥 开始 10 种 CoT 策略大逃杀 (Model: {MODEL}) 🔥\n")
    
    results = []
    
    for strategy in STRATEGIES:
        print(f"Testing {strategy['name']}...")
        
        try:
            response = chat(
                model=MODEL,
                messages=[{"role": "user", "content": strategy["prompt"]}],
                options={"temperature": 0.0} # 极致理性
            )
            
            content = response.message.content
            prediction = extract_answer(content)
            is_correct = (prediction.lower() == EXPECTED_ANSWER.lower())
            
            results.append({
                "name": strategy["name"],
                "prediction": prediction,
                "correct": is_correct,
                "raw_output": content[:200] + "..." # 只存前200字符用于预览
            })
            
            status = "✅ 成功" if is_correct else f"❌ 失败 (Got: {prediction})"
            print(f"Result: {status}\n")
            
        except Exception as e:
            print(f"Error: {e}")

    print("\n================ 最终战报 ================")
    for res in results:
        icon = "✅" if res['correct'] else "❌"
        print(f"{icon} {res['name']}")
        if not res['correct']:
            print(f"   -> Output: {res['prediction']}")

if __name__ == "__main__":
    run_benchmark()
