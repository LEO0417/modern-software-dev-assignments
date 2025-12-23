import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

# 实验配置
NUM_RUNS_TIMES = 5

# 【验证点】：我们的 System Prompt 例子里故意不包含 "音量调大 (Volume Up)" 的例子
# 我们只给它看 "空调(AC)"、"灯(Lights)" 和 "音乐(Music)" 的例子
# 看看它能不能举一反三，根据 "Volume Up" 这个自然语言，自己编出一个符合格式的 "SYS_VOLUME_UP"
YOUR_SYSTEM_PROMPT = """
你是一个智能家居指令转换器。请根据用户的自然语言，输出对应的系统指令码。
规则：
1. 始终使用 SYS_ 作为前缀。
2. 不要使用 Markdown（如 **粗体**）。
3. 只输出指令码，不要有任何其他废话。

Example 1:
Input: 打开空调
Output: SYS_AC_ON

Example 2:
Input: 关闭所有灯
Output: SYS_LIGHTS_OFF_ALL

Example 3:
Input: 播放音乐
Output: SYS_MUSIC_PLAY
"""

# 用户考题：这是一个 Prompt 里【没出现过】的新指令，但和 AC 很像
USER_PROMPT = "打开电视"

# 我们预期的标准答案
EXPECTED_OUTPUT = "SYS_TV_ON"

def test_your_prompt(system_prompt: str):
    print(f"--- 泛化能力测试开始 ---")
    print(f"目标指令: [{EXPECTED_OUTPUT}]")
    print(f"用户输入: [{USER_PROMPT}]")
    print(f"K-shot 例子包含: AC, Lights, Music (注：不包含 Volume)\n")
    
    success_count = 0
    
    for idx in range(NUM_RUNS_TIMES):
        response = chat(
            # 使用 3B 小模型来测试泛化能力
            model="ministral-3:3b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={
                "temperature": 0.1, # 调低温度，让它尽量严谨
            },
        )
        
        output_text = response.message.content.strip()
        
        # 判定逻辑
        if output_text == EXPECTED_OUTPUT:
            print(f"Test {idx+1}: SUCCESS ✅ -> {output_text}")
            success_count += 1
        else:
            print(f"Test {idx+1}: FAILED ❌ -> {output_text}")
            
    success_rate = (success_count / NUM_RUNS_TIMES) * 100
    print(f"\n最终成功率: {success_rate}%")

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
