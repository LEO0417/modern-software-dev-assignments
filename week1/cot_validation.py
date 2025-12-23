import os
import re
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

# 我们坚持使用这个做反面教材的 3B 小模型
MODEL = "ministral-3:3b"

# 硬骨头任务
USER_INPUT = "httpstatus"
EXPECTED_ANSWER = "sutatsptth"

# Few-Shot CoT Strategy: K-Shot + Step-by-Step Logic
# 我们不只给结果，还给它演示“怎么想”的过程
SYSTEM_PROMPT = """
你是一个精准的单词倒序专家。
为了保证准确性，请在回答前，严格按照以下格式展示你的思考过程：

Example 1:
Input: apple
Process:
1. List: ['a', 'p', 'p', 'l', 'e']
2. Reverse:
   - 5: e
   - 4: l
   - 3: p
   - 2: p
   - 1: a
3. Combine: elppa
Answer: elppa

Example 2:
Input: car
Process:
1. List: ['c', 'a', 'r']
2. Reverse:
   - 3: r
   - 2: a
   - 1: c
3. Combine: rac
Answer: rac
"""

USER_PROMPT = f"""
Input: {USER_INPUT}
"""

def extract_answer(text: str) -> str:
    # 简单的正则提取，匹配 Answer: 后面的内容
    match = re.search(r"Answer:\s*(\w+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ""

def test_cot():
    print(f"--- CoT 验证开始 (Model: {MODEL}) ---")
    print(f"User Prompt:\n{USER_PROMPT}\n")
    
    success_count = 0
    runs = 3
    
    for i in range(runs):
        print(f"Run {i+1}/{runs}...")
        response = chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ],
            options={"temperature": 0.1} # CoT 需要极度理性
        )
        
        content = response.message.content
        print(f"---------------- AI 思考过程 ----------------")
        print(content) 
        print(f"-------------------------------------------")
        
        prediction = extract_answer(content)
        
        if prediction == EXPECTED_ANSWER:
            print(f"✅ 成功! 提取答案: {prediction}")
            success_count += 1
        else:
            print(f"❌ 失败. 提取答案: {prediction} (预期: {EXPECTED_ANSWER})")
            
    print(f"\nFinal Success Rate: {success_count}/{runs}")

if __name__ == "__main__":
    test_cot()
