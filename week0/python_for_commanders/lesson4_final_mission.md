# Lesson 4: The Final Mission (最终任务 - 代号 RAG) 🚀 (口播稿)

> **场景建议**：背景音是火箭发射倒计时的广播声，极其紧张、专注。
> **预计时长**：20 分钟
> **角色**：战区总指挥 (Commander/Instructor)

---

## 0. 任务简报 (Mission Briefing) - 3 min

**总指挥**：
指挥官们，这是 **Stanford Modern Software Development Course Prep** 的最后一次通讯。
你们已经完成了所有的训练模块。
现在，我要把控制权完全移交给你们。

今天的任务代码：**Project Genesis**。
你们要从零开始，构建一个能够读取私有知识库并回答问题的 AI 助手。
这将是你们进入 **Stanford Course Week 1** 之前的投名状。

---

## 1. 任务目标 (Objectives) - 5 min

**总指挥**：
你需要创建一个名为 `simple_rag.py` 的脚本。
它必须包含以下四个模块（对应我们学过的四个阶段）：

1.  **Security Module (安全模块)**：
    必须从 `.env` 文件加载 `OPENAI_API_KEY`（或者假装加载）。使用了 `os.getenv` 和 `python-dotenv`。这是指挥官的底线。
    *(Power of Commander)*

2.  **Knowledge Module (知识模块)**：
    必须使用 `with open` 读取一个本地的 `knowledge.txt` 文件。
    *(Power of Explorer)*

3.  **Core Logic (核心逻辑)**：
    必须有一个函数 `generate_response(question, context)`，负责拼接 Prompt。
    *(Power of Apprentice)*

4.  **Interface (交互模块)**：
    必须有一个 `while` 循环，让用户不断输入问题，直到输入 "exit"。
    *(Power of Pilot)*

---

## 2. 执行策略 (Execution Strategy) - 8 min

**总指挥**：
这是一个复杂的系统。不要试图一行行手写。
**Use your Anti-gravity Agent.** (使用你的智能体)。

我建议的指挥流程：
1.  **Step 1**: 在 IDE 里创建一个空的 `simple_rag.py` 和 `knowledge.txt` (随便写点内容，比如“指挥官最喜欢的颜色是蓝色”)。
2.  **Step 2**: 在 Chat 框里输入这种级别的指令：
    > "I need a Python script that implements a simple RAG system.
    > 1. Load API key from env.
    > 2. Read 'knowledge.txt'.
    > 3. Enter a loop to ask user for input.
    > 4. For now, since I don't have a real API, just PRINT the final prompt that would be sent to the LLM."

**总指挥**：
看着 AI 帮你生成代码。
你的工作是 **Review (审查)**。
*   它用 `with open` 了吗？
*   它用 `os.getenv` 了吗？
*   它有类型提示吗？

如果是，批准执行。如果不是，驳回重写。
这就是 **Stanford Modern Software Development** 的工作方式。

---

## 3. 验收 (Verification) - 2 min

**总指挥**：
当你运行起这个脚本。
屏幕上显示 *"Loading knowledge base..."*
然后提示你 *"Ask me anything:"*
你输入 *"What is his favorite color?"*
程序输出了一段完美的 Prompt，包含了你的 `knowledge.txt` 内容。

那一刻，你就通过了测试。
你正式具备了 **AI Software Engineer** 的雏形。

---

## 4. 尾声 (Epilogue) - 2 min

**总指挥**：
这一周，我们从打印 "Hello World" 开始，走到了构建 "RAG System"。
这不仅仅是代码量的增加，这是思维维度的飞跃。

Apprentice, Pilot, Explorer, Commander.
这四个身份将伴随你的整个职业生涯。

下一节课 (Lesson 5) 我们将进行最后的**授勋仪式**。
我们将封存 Week 0 的档案，并把密钥卡切换到 **Stanford Course** 的模式。

**Mission is a GO. Good luck, Commanders.**
(任务开始。祝好运，指挥官们。)
