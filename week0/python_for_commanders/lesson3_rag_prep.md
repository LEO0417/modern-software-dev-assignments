# Lesson 3: The War Game (兵棋推演 - RAG 原理预演) ♟️ (口播稿)

> **场景建议**：背景音是全息地图展开的嗡嗡声，战略指挥的凝重感。
> **预计时长**：20 分钟
> **角色**：战区总指挥 (Commander/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**总指挥**：
指挥官们，这节课是理论与实战的结合。
我们即将解码 **Stanford Modern Software Development Course** Week 1 的终极武器——**RAG (Retrieval-Augmented Generation)**。
这个词听起来很吓人（检索增强生成）。

但让我们用人话翻译一下：
现在的 AI (大模型) 就像一个博学但不了解你公司内情的博士。
如果你问它：“我们公司明天的早餐是什么？”它不知道。
RAG 就是：先去公司食堂门口拍张菜单（检索），然后把照片和问题一起给博士看（增强）。博士就能回答了（生成）。

这就是 RAG：**找资料 + 问 AI**。

---

## 1. 拆解组件 (Deconstruction) - 6 min

**总指挥**：
在 Python 代码里，这个过程是怎么实现的？
我们要用到你们之前学过的所有知识。

**(Step 1: The Corpus 语料库)**
由于 Stanford 课程中我们会用到大量 PDF，但本质上，它就是一个**字符串列表**。

Create `rag_sim.py`:
```python
# 1. 语料库 (Corpus) - Explorer 技能
corpus = [
    "Machine learning is a field of inquiry devoted to understanding and building methods that 'learn'...",
    "Deep learning is a class of machine learning algorithms that...",
    "The commander loves coffee."
]
```

**(Step 2: The Retrieval 检索)**
我们要找“谁喜欢咖啡”。
我们需要一个函数，在列表里搜关键词。
```python
# 2. 检索器 (Retriever) - Pilot 技能
def retrieve(query, documents):
    results = []
    for doc in documents:
        if query.lower() in doc.lower(): # 简单的关键词匹配
            results.append(doc)
    return results

# 测试一下
query = "coffee"
context = retrieve(query, corpus)
print(f"Found context: {context}")
```

---

## 2. 增强与生成 (Augment & Generate) - 6 min

**总指挥**：
资料找到了。下一步是组装给 AI 的命令。这叫 **Prompt Engineering (提示词工程)**。
这是 DeepMind 和 OpenAI 工程师每天都在做的事情，也是你们在 Stanford 课程中要反复练习的技能。

**(Step 3: The Prompt)**
```python
# 3. 增强 (Augment) - Apprentice 技能
def make_prompt(user_question, context_list):
    # 把找到的资料拼成一段话
    context_str = "\n".join(context_list)
    
    prompt = f"""
    You are a helpful assistant.
    Use the following context to answer the question.
    
    Context:
    {context_str}
    
    Question: {user_question}
    Answer:
    """
    return prompt

final_prompt = make_prompt("What does the commander like?", context)
print(final_prompt)
```

**总指挥**：
仔细看打印出来的 `final_prompt`。
它包含了资料（Commander loves coffee）和问题（What does he like）。
如果你把这段话发给 Anti-gravity 副驾驶，它百分之百能答对。

这就是 Week 1 `rag.py` 里的核心魔法。
那个文件虽然有几百行，但骨架就是这三部分：**Corpus (列表), Retrieve (搜), Prompt (拼)**。

---

## 3. AI 互动：模拟运行 (AI Interaction) - 3 min

**总指挥**：
由于我们现在还没有连上真正的 OpenAI API（那是 Lesson 4 的事）。
我们可以让 Anti-gravity 扮演那个 LLM。

**(Step 4: AI Simulation)**
把生成的 `final_prompt` 复制下来。
粘贴到 Chat 框里，直接发给 Anti-gravity。

它应该会回答：*"The commander loves coffee."*
看，你自己动手构建了一个完整的 RAG 链路。

---

## 4. 课后预告 (Teaser) - 2 min

**总指挥**：
原理已经通了。
现在，我们拥有了所有的碎片：
*   读文件 (Explorer)
*   写函数 (Apprentice)
*   调 API (Pilot)
*   环境变量 (Commander)
*   RAG 原理 (Commander)

下一节课 (Lesson 4)，是你们的**Sranford Course 资格考试**。
我不会再带你们手写每一行代码。
我将发布任务书。
你将作为总指挥，统筹你的 AI Agent，去完成一个真正的、能跑通的 RAG 系统。

**Simulation over. Prepare for deployment.**
(推演结束。准备部署。)
