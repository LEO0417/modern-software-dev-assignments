# Lesson 2: Talking to the World (连接世界 - API操作) 🌐 (口播稿)

> **场景建议**：背景音有数据流传输的电子音效。
> **预计时长**：20 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**领航员**：
各就各位。
上一节课，我们安装了 `requests` 库。这相当于给我们的飞船装上了无线电收发器。
我们可以 Ping 通百度了。

但是，作为一个现代的程序员，我们不想要网页上的广告和图片，我们只想要**干净的数据**。
比如，现在的气温是多少？比特币的价格是多少？
为了获取这些纯净的数据，我们需要连接到一种特殊的端口——**API (Application Programming Interface)**。

简单说，网页是给人看的，API 是给程序看的。
今天，我们就来实战一次“外星联络”。

---

## 1. 核心概念：Request & JSON - 5 min

**领航员**：
当你向 API 发起请求时，对方通常会回给你一个 **JSON** 格式的数据。
别被这名字吓到。
还记得我们在 Phase 1 学的 **Dictionary (字典)** 吗？
JSON 长得跟 Python 的字典**一模一样**。

**(Step 1: Hand-write 手写实战)**
新建 `demo_api.py`。
我们要用一个免费的测试 API（JSONPlaceholder）来获取假的用户数据。

```python
import requests

# 1. 拨通电话 (Send Request)
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

# 2. 检查通没通 (Check Status)
if response.status_code == 200:
    print("Connection Successful!")
    
    # 3. 翻译数据 (Parse JSON)
    # 这一步把那串像乱码一样的文本，变成了你可以操作的 Python 字典
    user_data = response.json()
    
    # 4. 提取信息
    print(f"User Name: {user_data['name']}")
    print(f"User Email: {user_data['email']}")
else:
    print("Connection Failed.")
```

**领航员**：
运行它。
看，你不需要解析 HTML，你不需要找所有的 `div` 标签。
你直接拿到这把**钥匙** (`['name']`)，就拿到了**宝藏**。
这就是 API 的优雅之处。

---

## 2. 真实世界的挑战 (Real World Scenario) - 7 min

**领航员**：
但是，真实世界的 API 往往比这个复杂。
它们可能会嵌套很多层。比如 `user['address']['geo']['lat']`。

这时候，你的眼睛可能会花。
但你的 Anti-gravity 副驾驶不会。

**(Step 2: AI Interaction)**
我们可以让 AI 帮我们写解析代码。

选中刚才 `response.json()` 返回的那一大坨数据（你可以在终端里打印出来，或者假装有一段复杂的 JSON）。
贴到 Chat 里，跟 AI 说：
> "Here is the JSON response from an API. I want to extract the user's city and zip code. Write the parsing code for me."
> (这是 API 返回的 JSON。我要提取城市和邮编。帮我写解析代码。)

**AI 预期动作**：
它会精准地写出：
```python
city = user_data['address']['city']
zipcode = user_data['address']['zipcode']
```
**领航员**：
在 Week 1 的课程里，我们要处理 Open Source 模型返回的复杂数据。那个层级非常深。
学会**让 AI 帮你读 JSON**，是 Pilot 的必备生存技能。

---

## 3. 课后预告 (Teaser) - 2 min

**领航员**：
现在你能从网上抓数据了。
这很酷。
但是，网络不是永远可靠的。
如果网断了？如果 API 服务器挂了？如果对方改了密码？

在目前的脚本里，一旦出错，你的程序就会直接**报错退出 (Crash)**。
如果是除你的一台电脑，那无所谓。
但如果是控制一艘真正的飞船，或者运营一个商业服务，直接 Crash 是不可接受的。

下一节课 (Lesson 3)，我们要学习如何**防御性驾驶**。
我们要学习 `try/except`，学会处理异常。
我们要让我们的飞船即使在引擎着火的情况下，也能安全滑翔着陆。

**Communications secured. Stand by.**
(通讯已建立。待命。)
