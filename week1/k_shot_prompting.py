import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

# 实验配置：运行 5 次以观察稳定性
NUM_RUNS_TIMES = 5

# TODO: 在这里填入 K-shot 例子，教 AI 学会“说黑话”
# 目标：将自然语言指令转换为系统标准的指令代码
YOUR_SYSTEM_PROMPT = ""

# 用户的自然语言指令
USER_PROMPT = "把音量调大一点"

# 系统期待的标准指令代码（没有任何废话）
EXPECTED_OUTPUT = "SYS_VOLUME_UP"

def test_your_prompt(system_prompt: str) -> bool:
    success_count = 0
    
    print(f"--- 测试开始：目标指令 [{EXPECTED_OUTPUT}] ---")
    
    for idx in range(NUM_RUNS_TIMES):
        response = chat(
            # 我们先使用一个 3B 的“小脑瓜”模型
            model="ministral-3:3b",
            # model="gemini-3-flash-preview:cloud", # 后面我们会切换到这个“大脑瓜”
            
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={
                "temperature": 0.5, # 课后作业：你可以尝试修改这个参数，观察 AI “脾气”的变化
            },
        )
        
        output_text = response.message.content.strip()
        
        # 判定：必须精准匹配，连标点符号都不能多
        if output_text == EXPECTED_OUTPUT:
            print(f"Test {idx+1}: SUCCESS ✅")
            success_count += 1
        else:
            print(f"Test {idx+1}: FAILED ❌ (Output: {output_text})")
            
    success_rate = (success_count / NUM_RUNS_TIMES) * 100
    print(f"\n最终成功率: {success_rate}%")
    return success_rate == 100

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)