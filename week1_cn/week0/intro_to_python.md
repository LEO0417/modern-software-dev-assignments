# Week 0: Python 基础入门 (针对 Week 1)

欢迎来到 Week 0！本笔记本旨在为你提供完成 Week 1 作业所需的 Python 基础知识。我们不会涵盖 Python 的所有内容，而是专注于你在提示工程（Prompt Engineering）代码中会遇到的核心概念。

## 目录
1. [变量与类型 (Variables & Types)](#1.-变量与类型-(Variables-&-Types))
2. [字符串操作 (String Manipulation)](#2.-字符串操作-(String-Manipulation))
3. [函数与类型提示 (Functions & Type Hints)](#3.-函数与类型提示-(Functions-&-Type-Hints))
4. [控制流 (Control Flow)](#4.-控制流-(Control-Flow))
5. [模块导入 (Modules)](#5.-模块导入-(Modules))
6. [正则表达式 (Regular Expressions)](#6.-正则表达式-(Regular-Expressions))
7. [Ollama 库的使用](#7.-Ollama-库的使用)

## 1. 变量与类型 (Variables & Types)

在 Python 中，你不需要声明变量的类型，直接赋值即可。

```python
# 字符串 (String)
user_prompt = "Solve this problem" 
print(user_prompt)

# 整数 (Integer)
num_runs = 5
print(num_runs)

# 列表 (List) - 有序的集合
messages = ["Hello", "World", "Python"]
print(messages[0])  # 索引从 0 开始

# 字典 (Dictionary) - 键值对集合
# 在调用 LLM API 时，我们经常用字典来构建消息
message = {"role": "user", "content": "Hello AI"}
print(message["content"])
```

## 2. 字符串操作 (String Manipulation)

处理 LLM 的输入和输出时，字符串操作至关重要。

```python
# f-string (格式化字符串)
# 这是将变量嵌入字符串的最常用方法
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)

# 多行字符串 (使用三个引号)
# 用于定义长提示词 (Prompts)
long_prompt = """
You are a helpful assistant.
Please answer the question.
"""
print(long_prompt)

# strip() - 去除首尾空白字符 (空格、换行符)
# LLM 的输出通常包含多余的换行符，需要清理
raw_output = "   Answer: 42   \n"
clean_output = raw_output.strip()
print(f"Raw: '{raw_output}'")
print(f"Clean: '{clean_output}'")

# replace() - 替换子字符串
text = "Answer: 1,000"
clean_text = text.replace(",", "")  # 去除逗号
print(clean_text)
```

## 3. 函数与类型提示 (Functions & Type Hints)

函数用于封装可重用的代码块。类型提示 (Type Hints) 帮助我们理解函数的输入和输出类型。

```python
# 定义一个函数
# text: str 表示参数 text 应该是一个字符串
# -> str 表示函数返回一个字符串
def extract_answer(text: str) -> str:
    return text.strip()

result = extract_answer("  Some answer  ")
print(result)
```

## 4. 控制流 (Control Flow)

控制程序的执行顺序。

```python
# for 循环
# 常用于多次运行测试 (如 K-shot prompting)
for i in range(3):
    print(f"Running test {i + 1}")

# if/else 条件判断
score = 85
if score >= 60:
    print("Pass")
else:
    print("Fail")

# try/except 异常处理
# 防止程序因错误而崩溃
try:
    # 尝试执行可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 如果出错，执行这里的代码
    print("Cannot divide by zero!")
```

## 5. 模块导入 (Modules)

Python 有丰富的标准库和第三方库。

```python
import os  # 导入整个模块
from collections import Counter  # 从模块中导入特定的类或函数

# 使用 os 模块获取当前工作目录
print(os.getcwd())

# 使用 Counter 统计元素出现次数 (在 Self-Consistency 中很有用)
votes = ["A", "B", "A", "A", "C"]
counts = Counter(votes)
print(counts.most_common(1))  # 获取出现次数最多的元素
```

## 6. 正则表达式 (Regular Expressions)

正则表达式 (Regex) 是从文本中提取信息的强大工具。在 Week 1 中，我们用它从 LLM 的回复中提取答案。

常用符号：
- `\d`: 数字
- `+`: 一个或多个
- `.`: 任意字符
- `*`: 零个或多个

```python
import re

text = "The final answer is Answer: 42."

# re.findall: 查找所有匹配项
# r"..." 表示原始字符串，常用于正则
# Answer:\s*(\d+) 意思匹配 "Answer:" 后跟任意空格，然后捕获数字
matches = re.findall(r"Answer:\s*(\d+)", text)
print(f"Found matches: {matches}")

# re.search: 查找第一个匹配项
match = re.search(r"\d+", text)
if match:
    print(f"Found number: {match.group(0)}")
```

## 7. Ollama 库的使用

这是我们在 Week 1 中与 LLM 交互的核心代码模式。

```python
# 伪代码示例 (需要安装 ollama 并运行服务才能真正执行)
"""
from ollama import chat

response = chat(
    model="llama3.1:8b",  # 指定模型
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # 系统提示词
        {"role": "user", "content": "What is 2+2?"}  # 用户提示词
    ],
    options={"temperature": 0.5}  # 设置随机性 (0-1)
)

print(response.message.content)
"""
```
