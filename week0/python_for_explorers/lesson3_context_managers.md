# Lesson 3: The Safety Lock (安全锁 - Context Managers) 🔐 (口播稿)

> **场景建议**：背景音是气密门自动开启和关闭的声音。
> **预计时长**：15 分钟
> **角色**：档案管理员 (Archivist/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**管理员**：
探险家们，欢迎回到控制室。

在之前的课程里，我们打开文件用的都是“手动模式”：
1. `f = open(...)` (开门)
2. `f.write(...)` (进去办事)
3. `f.close()` (关门)

这有个致命的风险。如果在“办事”的时候，程序崩溃了（报错），第三步“关门”就不会执行。
文件就会保持打开状态，可能会导致数据丢失，或者别的程序打不开它。
这叫 **Resource Leak (资源泄露)**。

在 Python for Explorers 阶段，我们严禁使用裸露的 `open()`。
我们要使用一种自动化的安全锁——**With Statement (上下文管理器)**。

---

## 1. 自动关门 (Automatic Closing) - 6 min

**管理员**：
让我们对比一下。

**(Step 1: Old Way - 危险)**
```python
# 别写这个，看看就行
f = open("log.txt", "w")
f.write("System Start")
# 假设这里报错了... crash!
f.close() # 这行永远轮不到执行
```

**(Step 2: New Way - 安全)**
新建 `demo_with.py`。
```python
# "with" 意思是：当我在这个缩进块里的时候...
with open("log.txt", "w") as f:
    f.write("System Start... ")
    print("Writing data...")
    # 就算这里报错了，Python 也会在奔溃前自动把文件关好
    
print("File is closed now.")
```

**管理员**：
`with` 语句就像是一个负责任的管家。
只要你走出了那个缩进的代码块（无论是因为运行完了，还是因为报错跳出了），管家都会帮你执行 `f.close()`。
你再也不用担心忘记关门了。

---

## 2. 深入理解 (Deep Dive) - 4 min

**管理员**：
不仅仅是文件。
在 Week 1 和 Week 2 里，你们会看到很多类似的代码：
*   `with database.connect() as db:` (自动断开数据库连接)
*   `with ThreadPool() as pool:` (自动清理线程)

这是一种 **Pattern (设计模式)**。
它代表了“借用 -> 使用 -> 归还”的整个生命周期。

---

## 3. AI 互动：代码升级 (AI Interaction) - 4 min

**管理员**：
既然这是最佳实践，那我们是不是该把以前的老代码都修一遍？
当然。

**(Step 3: AI Refactor)**
把你 Lesson 1 里写的那个老式文件读取代码，贴给 Anti-gravity。
Command:
> "Refactor this code to use the 'with open' statement for better safety."
> (把这段代码重构成用 'with open' 语句。)

**AI 预期**：
它会立刻把三行变成两行，并加上缩进。
这就是 **Modern Python** 的样子。

---

## 4. 课后预告 (Teaser) - 2 min

**管理员**：
现在的你，已经能安全、规范地读写文件了。
但是，我们目前读的都是几十个字的小文件。

如果给你一个 100MB 的服务器日志，里面有 50 万行报错信息。
你要怎么找出里面所有的 "Error: 404"？
肉眼看是会瞎的。

下一节课 (Lesson 4)，我们将进行 Explorer 阶段的**终极任务**。
我们将写一个脚本，自动分析一份巨大的日志文件，生成一份统计报告。
这才是真正的“数据挖掘”。

**Lock engaged. System secure.**
(安全锁已启用。系统安全。)
