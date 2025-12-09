# Lesson 3: Brace for Impact (防冲击姿态 - 异常处理) 🛡️ (口播稿)

> **场景建议**：背景音有警报声，然后被消除，转为平稳。
> **预计时长**：15 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**领航员**：
注意！(Alert sound)
在上一节课我们连接了 API。代码跑得很顺。
但是，假设刚才那个网站倒闭了，或者你的 Wi-Fi 断了。
你的 `requests.get` 会发生什么？

它会抛出一个巨大的、红色的错误信息（Traceback），然后你的程序会当场死亡。
如果这是你给老板写的自动化日报脚本，老板早上 8 点没收到邮件，你 9 点就会被叫进办公室。

作为 Pilot，我们的原则是：**Always expect the unexpected.** (永远预料到意外)。
今天，我们要给飞船装上**安全气囊**——**Try / Except**。

---

## 1. 捕捉异常 (Catching the Crash) - 5 min

**领航员**：
在 Python 里，我们要把“可能出错”的代码，包在一个保护罩里。

**(Step 1: Hand-write 手写实战)**
新建 `demo_safety.py`。

我们先写一个一定会报错的代码（比如除以零）：
```python
# 这是一个自杀式代码
result = 10 / 0
print("I will never run.")
```

**领航员**：
运行它。你会看到 ZeroDivisionError。后面的 `print` 根本没机会执行。
现在，加上护盾：

```python
try:
    # 尝试做危险动作
    result = 10 / 0
    print(f"Result is {result}")
except ZeroDivisionError:
    # 如果出了这个错，执行这里
    print("Oops! You cannot divide by zero.")
    # 可以设置一个默认值，或者记录日志
    result = 0

print("I am still alive!")
```

**领航员**：
再次运行。就算出错了，程序也**活着**走到了最后一行。这就叫“优雅地处理错误”。

---

## 2. AI 互动：自动加固 (AI Interaction) - 5 min

**领航员**：
在实际开发中，你可能不知道那些复杂的 API 调用会出什么错（超时？404？解析错误？）。
这时候，Anti-gravity AI 经验比你丰富。

**(Step 2: AI Refactor)**
还是拿上一节课的 API 代码为例。
把那段裸奔的代码贴进去：
```python
import requests
resp = requests.get("https://fake-url.com/data")
data = resp.json()
```

选中它，命令 AI：
> "Wrap this code in a try/except block to handle network errors and JSON parsing errors."
> (用 try/except 包裹这段代码，处理网络和解析错误。)

**AI 预期生成的代码**：
```python
try:
    resp = requests.get("https://fake-url.com/data")
    resp.raise_for_status() # 检查 404/500
    data = resp.json()
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except ValueError:
    print("Invalid JSON received")
except Exception as e:
    print(f"Unknown error: {e}")
```

**领航员**：
看，AI 帮你考虑到了多种可能。
如果你在作业里用了这样的代码结构，我在 Code Review 时会给你打满分。哪怕你逻辑写错了，至少你的代码是**安全**的。

---

## 3. 课后预告 (Teaser) - 2 min

**领航员**：
现在，你们的飞船已经改装完毕。
装了模块（Pip），连了网络（API），还有了安全气囊（Try/Except）。

是时候进行一次真正的**自动化飞行**了。
下一节课 (Lesson 4)，我们将把这些零件全部组装起来。
我们将写一个完整的脚本：自动抓取某个服务的状态，如果异常就报警。
这将是你们作为 Pilot 的最后一次考核。

**Safety protocols engaged. Resume course.**
(安全协议已启用。恢复航线。)
