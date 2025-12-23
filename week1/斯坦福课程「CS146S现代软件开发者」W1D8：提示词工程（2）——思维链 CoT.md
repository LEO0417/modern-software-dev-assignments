# 斯坦福课程「CS146S现代软件开发者」W1D8：提示词工程（2）——思维链 CoT

在前两课中，我们学习了如何用 Python 搭建自动化监控系统，以及如何通过 K-shot 给 AI 喂例子。今天，我们要学习 Prompt Engineering 中最强大的“逻辑炸药”——**Chain of Thought (CoT，思维链)**。

当 AI 面对极其复杂的逻辑（如数学运算、法律分析）时，简单的例子可能已经不够用了。我们需要教 AI 如何**“打草稿”**。

---

## 1. 逻辑的“银弹”：为什么 AI 需要打草稿？

### 1.1 案例：心算 vs 笔算
- **场景 A (心算)**：我问你“3^{12345} (mod 100) 是多少？”，并要求你**秒回**一个数字。你大概率会 CPU 烧过载，然后蒙一个错答案。
- **场景 B (笔算)**：我给你一张纸和一支笔，让你慢慢写下推导过程（先算 3^1, 3^2, 3^3... 找规律），最后再告诉我答案。你做对的概率会大幅提升。

### 1.2 什么是思维链 CoT？
思维链就是让 AI 在输出最终答案之前，先吐出一大串**“推理中间过程”**。

#### 💡 核心心智模型
- **时间换智力**：AI 的智力很大程度上取决于它输出过程中产生的 Token 数量。输出的推理过程越详细，它由于“逻辑中断”而翻车的概率就越低。
- **自适应逻辑**：与其给它 100 个例子，不如教它一套“思考方法”。

---

## 2. 深度手术：解剖 `chain_of_thought.py`

在这一课的脚本中，我们要解决一个数学难题：计算 **3 的 12345 次方除以 100 的余数**。

### 2.1 全景预览：思考与提取的配合
*(完整代码请在视频介绍中领取)*

```python
import os
import re  # 核心零件：正则表达式(筛选器)
from dotenv import load_dotenv
from ollama import chat

# 我们这次的任务：一个高难度的数学题
USER_PROMPT = """
解决这个问题，然后在最后一行以 "Answer: <数字>" 的格式给出最终答案。
计算 3^{12345} (mod 100) 的值是多少？
"""

def extract_final_answer(text: str) -> str:
    # 核心零件：正则表达式(提取 Answer 后的数字)
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        return f"Answer: {value}"
    return text.strip()

def test_your_prompt(system_prompt: str):
    # 使用 Gemini-3-Flash 这样的推理强模型
    response = chat(
        model="gemini-3-flash-preview:cloud",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": USER_PROMPT},
        ]
    )
    full_text = response.message.content
    print(f"--- AI 的思考过程 ---\n{full_text}\n")
    
    # 将长篇大论送入“筛选器”
    final_answer = extract_final_answer(full_text)
    print(f"--- 最终提取答案 ---\n{final_answer}")
```

### 2.2 逻辑解剖：为什么要用正则表达式 (RegEx)？
当你开启了 CoT，AI 会变得非常话痨。它会写出几百字的推导过程，但我们的自动化系统只需要那个数字。这时候我们需要一个**“筛子”**。

#### L1 入门：比喻——自动分拣机
RegEx（正则表达式）就是程序员的**自动分拣机**。你给它一堆乱七八糟的废铜烂铁（AI 的推理原文），它能根据你定义的“形状”（匹配规则），瞬间把那个金子（答案）吸出来。

#### L2 语法：数字的“照妖镜”
在 Python 中，通过 `import re` 我们可以使用它：
- `\d`：代表一个数字。
- `+`：代表一个或多个。
- `re.findall`：帮你在长文中找所有符合条件的。

#### L3 深度：结构化输出的尊严
在 `chain_of_thought.py` 中，我们用了这行：
`r"(?mi)^\s*answer\s*:\s*(.+)\s*$"`
这意味着：**不管 AI 把 Answer 写在开头、结尾，也不管它加了几个空格，只要它写了 `Answer: 数字`，我们就能把它揪出来。**

---

## 3. 思维链的变身术：从“魔法”到“工程”

### 3.1 Zero-shot CoT：一句顶一万句
如果你不想写复杂的教案，只需在 Prompt 结尾加一句话：
> **“Let's think step by step” (让我们一步步思考)**

这是 AI 历史上的一个著名发现：只需这一句话，就能让 AI 在数学、逻辑任务上的表现呈指数级增长。

### 3.2 Manual CoT：手把手教 AI 断案
在你的 `YOUR_SYSTEM_PROMPT` 中，你可以规定 AI 思考的框架：
```python
YOUR_SYSTEM_PROMPT = """
你是一个严谨的数学家。
在解决问题时，请务必遵循以下步骤：
1. 找出前 5 次幂的规律 (3^1, 3^2...)。
2. 确定余数的循环周期。
3. 计算 12345 属于周期的哪个位置。
最后，给出最终答案。
"""
```

---

## 4. 降维打击：为什么不仅要 K-shot，更要 CoT？

#### 💡 核心心智模型
- **K-shot 解决的是“怎么说” (Format)**：通过例子告诉 AI 输出的格式。
- **CoT 解决的是“怎么想” (Logic)**：通过引导推理过程，解决 AI 的“幻觉”问题。

**如果你发现一个任务 AI 给足了例子还是做错，请立即开启 CoT 让它“打草稿”。**

---

## 本课总结

1. **过程重于结果**：复杂逻辑必须要求 AI 输出推理过程。
2. **后处理的必要性**：思考越多，“杂音”越多，必须学会用 **RegEx (正则表达式)** 提取结果。
3. **标准化输出**：在 Prompt 中强制要求以 `Answer: <结果>` 结尾，是实现自动化的关键。

---

## 预告：终极武器库——Tool Calling (工具调用)
如果 AI 的思考能力也达到了极限（比如算 1234567 * 7654321 这种纯计算任务），该怎么办？下一课，我们将学习如何让 AI 停止“硬算”，而是学会去**调用计算器和搜索工具**。
