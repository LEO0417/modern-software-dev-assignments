# Lesson 1: Upgrading the Ship (改装飞船 - 模块与Pip) 🔧 (口播稿)

> **场景建议**：背景音有机械安装、螺丝刀转动的声音。
> **预计时长**：20 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**领航员**：
飞行员们，欢迎来到改装车间。

以前在 Apprentice 阶段，我们用的都是 Python **自带** 的功能（Built-ins），比如 `print`, `len`, `list`。
这就像是你买了一辆素车（Stock Car），只有最基本的方向盘和油门。

但如果你想去越野（爬虫），或者想去赛道（跑 AI 模型），光靠原厂配置是不够的。
今天，我们要学习两个关键技能：
1.  **Import (导入)**：把出厂时放在后备箱里的工具拿出来用。
2.  **Pip Install (安装)**：去商店买更牛逼的零件装上去。

---

## 1. 自带的武库：Standard Library (标准库) - 5 min

**领航员**：
Python 被称为 "Batteries Included" (自带电池) 的语言。
这意味着它预装了很多好东西，只是默认没开启。

**(Step 1: Hand-write 手写演练)**
新建 `demo_modules.py`。

假设我们要搞随机抽奖。你自己写随机算法很难。
但是 Python 自带了一个 `random` 模块。

```python
# 呼叫 random 模块
import random

# 使用它的功能
luck = random.randint(1, 100)
print(f"Your luck level: {luck}")
```

**领航员**：
再比如，我们要跟操作系统打交道（比如获取当前路径）。
```python
import os
print(os.getcwd())
```

这就是 **Import**。你只需要喊一声，工具就来了。

---

## 2. 外部的海洋：PyPI & Pip - 7 min

**领航员**：
但是，自带的工具毕竟有限。
真正的宝藏在外面——**PyPI (Python Package Index)**。
那里有全世界开发者上传的几十万个库。

要获取它们，我们需要一个神奇的咒语：**pip**。

**(Step 2: Terminal Operation 终端操作)**
打开你的 Anti-gravity IDE 的终端 (Terminal)。
我们要安装一个在这个星球上最流行的第三方库：`requests`（它能让你像浏览器一样访问网站）。

输入命令：
```sh
pip install requests
```
看到那个进度条了吗？那就是你的飞船在下载新装备。

**(Step 3: Code it)**
装好之后，回到代码里：

```python
import requests

# 访问百度
response = requests.get("https://www.baidu.com")

print(f"Status Code: {response.status_code}")
# 如果是 200，说明访问成功
```

**领航员**：
就这么简单。
如果没有 `requests`，你要写几百行代码来处理网络连接。现在只需要一行。
这就是 Python 生态系统的威力。

---

## 3. AI 互动：寻找合适的包 (AI Interaction) - 5 min

**领航员**：
问题来了：我怎么知道我想干的事有没有现成的包？
这时候，问你的 Anti-gravity AI。

**(Step 4: AI Inquiry)**
在 Chat 框里问：
> "I want to read data from an Excel file using Python. Which library should I use and how to install it?"
> (我想用 Python 读 Excel 文件，该用哪个库？怎么装？)

**AI 回答预演**：
AI 会告诉你：使用 `pandas` 或者 `openpyxl`。
命令是 `pip install pandas`。
并且它通常会直接给你一段示例代码。

**领航员**：
这就是飞行员的智慧。
遇到难题，先不要自己造轮子。先问 AI：“有没有人已经造好了？”
通常答案是肯定的。

---

## 4. 课后预告 (Teaser) - 2 min

**领航员**：
今天我们给飞船装上了 `requests` 这个强大的通讯模块。
你可以访问网页了。

但是，访问 `www.baidu.com` 只是最无聊的玩法。
我们要连接的是那些**能给我们数据**的服务器。
也就是 **API**。

下一节课 (Lesson 2)，我们将学习如何用 `requests` 库，去跟真正的互联网服务（比如天气预报、GitHub）对话。
我们要开始从互联网的大海里捕鱼了。

**Upgrade complete. Systems online.**
(改装完成。系统上线。)
