# Lesson 4: The Archaeologist (数据考古 - 日志分析) 🔦 (口播稿)

> **场景建议**：背景音是风吹过洞穴的声音，探照灯打开的音效。
> **预计时长**：20 分钟
> **角色**：档案管理员 (Archivist/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**管理员**：
探险家们，拿起你们的铲子。

在前几课，我们学会了 `open`, `json`, `with`。
今天，我们要面对一座真正的“数据矿山”。

假设你是 Google 的运维工程师。
昨晚服务器崩了一次。老板甩给你一个巨大的 `server.log` 文件，问你：“到底哪里出错了？给我一个报告。”
文件里有几千行这样的东西：
`[2023-01-01 10:00:01] INFO: System normal`
`[2023-01-01 10:00:05] ERROR: Connection lost`

你不可能一行行去看。
我们要写一个 Python 脚本，替我们去读、去找、去统计。

---

## 1. 制造样本 (Generate Data) - 5 min

**管理员**：
首先，我们需要这座矿山。
既然我们没有真的服务器，我们就造一个假的。

**(Step 1: Setup)**
新建 `log_analyzer.py`。
先写一段代码生成一个假日志：

```python
# 造假日志
log_content = """
[INFO] User Login
[INFO] User Logout
[ERROR] Database timeout
[INFO] User Login
[ERROR] File not found
[WARNING] Disk space low
"""
# 把它存起来
with open("server.log", "w") as f:
    f.write(log_content)
```
运行一下，确保 `server.log` 已经生成了。

---

## 2. 挖掘分析 (Mining Logic) - 8 min

**管理员**：
现在，任务是：统计有多少个 ERROR，并把所有的报错信息打印出来。

**(Step 2: Analysis Script)**
在同一个文件里，接着写：

```python
print("Starting Analysis...")

error_count = 0

# 打开矿山
with open("server.log", "r") as f:
    # 逐行扫描
    for line in f:
        # 去掉行尾的换行符
        line = line.strip()
        
        # 核心判断逻辑
        if "[ERROR]" in line:
            error_count += 1
            print(f"Found Issue: {line}")

print(f"Analysis Complete. Total Errors: {error_count}")
```

**管理员**：
运行它。
看，程序在一瞬间就找到了所有的 ERROR。
这就是 **Log Analysis** 的雏形。
如果在 Week 1 你遇到 RAG 系统回答错误，你也是这样去日志里搜 `[RAG ERROR]` 的。

---

## 3. AI 互动：高级过滤 (Advanced Filtering) - 5 min

**管理员**：
但是，老板的需求总是变来变去。
老板现在想问：“把所有的 INFO 过滤掉，只把 WARNING 和 ERROR 存到一个新文件 `report.txt` 里。”

这逻辑稍微复杂点（又要读，又要写）。
交给 Anti-gravity AI。

**(Step 3: AI Command)**
选中刚才的分析代码，告诉 AI：
> "Modify this script. Instead of printing, write all lines containing `[ERROR]` or `[WARNING]` to a new file called `report.txt`."
> (修改脚本。把所有包含 ERROR 或 WARNING 的行写入 report.txt。)

**AI 动作**：
它会给你生成一个同时用了读写模式的代码，可能会用到 `if "[ERROR]" in line or "[WARNING]" in line:`。

**管理员**：
这就是探险家的工作方式：**明确目标 -> 编写/生成脚本 -> 提取价值**。

---

## 4. 课后预告 (Teaser) - 2 min

**管理员**：
恭喜你，你已经从那些枯燥的文本里提取出了情报。
这就是 **Python for Explorers** 的全部精髓。

现在，你们已经掌握了：
1.  **Apprentices**: 基础语法 (Functions, Lists)。
2.  **Pilots**: 自动化与网络 (Requests, Exceptions)。
3.  **Explorers**: 数据持久化与分析 (Files, JSON)。

你们的拼图只差最后一块了。
那就是 **Strategy (战略)**。
如何处理像山一样大的数据？如何根据环境变量切换配置？
这不仅仅是写代码，这是**指挥**。

下一阶段，我们将迎来终局：**Python for Commanders (指挥官)**。
我们将直接预演 Week 1 的核心挑战。

**Analysis saved. Shutting down.**
(分析已保存。关机。)
