# Lesson 1: The First Record (第一块石碑 - 文件读写) 🗿 (口播稿)

> **场景建议**：背景音有打字机敲击声或凿石头的声音。
> **预计时长**：20 分钟
> **角色**：档案管理员 (Archivist/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**管理员**：
探险家们，欢迎来到挖掘现场。

在之前的课程里，我们的变量（比如 `student_names`）都只活在**内存 (Memory)** 里。
内存就像是个健忘的孩子，电源一拔（程序结束），它就什么都忘了。

今天要教你们的技能，是把数据刻在**硬盘 (Disk)** 上。
硬盘是我们的石碑，哪怕过了一千年（其实是重启后），字依然在那里。

---

## 1. 写入历史 (Writing to Files) - 6 min

**管理员**：
Python 操作文件非常直观，就像你平时用 Word 一样：打开 -> 写入 -> 关闭。

**(Step 1: Hand-write 手写演练)**
新建 `demo_file.py`。

我们先来写一段话。
```python
# 1. 打开文件 (Open)
# "w" 意思是 Write (写入模式)。如果文件不存在，它会新建；如果存在，它会清空重写！
file = open("my_journal.txt", "w", encoding="utf-8")

# 2. 写入内容 (Write)
file.write("Day 1: We found a strange signal.\n")
file.write("Day 2: AI is learning fast.\n")

# 3. 关闭文件 (Close)
# 千万别忘了这一步！否则数据可能没存进去。
file.close()
```

**管理员**：
运行它。然后在你的 Anti-gravity 文件树里找一找，是不是多了一个 `my_journal.txt`？
双击打开它。看，字就在那里。

---

## 2. 读取记忆 (Reading from Files) - 6 min

**管理员**：
现在我们把刚才写的读回来。

**(Step 2: Code it)**
```python
# "r" 意思是 Read (读取模式)
file = open("my_journal.txt", "r", encoding="utf-8")

# 读取全部内容
content = file.read()
print("Here is what we found:")
print(content)

file.close()
```

**管理员**：
这很简单，对吧？
但是这里有个 **Apprentice** 阶段学过的坑。
除了 `read()` 全读出来，我们还可以 `readlines()` 一行行读。这在处理 huge files (大文件) 时很有用。

---

## 3. 追加模式 (Appending) - 3 min

**管理员**：
如果你不想覆盖之前的日记，而是想接着写，该怎么办？
把 `w` 改成 `a` (Append)。

```python
file = open("my_journal.txt", "a", encoding="utf-8")
file.write("Day 3: The signal is gone.\n")
file.close()
```

**管理员**：
记住这三个咒语：`w` (写/覆盖), `r` (读), `a` (追加)。

---

## 4. 课后预告 (Teaser) - 2 min

**管理员**：
今天我们学会了像野人一样在石头上刻字（Plain Text）。
但是，如果我们有一份复杂的飞船配置清单（包含列表、字典、数字），只用文本存起来会很难读。

`config = {"ship_name": "Voyager", "speed": 9000}`
如果只是把它变成字符串存进去，下次读出来就很难变回字典了。

我们需要一种更高级的格式。
下一节课 (Lesson 2)，我们将学习 **JSON**——这是全宇宙通用的数据封印术。

**Journal updated. Saving...**
(日志已更新。保存中...)
