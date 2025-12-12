# Lesson 1: Orbit Survival (轨道求生 - 变量与生还) 🛰️ (口播稿)

> **场景建议**：背景音是急促的警报声，然后转为沉重的呼吸声和仪器运转声。
> **预计时长**：25 分钟
> **角色**：领航员 (Instructor) - 语气严肃，带有紧迫感。

---

## 0. 紧急开场 (Emergency Opening) - 3 min

**领航员**：
(拍打麦克风)
这里是控制中心。所有学徒，立即汇报状态。

听着，这不是演习。
我们的飞船 `Antigravity` 号刚刚遭遇了太阳风暴。主控电脑重启了。
现在，所有的仪表盘都是黑的。
你不再是在宽敞明亮的教室里学习 Python 语法。
你现在就在**轨道上**。你需要手动输入指令来维持飞船的生命维持系统。

在这个高度，哪怕一个小数点的错误，都会让我们化为灰烬。
我们必须重新定义周围的一切。
在这里，变量不仅仅是内存里的盒子。
**Variables are Life.** (变量即生命)。

---

## 1. 启动手动控制台 (Integers as Crew) - 8 min

**领航员**：
首先，我们需要通过手动指令清点幸存人数。
请立刻接管控制台。

**(Step 1: The Terminal)**
1.  **打开控制面板**：点击 IDE 顶部的 "Terminal" -> "New Terminal"。
2.  **激活环境**：我们必须进入那个在 Infants 阶段建立的安全屋。
    输入：`conda activate ai_course`
    看到 `(ai_course)` 出现，才说明你安全了。
3.  **进入 Python 交互模式**：
    输入：`python`
    看到 `>>>` 符号，说明你已经连接上了飞船的核心引擎。

**(Step 2: The REPL Check)**
我们需要确认船员数量。在 Python 里，船员必须是 **Integer (整数)**，因为人是不可分割的。
在 `>>>` 后面输入：
```python
crew_count = 5
print(crew_count)
```
你会立刻看到输出 `5`。

**领航员**：
好，系统有反应了。
但如果我们要检查几十项数据（燃料、氧气、护盾），这样一行行敲太慢了。
如果敲错一行，就要全部重来。
我们没有时间浪费。

**(Step 3: The Script)**
我们要创建一个**自动化脚本**。
1.  在左侧 Explorer (资源管理器) 右键及新建文件，命名为 `orbit_survival.py`。
2.  以后我们所有的指令，都写在这个文件里。

现在，把刚才的指令写入文件：
```python
# Orbit Survival Script
crew_count = 5
print(f"Crew Check: {crew_count}")
```
写完后，在 Terminal 里按下 `Ctrl+Z` (Win) 或 `Ctrl+D` (Mac) 退出 Python 模式（回到 `(ai_course)`）。
然后运行脚本：
`python orbit_survival.py`

如何运行脚本请查看infant课程第二课「登机」

看到结果了吗？这才是 Pilot 的工作方式。
接下来的所有计算，我们都在这个脚本里完成。

**(Step 4: The Critical Error)**
回到代码里。为什么必须是整数？
因为如果你输入 `5.5`，系统会认为有一半个船员挂在外面。这会导致生命维持系统报错。
我们来试一次**受控的错误**。
把 `5` 改成 `5.5`，再次运行脚本。
问右边的 AI 副驾驶 (Right Panel)：
> "Why is it dangerous to use a float for crew count in a life support system?"

AI 会告诉你：逻辑错误。这也是作为指挥官的第一课：**选择正确的数据类型，是对生命的尊重。**

---

## 2. 浮点数：生死的精度 (Floats as Fuel) - 6 min

**领航员**：
好，人齐了。接下来看燃料。
这就完全不同了。
燃料不仅可以分割，而且必须极其精确。
如果你只告诉引擎剩下 `90` 吨燃料，而实际上是 `90.000000001` 吨。
那微小的误差在几百万公里的航程中，会让你错过火星轨道。

**(Step 2: The Fuel Gauge)**
我们需要 **Float (浮点数)**。
```python
fuel_level = 98.7564
burn_rate = 1.2
```
**领航员**：
现在，试着算一下我们还能飞多久。
```python
# 计算剩余时间
flight_hours = fuel_level / burn_rate
print(f"Time remaining: {flight_hours} hours")
```
看着那个长长的小数点。
那就是你的**命**。
如果你把它四舍五入变成了 `int`，你就把那一小时的求生时间扔掉了。
在 Stanford Course 的科学计算里，这种精度意识至关重要。

---

## 3. 布尔值：系统的脉搏 (Booleans as System Status) - 4 min

**领航员**：
最后，我们需要知道飞船是不是还活着。
**Boolean (布尔值)**。
它只有两个状态：`True` (生) 或 `False` (死)。

**(Step 3: System Check)**
```python
is_oxygen_stable = True
has_hull_breach = False

print(f"Oxygen System: {is_oxygen_stable}")
print(f"Hull Breach Alert: {has_hull_breach}")
```
想象一下，如果这里弄反了。
`has_hull_breach = True` (船壳破裂 = 真)。
那红灯就会疯响。
所有的自动防御系统（我们将在 Lesson 4 编写它们）都依赖这几个简单的 True/False 来决定是否封锁舱门。
运行脚本，确认系统状态。

---

## 4. f-string：最后遗言 (The Black Box Record) - 5 min

**领航员**：
如果——我是说如果——我们没能挺过去。
我们需要留下黑匣子记录。
我们需要把刚才定义的那些散乱的数据（人数、燃料、状态）拼成一条完整的信息，发送回地球。

在旧时代，你会手忙脚乱地用加号拼凑字符串，然后因为忘记把 `int` 转成 `string` 而导致发报失败（Crash）。
但我们没有时间报错。
我们要用 **f-string**。

**(Step 4: The Report)**
```python
report = f"""
== EMERGENCY BROADCAST ==
Crew Alive: {crew_count}
Fuel Remaining: {fuel_level}
Oxygen Stable: {is_oxygen_stable}
Status: CRITICAL
"""
print(report)
```
**领航员**：
看着屏幕上打印出的这段话。
它不仅仅是一段文本。它是我们存在的证明。
这也是你们未来构建 **AI Prompts** 的雏形。
你必须学会如何把冰冷的数据，嵌入到人类的语言框架中。

---

## 5. 总结 (Debrief) - 2 min

**领航员**：
警报暂时解除。
我们重新定义了飞船的状态。
*   Integers 是我们的战友。
*   Floats 是我们的燃料。
*   Booleans 是我们的脉搏。

但现在，坐在你右边的那个 AI 副驾驶（Agent），它刚才一直很安静。
下一节课，我们要激活它。
但记住，它不是神。它只是一个刚刚出厂的、有点傻的**翻译官**。
我们需要学会如何跟它说话，它才不会听不懂指令把我们害死。
Prepare for Lesson 1.5: **The Universal Translator**.

**Orbit stable. Stand by.**
(轨道稳定。待命。)
