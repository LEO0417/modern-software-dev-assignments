# Lesson 2: The Machine (造物主 - 函数与 Agent 协作) ⚙️ (口播稿)

> **场景建议**：背景音为机械臂组装的声音，充满工业美感。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Recap) - 3 min

**领航员**：
欢迎回来，各位学徒。
在 Lesson 1 中，我们在飞船的甲板上贴满了便以此（Variables），学会了分清哪个是 `String`，哪个是 `Int`。

但现在，我有了一个新问题。
如果我让你计算飞船上 100 个船员的薪水，每个人都要扣除 20% 的税，再加上 500 块的补贴。
如果你只用变量，你得写 100 次 `(salary * 0.8) + 500`。
只要算错一个，全船都要暴动。

今天，我们要学习如何制造**机器**。
也就是 **Function (函数)**。
更重要的是，我们要学会如何让你的 **Right Panel (AI Agent)** 帮你设计这台机器说明书。

---

## 1. 定义机器 (The Blueprint) - 5 min

**领航员**：
函数，本质上就是一个**黑盒子**。
它有入口（Input），有出口（Output）。

**(Step 1: Hand-write)**
我们先手写一个最简单的。
```python
def calculate_pay(salary):
    # 机器内部的齿轮
    tax_rate = 0.2
    bonus = 500
    final_pay = (salary * (1 - tax_rate)) + bonus
    return final_pay
```

**领航员**：
注意几个关键点：
1.  `def` 是告诉 Python：“我要造机器了”。
2.  `salary` 是原材料入口（Arguments）。
3.  `return` 是产品出口。这行非常关键！如果没有 `return`，这台机器就算造出来了，产品也拿不出来。

---

## 2. Agent 协作：解释代码 (Visualizing Logic) - 5 min

**领航员**：
现在，把目光移到右边的 **Right Panel (Agent)**。
很多新手写函数，写着写着就把逻辑搞乱了。
这时候，Agent 就是你的**透视眼**。

**(Step 2: Explain)**
假设你写了一个很复杂的函数，里面有一堆数学公式。
你可以**选中代码**，然后在右边问 Agent：
> "Agent, explain this function step-by-step. specificly, how is the tax calculated?"

Agent 不仅会用自然语言告诉你“先乘 0.8，再加 500”，它甚至可以用伪代码画出流程图。
**训练目标**：不要只盯着代码发呆。看不懂的时候，马上问 Agent。这是 Stanford Course 中阅读别人源码的唯一方式。

---

## 3. Agent 协作：生成说明书 (Docstrings) - 6 min

**领航员**：
不仅如此。
一台好的机器，必须有**说明书**。
在 Python 里，这叫 **Docstring (文档字符串)**。就是函数第一行那个三引号包裹的文字。

很多人懒得写。但你是 **Stanford Prep** 的学员，你不能懒。
或者说，你可以“懒”，但要懒得有技巧。

**(Step 3: Generate Docstring)**
选中刚才那个 `calculate_pay` 函数。
在 Right Panel 输入：
> "Generate a Google-style docstring for this function."

Agent 会立刻帮你生成：
```python
def calculate_pay(salary):
    """Calculates the final pay after tax and bonus.

    Args:
        salary (float): The base salary amount.

    Returns:
        float: The final calculated pay.
    """
    ...
```
**领航员**：
看！这就叫专业。
在未来的大项目中，IDE 只要把鼠标悬停在函数名上，就会显示这段文字。
而你，只花了一句话的时间。

---

## 4. Agent 协作：编写测试 (Unit Testing) - 4 min

**领航员**：
机器造好了，说明书也写了。
敢不敢直接上线？
**绝对不敢。**

你需要测试。
但在旧时代，写测试很痛苦。你需要自己算各种边缘情况。
现在，把这个任务交给 Agent。

**(Step 4: Generate Tests)**
在 Right Panel 输入：
> "Write 3 unit tests for this function using asserts. Include edge cases (like 0 salary)."

Agent 可能会给你：
```python
assert calculate_pay(1000) == 1300.0
assert calculate_pay(0) == 500.0  # 即使没工资也能拿补贴？
```
**领航员**：
你会发现，有时候 Agent 生成的测试会让你反思：“咦？工资为 0 的时候真的应该发补贴吗？”
这就是 **AI-Driven Development**。AI 是你的镜子，帮你发现逻辑漏洞。

---

## 5. 总结 (Closing) - 2 min

**领航员**：
今天我们不仅学会了写函数。
我们更学会了**Agent Workflow**：
1.  我写核心逻辑。
2.  Agent 帮我解释 (Explain)。
3.  Agent 帮我写文档 (Docstring)。
4.  Agent 帮我写测试 (Test)。

这样，你就不再是一个孤独的代码工人在搬砖。
你是一个**指挥官**，带着一支精锐部队在战斗。

下一节课 (Lesson 3)，我们将面对更庞大的敌人：**Data (数据)**。
我们将学习 List 和 Dictionary，并且让 Agent 帮我们“看见”数据。

**System check. Agent sync complete.**
(系统检查。Agent 同步完成。)
