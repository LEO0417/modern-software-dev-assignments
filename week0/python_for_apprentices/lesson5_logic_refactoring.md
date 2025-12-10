# Lesson 5: Navigation Audit (导航审计 - 逻辑重构与代码审查) 🧭 (口播稿)

> **场景建议**：背景音是深空探测的微弱信号声，和键盘快速敲击的声音。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor) - 冷静、严谨。

---

## 0. 航线偏离 (Course Deviation) - 3 min

**领航员**：
氧气危机解除了。但我们在混乱中偏离了航线。
自动驾驶系统生成了一段新的导航代码，声称是“根据最新的量子算法优化过的”。
但是，在这飞船上，**不要相信任何未经审查的代码**。

今天，你的身份不是 Pilot，是 **Auditor (审计官)**。
我们将学习 **Logic (逻辑控制)** 和 **Refactoring (重构)**。
我们还将使用最强大的武器——**Type Hints (类型提示)**——给狂野的 AI 代码套上缰绳。

---

## 1. 屎山导航 (Spaghetti Navigation) - 6 min

**领航员**：
让我们看看自动驾驶系统给出的代码。这也叫 **Spaghetti Code (面条代码)**。

**(Step 1: The Bad Code)**
1.  新建文件 `navigation.py`。
2.  输入这段 AI 生成的导航逻辑（或者让 Agent 生成它）：
```python
x = 100
y = "200" # 等等，为什么坐标是字符串？
status = True

if status:
   if x > 0:
       if y != "0": # 这种嵌套...
           print("Move forward")
       else:
           print("Stop")
   else:
       print("Turn back")
else:
   print("Error")
```

**领航员**：
如果你是审计官，这代码能过吗？
1.  嵌套像金字塔一样深，看着头晕。
2.  `y` 是字符串，万一有人算数怎么办？
3.  变量名 `x`, `y` 是什么意思？是星际坐标还是像素点？

这种代码如果运行在导航仪上，我们会在下一个星系路口迷路。

---

## 2. 审计与重构 (Audit & Refactor) - 8 min

**领航员**：
现在，指挥你的 Right Panel Agent 进行重构。
但记住，**你才是老板**。你不能只说 "Fix it"。你要给出具体的审计意见。

**(Step 2: Auditor Prompt)**
在 Right Panel 输入：
> "Act as a Senior Engineer. Refactor this navigation logic.
> 1. Flatten the nested if/else using guard clauses or elif.
> 2. Rename variables to be meaningful (e.g., `galaxy_x`).
> 3. Enforce types: coordinates must be integers."

Agent 可能会给出：
```python
def navigate_ship(galaxy_x, galaxy_y, system_active):
    if not system_active:
        print("System Error")
        return

    if galaxy_x <= 0:
        print("Turn back")
        return

    # 逻辑拍平了，清晰多了
    print(f"Projecting course to {galaxy_x}, {galaxy_y}")
```

**领航员**：
对比一下。
这就叫 **Refactoring (重构)**。
功能完全一样，但阅读它的风险从“极高”变成了“极低”。

---

## 3. 类型提示：给代码上锁 (Type Hints as Safety Locks) - 5 min

**领航员**：
还有一个隐患。
那个 `galaxy_y`。刚才的代码里它是字符串 `"200"`。
如果在后面的计算里，有谁把它乘了 2，它会变成 `"200200"` (字符串重复)，而不是 `400`。
我们会飞到几亿光年之外去。

我们要给变量上锁。这就是 **Type Hints**。

**(Step 3: Enforcing Types)**
修改代码：
```python
def navigate_ship(galaxy_x: int, galaxy_y: int) -> None:
    # ...
```
**领航员**：
加上 `: int`。
现在，如果你试图把 `"200"` 塞进去。
你的 Agent（如果你开启了静态分析模式）会立刻报警。
这就是我们在 Infant 阶段安装 IDE 的原因——让它在飞船起飞前就预警。

---

## 4. 总结 (Debrief) - 3 min

**领航员**：
航线已修正。代码逻辑清晰，类型安全。
我们躲过了最后一次危机。

在这个 Phase 1 里，你们已经从一个只会手动输入的学徒，变成了一个敢于质疑 AI、重构逻辑的初级审计官。
这才是 Stanford 课程的核心精神：
**We don't just write code. We engineer systems.**

下一节课 (Lesson 6)，我们将进行最后的资格认证。
你的面试官就在你的右边。
准备好迎接它的拷问了吗？

**Navigation verify. Course locked.**
(导航确认。航线锁定。)
