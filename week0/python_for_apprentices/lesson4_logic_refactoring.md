# Lesson 4: The Architect (大工匠 - 类型、重构与 Agent 审查) 📐 (口播稿)

> **场景建议**：背景音是那种无尘实验室里安静、精密的仪器运转声。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Recap) - 3 min

**领航员**：
学徒们，这是 Phase 1 的最后一课。
我们有了变量，有了函数，有了列表。你的代码已经可以跑起来了。
但是，“能跑”的代码和“专业”的代码之间，隔着一条巨大的鸿沟。

Stanford 的课程要求我们写的代码必须是 **Robust (健壮)** 和 **Readable (可读)** 的。
今天我们要学习两项高级技能：
1.  **Type Hints (类型提示)**：给代码加上说明书。
2.  **Logic & Refactoring (逻辑与重构)**：把烂代码变废为宝。

更重要的是，我们将学会让 **Right Panel (Agent)** 变成你的**Code Reviewer (代码审查员)**。

---

## 1. 类型提示：给 AI 的说明书 (Type Hints) - 5 min

**领航员**：
看这个函数：
```python
def add(a, b):
    return a + b
```
如果我传 `1, 2`，它返回 `3`。
如果我传 `"Big", "Apple"`，它返回 `"BigApple"`。
这很灵活，但也极其危险。因为你不知道设计者到底是想让你传数字还是字符串。

**(Step 1: Code)**
让我们加上类型提示：
```python
# 告诉 Anti-gravity：a 和 b 必须是 int，返回的也是 int
def add(a: int, b: int) -> int:
    return a + b
```
**领航员**：
加上这几个字，Python 运行起来其实没有任何区别（Python 会忽略它们）。
但是！你的 IDE (Agent) 看懂了。
如果你现在写 `add("hi", "there")`，IDE 会给你画波浪线警告。
这叫 **Static Analysis (静态分析)**。这是大厂代码的标配。

---

## 2. 逻辑控制与屎山 (Logic Spaghetti) - 5 min

**领航员**：
现在，让我们看一段写的很烂的代码。也就是传说中的“屎山” (Spaghetti Code)。

**(Step 2: Bad Code)**
新建 `messy_code.py`：
```python
score = 85
if score > 90:
    print("A")
else:
    if score > 80:
        print("B")
    else:
        if score > 70:
            print("C")
        else:
            print("D")
```
这种嵌套的 `if/else` 就像楼梯一样，丑陋且难读。
如果再多几层，你自己都会迷路。

---

## 3. Agent 协作：重构 (Refactoring) - 6 min

**领航员**：
怎么修？手改吗？不。
让 **Right Panel Agent** 来做。

**(Step 3: AI Refactor)**
选中这段烂代码。
在右边输入 Prompt：
> "Refactor this code to flatten the nested logic. Use `elif` clauses. Also, clean it up into a function."

Agent 会秒生成：
```python
def get_grade(score: int) -> str:
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    else:
        return "D"
```
你需要给学徒展示对比图：
*   Before: 像个向右倒的金字塔。
*   After: 像一条直线。
**领航员**：
这就是 **Refactoring (重构)**。
代码的功能没变，但结构变得极其清晰。
在未来的开发中，Code Review 主要就是在干这件事。

---

## 4. Agent 协作：静态分析解释 (Analysis) - 4 min

**领航员**：
有时候，IDE 会给你画各种颜色的波浪线。
黄色警告，红色错误。
新手看到这些会心慌。但现在，你有 Agent。

**(Step 4: Ask Agent)**
故意写错一个逻辑，或者鼠标悬停在波浪线上。
然后在 Right Panel 问：
> "What does this warning mean? How do I fix it according to PEP 8 standards?"

Agent 不仅会告诉你“缩进不对”或者“类型不匹配”，还会告诉你“PEP 8 标准建议每行不超过 79 个字符”。
它会教你不只做把题做对，还要做得**Elegant (优雅)**。

---

## 5. 总结 (Closing) - 2 min

**领航员**：
恭喜你们。
你们现在不仅会写代码，还会写“漂亮”的代码。
变量、函数、列表、类型、重构。
这五块积木拼在一起，就是 **Stanford Prep Phase 1** 的全部内容。

下一节课 (Lesson 5)，我们将进行最后的盘点，并且进行一次特殊的**“面试”**。
是的，你的面试官，就是右边的那个 Agent。

**Codebase secured. Architecture verified.**
(代码库安全。架构验证完毕。)
