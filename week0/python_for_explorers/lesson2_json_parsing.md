# Lesson 2: The Universal Format (通用语言 - JSON解析) 📦 (口播稿)

> **场景建议**：背景音是数据解压、加载的科技音效。
> **预计时长**：20 分钟
> **角色**：档案管理员 (Archivist/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**管理员**：
欢迎回来，Explorers。

上一节课我们学会了读写 `.txt` 文件。这对于写日记够了。
但是，如果你想保存这种数据呢？

```python
settings = {
    "theme": "dark",
    "fontSize": 14,
    "recentFiles": ["demo1.py", "demo2.py"]
}
```

你要是把它强行转成字符串写进 txt，下次读出来就是一串死文本，你没法直接访问 `settings['theme']`。
我们需要把这个 Python 字典，“冷冻”起来存到硬盘，下次用的时候再“解冻”变回字典。
这个过程叫 **Serialization (序列化)**。
而最常用的冷冻格式，就是 **JSON**。

---

## 1. 冷冻：Dump (Save) - 6 min

**管理员**：
Python 有个专门处理这个的模块，叫 `json`。

**(Step 1: Hand-write 实战)**
新建 `demo_json.py`。

```python
import json

# 这是我们要存的数据
data = {
    "pilot_name": "Leo",
    "level": 3,
    "inventory": ["sword", "shield"]
}

# 1. 打开一个 .json 文件 (写入模式)
# 上下文管理器 (with) 我们下节课细讲，但今天先照着写
file = open("save_game.json", "w")

# 2. Dump (倾倒/保存)
json.dump(data, file, indent=4)
# indent=4 是为了让保存的文件好看，有缩进

file.close()
```

**管理员**：
运行它。打开生成的 `save_game.json`。
看！它被完美地保存了下来，格式非常整齐。

---

## 2. 解冻：Load (Open) - 6 min

**管理员**：
现在假设你关机了，第二天重开游戏。我们要加载存档。

**(Step 2: Code it)**
```python
import json

# 1. 打开文件 (读取模式)
file = open("save_game.json", "r")

# 2. Load (加载)
# 这一步，它把文件里的文本，神奇地变回了 Python 字典
loaded_data = json.load(file)

file.close()

# 验证一下
print(f"Welcome back, {loaded_data['pilot_name']}!")
print(f"Your inventory: {loaded_data['inventory']}")
```

**管理员**：
通过 `json.dump` 和 `json.load`，你就实现了数据的永生。
在 Week 1 的开发中，几乎所有的配置文件、API 数据缓存，都是这么处理的。

---

## 3. AI 互动：修复损坏的 JSON (AI Interaction) - 5 min

**管理员**：
JSON 虽然好用，但它对格式要求极高。
少个逗号，或者用了单引号（JSON 必须双引号），都会报错。

**(Step 3: AI Fix)**
如果你手滑把 json 文件改坏了：
`{ "name": "Leo" "level": 3 }` (中间缺了逗号)。
Python 读取时会爆 `JSONDecodeError`。

这时候，把那个坏掉的文件内容贴给 Anti-gravity：
> "Fix this JSON string for me."

它会一眼看出缺了什么，并给你一个合法的版本。

---

## 4. 课后预告 (Teaser) - 2 min

**管理员**：
细心的探险家可能发现了，刚才代码里我提到了一个词：`with open...` 但我还是用了 `file.close()`。
你有没有觉得，每次都要记得写 `close()` 很麻烦？而且万一程序中间报错了，`close()` 没执行怎么办？文件就会锁死。

下一节课 (Lesson 3)，我要教你们 Python 里最优雅的语法糖——**Context Manager (上下文管理器)**。
有了它，你再也不用写 `close()` 了。

**Data archived. Configuration saved.**
(数据已归档。配置已保存。)
