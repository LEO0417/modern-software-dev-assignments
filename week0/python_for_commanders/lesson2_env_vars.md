# Lesson 2: Top Secret (绝密档案 - 环境变量) 🔐 (口播稿)

> **场景建议**：背景音是保险箱转盘的声音，加密通讯的杂音。
> **预计时长**：15 分钟
> **角色**：战区总指挥 (Commander/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**总指挥**：
指挥官们，这节课涉及到最高安全等级。

在 Week 1，你们所有人都会用到 OpenAI 或者 Gemini 的 API Key。
这串字符直接连通着你的信用卡。
如果这串字符泄露了，几秒钟内黑客就能刷爆你的额度。

在 Infants 阶段，可能有人教过你直接把 Key 写在代码里：
`api_key = "sk-123456..."`
**这是绝对禁止的**。
因为代码是要分享协作的（Git），而密钥是私人的。

今天，我们要学习把秘密藏在一种特殊的保险箱里——**.env (Environment Variables)**。

---

## 1. 制造保险箱 (.env) - 5 min

**总指挥**：
这个保险箱其实就是个普通文件，但它有个特殊的名字。

**(Step 1: Create File)**
在你的项目根目录下，新建一个文件，名字就叫 `.env`（注意前面有个点，没有文件名）。
在里面写上：
```text
MY_SECRET_KEY=TopSecret123
DB_PASSWORD=Hunter2
```
这个文件，永远不要提交到 Git 上（我们要把它加进 `.gitignore`，这个以后细说）。现在你只要知道，它是仅供你本地电脑查看的。

---

## 2. 读取秘密 (os.getenv) - 6 min

**总指挥**：
现在，我们的 Python 代码怎么拿到这个秘密呢？
我们需要一把钥匙：`python-dotenv` 库。

**(Step 2: Install)**
打开终端：`pip install python-dotenv`

**(Step 3: Code it)**
新建 `security_check.py`：

```python
import os
from dotenv import load_dotenv

# 1. 加载保险箱
# 这行代码会去读 .env 文件，把里面的秘密放到系统的环境变量里
load_dotenv()

# 2. 取出秘密
# 注意：我们这里没有写明文密码，只有一个代号 "MY_SECRET_KEY"
secret = os.getenv("MY_SECRET_KEY")

if secret == "TopSecret123":
    print("Access Granted. Welcome Commander.")
else:
    print("Access Denied.")
```

**总指挥**：
这看起来多此一举？
不。这样做的好处是，你的代码文件 (`security_check.py`) 是干净的。如果不小心把这个代码发给了别人，里面只有一行 `os.getenv(...)`，真正的值还在你自己的电脑里。

这就是 **Security Best Practice (安全最佳实践)**。

---

## 3. AI 互动：安全检查 (AI Interaction) - 3 min

**总指挥**：
如果你拿到一段别人的代码，或者自己以前写的代码，里面有硬编码的密码。
请立刻让 AI 帮你清理。

**(Step 4: AI Command)**
把这行危险代码贴给 Anti-gravity：
`conn = connect_db(password="123456")`

Command:
> "Refactor this to use environment variables for the password."
> (重构这段代码，使用环境变量存密码。)

AI 会自动帮你改成 `os.getenv` 的形式。

---

## 4. 课后预告 (Teaser) - 2 min

**总指挥**：
安全协议已建立。
现在你们已经具备了操作 Week 1 复杂系统的资格。

Week 1 的核心是一个叫做 **RAG** 的系统。
它听起来很玄乎，但拆解开来，无非就是：读取文件 -> 搜索关键词 -> 喂给 AI。
你们已经掌握了所有这些零件。

下一节课 (Lesson 3)，我们将进行一次 **War Game (兵棋推演)**。
我们将完全解构 Week 1 的 `rag.py` 逻辑。
当你第一天打开那个作业时，你会发现——“哈，这不就是我之前写过的东西吗？”

**Encryption active. Dismissed.**
(加密已激活。解散。)
