# Week 0: Python 极简入门 (新手友好版)

欢迎来到 Week 0！这份教程是专门为**完全没有编程经验**或者**希望巩固基础**的同学准备的。

我们的目标不是让你成为计算机科学家，而是让你掌握**能够开始 AI 编程**（特别是 Prompt Engineering）所需的最核心概念。

我们会用通俗易懂的比喻来解释每一个概念，确保你不仅“会写”，而且“懂原理”。

## 目录
1. [变量与盒子 (Variables)](#1.-变量与盒子-(Variables))
2. [数据的种类 (Data Types)](#2.-数据的种类-(Data-Types))
3. [玩转文本 (String Manipulation)](#3.-玩转文本-(String-Manipulation))
4. [函数：神奇的机器 (Functions)](#4.-函数：神奇的机器-(Functions))
5. [控制流：做决定与重复 (Control Flow)](#5.-控制流：做决定与重复-(Control-Flow))
6. [模块：借用工具箱 (Modules)](#6.-模块：借用工具箱-(Modules))
7. [正则表达式：超级搜索 (Regex)](#7.-正则表达式：超级搜索-(Regex))
8. [实战：与 AI 对话 (Ollama)](#8.-实战：与-AI-对话-(Ollama))

## 1. 变量与盒子 (Variables)

### 什么是变量？
想象你在搬家。你有很多东西（数据），你需要把它们放进箱子里，并在箱子上写上名字（变量名），这样你以后才能找到它们。

在 Python 中：
- **`=` (等号)**：这不是数学里的“相等”，而是**“赋值”**。意思是：把右边的东西，放进左边的箱子里。
- **变量名**：就是箱子上的标签。你可以随便起名字，最好是有意义的英文（比如 `user_name`）。

```python
# 创建一个叫 user_prompt 的变量，里面装着一句话
user_prompt = "请帮我解决这个问题" 

# print() 是一个“函数”（后面会讲），它的作用是把箱子里的东西拿出来给我们在屏幕上看一看
print(user_prompt)

# 我们可以随时修改箱子里的东西
num_runs = 5  # 现在箱子里是数字 5
print(num_runs)

num_runs = 10 # 现在把 5 拿走，放进去了 10
print(num_runs)
```

## 2. 数据的种类 (Data Types)

箱子里的东西有不同的类型。Python 会自动识别它们。

### 常见类型：
1.  **字符串 (String)**: 就是**文本**。必须用引号 `"` 或 `'` 包裹起来。如果不加引号，Python 会以为它是一个变量名。
2.  **整数 (Integer)**: 就是数学里的整数，比如 `1`, `100`, `-5`。
3.  **列表 (List)**: 就像一个**购物清单**。它是有顺序的，可以放很多东西。用方括号 `[]` 表示。
4.  **字典 (Dictionary)**: 就像一本**字典**。你通过一个“词”（Key）去查找它的“定义”（Value）。用花括号 `{}` 表示。

```python
# --- 列表 (List) ---
# 创建一个列表，里面有三个字符串
messages = ["你好", "世界", "Python"]

# 访问列表里的东西。注意：计算机是从 0 开始数数的！
# [0] 拿的是第一个，[1] 拿的是第二个
print(messages[0]) 

# --- 字典 (Dictionary) ---
# 这是一个典型的 AI 消息格式
# "role" 是键 (Key)，"user" 是值 (Value)
message = {
    "role": "user", 
    "content": "你好，AI助手"
}

# 我们想知道 "content" 对应的内容是什么
print(message["content"])
```

## 3. 玩转文本 (String Manipulation)

在 AI 编程中，我们 90% 的时间都在处理文本（也就是 Prompt）。学会像玩泥巴一样随意捏造文本非常重要。

```python
# 1. f-string (格式化字符串) - 最好用的“填空题”工具
# 在字符串前面加一个 f，然后在 {} 里写变量名，Python 会自动把变量的值填进去
name = "爱丽丝"
greeting = f"你好, {name}! 欢迎来到 Python 世界。"
print(greeting)

# 2. 多行字符串 - 用三个引号 """ 包裹
# 当你的 Prompt 很长，需要换行时，用这个
long_prompt = """
你是一个有用的助手。
请回答我的问题。
"""
print(long_prompt)

# 3. strip() - 清理工
# AI 回复的内容经常会在前后带有一些多余的空格或换行符，strip() 可以把它们去掉
raw_output = "   答案是 42   \n"
clean_output = raw_output.strip()
print(f"清理前: '{raw_output}'")
print(f"清理后: '{clean_output}'")

# 4. replace() - 替换工具
# 把文本里的某个部分换成别的
text = "价格: 1,000 美元"
clean_text = text.replace(",", "")  # 把逗号替换成“空”，也就是删掉逗号
print(clean_text)
```

## 4. 函数：神奇的机器 (Functions)

### 什么是函数？
函数就像一个**微波炉**或者**榨汁机**。
1.  **输入 (参数)**: 你把水果（数据）放进去。
2.  **处理**: 机器运转（执行代码）。
3.  **输出 (返回值)**: 机器吐出果汁（结果）。

### 关键词解释：
- `def`: Define（定义）的缩写。告诉 Python：“我要开始造一台机器了”。
- `return`: 告诉 Python：“机器处理完了，这是吐出来的结果”。
- `-> str`: 这叫**类型提示**。它不影响代码运行，只是像说明书一样告诉人类：“这台机器吐出来的是字符串”。

```python
# 定义一个叫 extract_answer 的机器
# text: str 意思是：请在这个机器里放入字符串类型的原料
def extract_answer(text: str) -> str:
    # 机器内部的操作：把输入的文本进行清理
    cleaned_text = text.strip()
    # 输出结果
    return cleaned_text

# 使用机器（调用函数）
raw_data = "  这就是答案  "
result = extract_answer(raw_data)
print(result)
```

## 5. 控制流：做决定与重复 (Control Flow)

程序如果不只是傻傻地从上往下执行，就需要控制流。

### 1. if/else (如果/否则)
就像生活中的决定：“**如果**下雨，我就带伞；**否则**，我就戴帽子。”

### 2. for 循环
就像体育老师喊口号：“绕操场跑 3 圈！”。当我们需要对列表里的每一个东西都做同样的事情时，就用循环。

```python
# --- if/else 判断 ---
score = 85

if score >= 60:
    print("恭喜，你及格了！") # 注意：这里必须缩进（按 Tab 键），表示这句话属于 if 管辖
else:
    print("很遗憾，不及格。")

# --- for 循环 ---
# range(3) 会生成一个序列：0, 1, 2
print("开始测试...")
for i in range(3):
    print(f"正在运行第 {i + 1} 次测试")

# --- try/except (尝试/捕获错误) ---
# 有些代码可能会报错（比如除以零）。为了不让程序直接崩溃，我们可以“捕获”这个错误。
try:
    result = 10 / 0
except ZeroDivisionError:
    print("出错了：不能除以零！")
```

## 6. 模块：借用工具箱 (Modules)

Python 之所以强大，是因为有成千上万的人写好了现成的代码库（Modules）。你不需要从头造轮子，直接拿来用就行。

- `import`: 意思是“导入”。就像把别人的工具箱搬到你的工作台上。

```python
import os  # 导入操作系统工具箱

# 使用 os 工具箱里的 getcwd 功能，查看当前我们在哪个文件夹
print(os.getcwd())

from collections import Counter # 从 collections 工具箱里，只拿 Counter 这一样工具

# Counter 是一个用来统计数量的神器
votes = ["A", "B", "A", "A", "C"]
counts = Counter(votes)
print(counts.most_common(1))  # 看看谁出现的次数最多
```

## 7. 正则表达式：超级搜索 (Regex)

想象你在读一本书，想找到所有的“电话号码”。电话号码的规律是“3个数字-4个数字-4个数字”。

正则表达式（Regex）就是用来描述这种**“规律”**的语言。它能帮你从一大堆乱七八糟的文本里，精准地抓出你想要的信息。

### 常用符号：
- `\d`: 代表任意一个**数字** (0-9)。
- `+`: 代表前面的东西出现**一次或多次**。
- `\d+`: 连在一起，就代表“一串数字”。

```python
import re # 导入正则工具箱

text = "最终的答案是 Answer: 42。"

# 我们的目标：提取出 42
# 策略：寻找 "Answer:" 后面跟着的数字
# r"..." 表示这是一个正则规则字符串
# (\d+) 是我们想“抓取”的部分
matches = re.findall(r"Answer:\s*(\d+)", text)

print(f"找到了: {matches}")
```

## 8. 实战：与 AI 对话 (Ollama)

这是 Week 1 最激动人心的部分。我们将使用 Python 代码来控制大语言模型（LLM）。

虽然下面的代码需要安装额外的软件才能运行，但你可以先看懂它的逻辑。

```python
# 这是一个伪代码示例，展示了如何“像人类一样”跟 AI 聊天

"""
from ollama import chat # 导入聊天功能

# 调用 chat 函数，就像给 AI 发微信
response = chat(
    model="llama3.1:8b",  # 指定你要聊天的对象（模型名字）
    messages=[
        # system: 给 AI 的人设，告诉它它是谁
        {"role": "system", "content": "你是一个乐于助人的助手。"},  
        # user: 你说的话
        {"role": "user", "content": "1加1等于几？"}  
    ],
    options={"temperature": 0.5}  # 温度：0.5 表示中规中矩。越接近 1 越有创造力（也越容易胡说八道）。
)

# 打印 AI 回复的内容
print(response.message.content)
"""
```

## 总结

恭喜！你已经浏览了 Python 编程中最核心的概念。虽然这只是冰山一角，但对于开始学习 Prompt Engineering 已经足够了。

**下一步建议：**
尝试修改上面的代码块，把 `name` 改成你的名字，或者把数学题改难一点，看看运行结果有什么变化。编程最好的学习方式就是**动手尝试**！
