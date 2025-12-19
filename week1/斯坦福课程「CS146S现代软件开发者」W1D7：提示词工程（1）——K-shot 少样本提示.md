# 斯坦福课程「CS146S现代软件开发者」W1D7：提示词工程（1）——K-shot 少样本提示

在上一课 (W1D6) 中，我们学习了如何利用函数、循环和布尔逻辑来“约束” AI。今天，我们将把这些逻辑零件组装起来，完成一个真正的进阶任务：**通过示例引导（K-shot），教 AI 掌握最让它头疼的字符逻辑。**

---

## 1. 核心理论：K-shot 少样本提示

### 1.1 模仿的力量 (Learning from Examples)
- **Zero-shot (无例子)**：全靠模型自己的领悟力。
- **K-shot (K 代表数量)**：我们在 Prompt 中通过“打样”来告诉模型：**“这就是我要的风格、逻辑和格式”**。

**为什么要用 K-shot？**
1.  **逻辑对齐**：当文字命令无法解释复杂的逻辑（如“反转字符串”）时，给几个例子是最廉价、最有效的教学方式。
2.  **格式纠偏**：通过例子，可以强制模型只输出你想要的内容，而不带任何“废话”。

---

## 2. 自动化实战解析：`k_shot_prompting.py`

我们将分析一个完整的自动化测试脚本。它不仅给 AI 提供了示例，还利用循环跑了 5 次，并用布尔逻辑自动判断测试是否通过。

### 2.1 完整源码预览
```python
import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

YOUR_SYSTEM_PROMPT = """
你是字符处理专家。请将单词字母反转。
示例 1: apple -> elppa
示例 2: cat -> tac
"""

USER_PROMPT = "httpstatus"
EXPECTED_OUTPUT = "sutatsptth"

def test_your_prompt(system_prompt: str) -> bool:
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="ministral-3:3b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
        output_text = response.message.content.strip()
        if output_text == EXPECTED_OUTPUT:
            print("SUCCESS")
            return True
        else:
            print(f"Expect: {EXPECTED_OUTPUT} | Actual: {output_text}")
    return False

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
```

---

### 2.2 逐逻辑块拆解

#### 全局配置与 K-shot 样板
这是程序的“控制中心”。我们通过 `YOUR_SYSTEM_PROMPT` 注入了两个关键例子。
```python
NUM_RUNS_TIMES = 5  # 我们要重复测 5 次，验证稳健性

YOUR_SYSTEM_PROMPT = """
你是字符处理专家。请将单词字母反转。
示例 1: apple -> elppa
示例 2: cat -> tac
"""
```

#### 定义自动化裁判
这个函数包裹了所有的测试逻辑。它接受我们的 Prompt，返回一个布尔值结果。
```python
def test_your_prompt(system_prompt: str) -> bool:
    # 启动复读机模式：开始 5 次循环测试
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        # 下一页我们将看到通信逻辑...
```

#### 与 AI 通信并清洗数据
我们将原材料发送给 AI，并把拿到的“包裹”进行拆解和去空格处理。
```python
        response = chat(
            model="ministral-3:3b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
        # 清洗数据：strip() 是必修课
        output_text = response.message.content.strip()
```

#### 处理裁判逻辑
利用 W1D6 学到的布尔值比对，决定这次测试的成败。
```python
        # 像素级比对：电脑不接受“差不多”
        if output_text == EXPECTED_OUTPUT:
            print("SUCCESS")
            return True # 只要成功一轮，说明 Prompt 具备成功潜质
        else:
            # 失败时打印对比，辅助我们调优 Prompt
            print(f"Expect: {EXPECTED_OUTPUT} | Actual: {output_text}")
            
    return False # 5 次机会都用完了还没成功
```

#### 红色启动开关
这是程序的生命起点。
```python
if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
```

---

## 3. 进阶探讨：当 K-shot 也无力回天

在运行上述脚本时，你可能会发现 `ministral-3:3b` 依然死活答不对。这并不是你的 Prompt 没写好，而是触碰到了**“地基智力天花板”**。

### 3.1 为什么它学不会？（Tokenization 的诅咒）
- **原因**：AI 并不是像人类一样阅读字母。它看到的是 **Token (词元)**。
- 对于 `ministral` 这样的小模型，`httpstatus` 对它来说可能就是一个无法拆解的整体块。由于它的“脑容量”有限，它无法在脑内完成“拆碎-反转-重组”的高难度体操。

### 3.2 进阶方案：模型智力升级
面对此类硬核逻辑任务，最有效的手段往往是换一个更聪明的大脑——**推理模型 (Reasoning Model)**。

**实验对比：**
在代码中，将 `model` 修改为云端版本：
```python
response = chat(
    model="gemini-3-flash-preview:cloud", # 换成逻辑高手
    ...
)
```
**课后观察：**
你会惊奇地发现，换了模型后，Gemini 甚至不需要任何 K-shot 例子 (0-shot) 就能直接反转成功。

---

## 4. 总结与反思

今天我们学会了：
1. **K-shot** 是通过“模仿”来引导 AI 逻辑的强力武器。
2. **自动化测试** 是验证 Prompt 稳健性的唯一标准。
3. **模型智力** 是底座。Prompt 优化是“术”，模型智商是“道”。

### 课后练习：
1. 运行同步下发的 `k_shot_prompting.py`。
2. 观察 `ministral` 报错的结果，尝试分析它的错误规律。
3. 修改代码切换到 `gemini` 模型，见证真正的“智力压制”。

---

## 预告：下一课的挑战
在面对比“反转字符串”更复杂的逻辑——如高次幂数学竞赛题时，连 K-shot 也会失效。我们将学习 AI 届的必杀技：**思维链 (Chain of Thought)**。
我们将解锁如何让 AI 在回答答案之前，先在黑板上写出它的推导过程（Show Your Work）。
