# Lesson 1: The Atomic Theory (万物基石 - 变量与类型详解) ⚛️ (口播稿)

> **场景建议**：背景音从早晨的鸟叫声开始，转为轻松的课堂氛围。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场 (Opening) - 2 min

**领航员**：
各位学徒，早上好。
今天，我们要进行长达 25 分钟的深度训练。
请给自己倒一杯咖啡，或者打开你最喜欢的背景音乐。

我们要讨论的话题听起来很枯燥：**Variables (变量)** 和 **Data Types (数据类型)**。
在很多教程里，这只是一页 PPT。
但在 **Stanford Modern Software Development Course**，这是万物的基石。

如果你搞不清“字符串”和“数字”的区别，你的 AI 就会产生幻觉。
如果你不会用 f-strings，你就无法构建 RAG 系统的 Prompt。

不仅要会写，还要**懂**。让我们开始拆解世界的原子。

---

## 1. 变量：贴标签的艺术 (The Variable) - 3 min

**领航员**：
首先，什么是变量？
不要去背计算机科学的定义“内存地址的引用”。太抽象了。

想象你正在搬家。你有一堆箱子。
如果你把所有的东西都乱塞进箱子，也不写名字。到了新家，你想找牙刷，你得把所有箱子拆开。
这就是**没有变量的代码**。

**Code Example**:
```python
print(100 * 0.8)  # 这是什么？谁知道这是打折后的价格还是体重？
```

**领航员**：
变量，就是给箱子**贴标签**。
```python
price = 100
discount_rate = 0.8
final_price = price * discount_rate
print(final_price)
```
现在，傻子都知道你在算什么。
在 Python 里，贴标签超级简单：`标签名 = 内容`。
**Anti-gravity AI 提示**：标签名最好用小写字母，中间用下划线连起来 (snake_case)。这是 Python 的行规。

---

## 2. 字符串：文本的容器 (Strings) - 5 min

**领航员**：
好，现在我们来看看箱子里能装什么。
第一种，也是最常见的一种：**String (字符串)**。

也就是 **Text (文本)**。
在 Python 眼里，只要被**引号**包起来的东西，都是字符串。

**(Step 1: Quotes)**
```python
name = "Leo"   # 双引号，标准
city = 'Beijing' # 单引号，也行
message = "I'm coming" # 如果里面有单引号，外面就得用双引号
```

**领航员**：
在 Stanford 课程里，字符串是绝对的主角。
为什么？因为 **LLM (大语言模型)** 吃的就是 Text。
你的 Prompt 是字符串，AI 回复的也是字符串。

**易错点警告**：
`"100"` 和 `100` 是不一样的。
`"100"` 是一串字符，没有任何数学意义。它就像是写在纸上的“一百”两个字。

---

## 3. 数字：整数与浮点 (Integers & Floats) - 5 min

**领航员**：
第二种，**Numbers (数字)**。
这时候，引号消失了。

Python 把数字分成了两派：
1.  **Integers (整数)**：没有小数点的。
    `level = 10`
    `count = -5`
    通常用来计数 (Counting)。

2.  **Floats (浮点数)**：带小数点的。
    `price = 9.99`
    `pi = 3.14159`
    通常用来测量 (Measuring)。

**领航员**：
为什么要在意这个？
因为精度的陷阱。
在金融计算或者飞船轨迹计算中，浮点数可能会有极微小的误差。
但在 Apprentice 阶段，你只需要知道：**如果不带小数点，就是 int；带了，就是 float。**

试运行一下：`type(10)` vs `type(10.0)`。
在中间的 Editor 里试一下，看右边的 AI 怎么解释。

---

## 4. 布尔值：逻辑的开关 (Booleans) - 4 min

**领航员**：
第三种，最简单，但也最重要：**Boolean (布尔值)**。

它只有两个值：
`True` (真)
`False` (假)

**注意首字母大写！**
它就像是飞船上的一个个**开关**。
`is_engine_on = True`
`has_error = False`

在未来的 Lesson 4 (逻辑控制) 中，所有的 `if/else` 判断，归根结底都是在看这个布尔值是 True 还是 False。

---

## 5. f-string：万能胶水 (The f-string) - 5 min

**领航员**：
最后，我们要讲一个魔法。
我们有了字符串，有了数字，有了开关。
怎么把它们拼成一句话，发给 AI 或者用户？

在旧时代，我们用 `+` 号拼凑：
`"Hello " + name + ", level " + str(level)`
太丑了。而且容易错。

**领航员**：
拥抱 **f-string** 吧。
只要在引号前面加一个小写的 `f`。
你就可以在字符串里挖坑，填入任何变量。

**(Step 2: f-string Magic)**
```python
name = "Leo"
level = 5
score = 98.5

# 看着这个优雅的句子
report = f"Pilot {name} is at Level {level}. Current Score: {score}"
print(report)
```

**领航员**：
这不仅仅是打印。
在 Week 1 构建 RAG 时，你会这样写 Prompt：
```python
user_question = "What is the weather?"
context = "It is sunny."

prompt = f"""
Context: {context}
Question: {user_question}
Answer:
"""
```
看清楚了吗？**f-string 是我们在 Python 里构建 Prompt 的核心工具。**
一定要练熟它。

---

## 6. 总结 (Closing) - 1 min

**领航员**：
呼... 漫长的 25 分钟。
但我们打下了最坚实的地基。

今天如果不理解 `String` 和 `Int` 的区别，明天你的计算器就会报错。
今天如果不掌握 `f-string`，后天你就写不出动态的 Prompt。

下一节课 (Lesson 2)，我们将学习如何把这些操作打包成 **Function (机器)**。

**Analysis complete. Atoms stabilized.**
(分析完毕。原子已稳定。)
