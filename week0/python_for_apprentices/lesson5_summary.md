# Lesson 5: The Checkpoint (检查站 - 晋升总结与 Agent 面试) 🏁 (口播稿)

> **场景建议**：背景音宏大、充满史诗感，仿佛置身于机库中准备登机。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor)

---

## 0. 总结回顾 (The Debriefing) - 4 min

**领航员**：
立正，学徒们！

在过去的四节课里，你们经历了一场高强度的训练，为 **Stanford Modern Software Development Course** 迈出了坚实的第一步。
让我们快速回放一下我们拿到的四枚勋章：

1.  **勋章一：基础语法 (Lesson 1)**
    Variables & Types，特别是 **f-string**。这是 Prompt Engineering 的基石。
2.  **勋章二：封装之术 (Lesson 2)**
    Functions & Docstrings。我们学会了指挥 Agent 生成说明书和测试。
3.  **勋章三：收纳之道 (Lesson 3)**
    Lists & Dicts。我们学会了指挥 Agent 帮我们“看见”复杂的数据结构。
4.  **勋章四：大工匠精神 (Lesson 4)**
    Type Hints & Refactoring。我们学会了让 Agent 充当代码审查员，清理屎山。

现在的你们，已经不再是 Python 世界的婴儿。
你们已经具备了 **Stanford Prep Apprentice** 的资格。

---

## 1. 毕业挑战：Agent Mock Interview (模拟面试) - 8 min

**领航员**：
在以往，我会给你们出几道题。
但今天，我要教你们一种全新的复习方式。
我们将利用 **Right Panel Agent** 进行一场 **Mock Interview (模拟面试)**。

**(Step 1: Setup)**
请在 Right Panel 输入以下 Prompt：
> "Act as a strict Python interviewer. I am applying for a junior developer role. Ask me 3 questions based on Python functions, lists, and type hints. Do not give me the answers immediately. Wait for my response and then grade me."

**领航员**：
看，Role Play 开始了。
Agent 可能会问：
> "Question 1: What is the difference between a list and a dictionary? When would you use a dictionary over a list?"

你可以直接在 Chat 框里回答（用自然语言或者代码）。
比如你回答：*"List is ordered, Dict is key-value."*
Agent 会评价：*"Correct. But can you explain the time complexity for lookup?"*
(如果它问得太深，你可以让它 Explain like I'm 5)。

这就是 **Active Recall (主动回忆)**。比死记硬背强一万倍。

---

## 2. 实战演习：The Library System - 8 min

**领航员**：
面试通过了。现在来实战。
我们把前四课的内容串起来，做一个微型的“图书管理系统”。
当然，是全程与 Agent 协作的那种。

**(Step 2: The Workflow)**
你不需要手写每一行。按照这个剧本走：

1.  **Define (Lesson 3)**:
    > "Agent, suggest a data structure to represent a library book with title, author, and price."
    (它会给你一个 Dictionary)

2.  **Encapsulate (Lesson 2 & 4)**:
    > "Write a function `add_book` that takes the library list and a new book dict, and adds it. Use type hints."
    (它会给你 `def add_book(...) -> None:`)

3.  **Visualize (Lesson 3)**:
    > "Now create a list with 3 dummy books. Show me how to print them nicely using f-strings."
    (它会给你 Loop + f-string)

**领航员**：
看到没有？
你没有敲几行代码，但你**设计**了整个系统。
这就是 **Intent-Driven Development**。

---

## 3. 前方预警：Python for Pilots - 5 min

**领航员**：
现在，把目光投向前方。
你们即将进入 **Phase 2: Python for Pilots (飞行员阶段)**。

这将是 **Stanford Modern Software Development Course** 预备营的第二个重要台阶。
在下一阶段，我们将接触更危险、也更强大的力量：

*   **Modules (模块)**：我们要给 Python 装上“外挂”。
*   **APIs (接口)**：我们要连接全世界。你的程序将不再是孤岛，我们要去连接 OpenAI、Google 等顶级模型。
*   **Error Handling (异常处理)**：我们要学会应对“空中停车”。

当然，我们的 **Agent** 将全程伴随。
它将不再只是面试官，它将成为你的 **Co-pilot (副驾驶)**，帮你查阅 API 文档，帮你调试那些看不懂的网络错误。

---

## 4. 结语 (Closing) - 2 min

**领航员**：
学徒们，脱下你们的学徒制服吧。
换上飞行服。

检查你们的 IDE，由 "Junior Mode" 切换到 "Pilot Mode"（心理上的切换）。
下一场简报，我们将在**云端**进行。

**End of Phase 1.**
**See you on the runway.**
(Phase 1 结束。跑道见。)
