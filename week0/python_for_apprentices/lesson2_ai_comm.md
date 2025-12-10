# Lesson 2: The Universal Translator (通用翻译机 - 与 AI 沟通) 📡 (口播稿)

> **场景建议**：背景音是静电干扰的嘶嘶声，然后逐渐变清晰的信号声。
> **预计时长**：20 分钟
> **角色**：通讯官 (Comms Officer/Instructor)

---

## 0. 信号校准 (Signal Calibration) - 3 min

**通讯官**：
学徒们，停下手里的工作。
在上一节课，我们手动输入了变量，勉强维持了飞船的生命体征。
但你也发现了，右边那个一直闪烁的 **Right Panel Agent**，它似乎想说什么。

很多新人你会犯一个致命错误：
他们以为 AI 是神。直接把一堆乱七八糟的要求丢给它，然后期待它变魔术。
结果呢？AI 给出的代码是错的，甚至是危险的。

今天，我们在写下一行 Python 代码之前，必须先上一堂**语言课**。
不是 Python 语言，而是 **Prompt Engineering (提示词工程)**。
你要学会如何把你的“意图”翻译成 AI 能听懂的“指令”。

---

## 1. 模糊指令 vs 精确指令 (Vague vs Precise) - 5 min

**通讯官**：
我们来做一个实验。
假如你想让 AI 帮你计算飞船燃料。

**(Step 1: The Bad Prompt)**
在右边的 Chat 框里输入：
> "Calculate fuel." (算一下燃料。)

AI 可能会给你一堆废话，或者问你是哪种燃料，甚至写出一个和你飞船型号完全不匹配的公式。
这就是**垃圾输入，垃圾输出 (GIGO)**。

**(Step 2: The Good Prompt)**
现在，试着用**指挥官**的口吻再说一次：
> "Act as a Python expert. Write a code snippet to calculate remaining flight hours. Given: fuel=98.7, burn_rate=1.2. Print the result using an f-string."

**通讯官**：
看这个结果。
这次它直接给出了完美的 Python 代码。
为什么？因为你提供了三个要素：
1.  **Role (角色)**: Python Expert.
2.  **Context (上下文)**: Given variables.
3.  **Task (任务)**: Write code, print result.

---

## 2. 也是一种代码 (English is Code) - 5 min

**通讯官**：
记住这句话：**English is the new hottest programming language.**
在 Stanford Course 里，你会发现，有时候写好 Prompt 比写好 Python 更难。

我们来练习三种不同的“语调”：

1.  **Explain (解释)**：当你看不懂代码时。
    > "Explain this code like I'm 5 years old."
2.  **Refactor (重构)**：当你觉得代码太烂时。
    > "Make this code more readable and add comments."
3.  **Debug (找茬)**：当代码报错时。
    > "Find the logic error in this calculation."

**(Step 3: Practice)**
试着让 AI 解释一下 Lesson 1 里的那段 f-string 代码。
观察它的回答。

---

## 3. 受控幻觉 (Controlled Hallucination) - 5 min

**通讯官**：
现在，我要告诉你们一个秘密。
**AI 会撒谎。**
或者说，它会一本正经地胡说八道。这叫 **Hallucination (幻觉)**。

试着问它一个不存在的 Python 函数：
> "How do I use the `python.spaceship_module.warp_speed()` function?"

有些模型会诚实地说不知道，但有些模型会给你编造一个看起来完全正确的函数用法。
如果你直接把这个代码复制进你的飞船系统……
**Boom.** 我们就完蛋了。

所以，作为人类指挥官，你的职责不是“复制粘贴”，而是**Review (审查)**。
永远不要信任 AI 的第一次输出。
**Trust, but Verify.** (信任，但要验证。)

---

## 4. 总结 (Debrief) - 2 min

**通讯官**：
这节课虽然没有写 Python，但可能是救命的一课。
你们手中的 AI Agent 是目前全宇宙最强的副驾驶。
但它只是副驾驶。
**方向盘在你手里。**

下一节课 (Lesson 3)，我们将进行一次实弹演习。
我会让这位 AI 副驾驶帮我们写一个引擎控制函数。
但我会**故意**诱导它写出一个有 Bug 的版本。
到时候，就看你们能不能像一个真正的 Auditor 一样，把它揪出来了。

**Channel clear. End transmission.**
(频道清晰。通话结束。)
