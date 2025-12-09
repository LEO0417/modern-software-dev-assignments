# Lesson 1: Intelligence Report (情报分析 - 数据分析基础) 📊 (口播稿)

> **场景建议**：背景音是战术指挥室的背景嘈杂声，雷达滴答声。
> **预计时长**：20 分钟
> **角色**：战区总指挥 (Commander/Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**总指挥**：
指挥官们，请看大屏幕。

我们手里有一份侦察机传回来的数据——`mission_data.csv`。
里面记录了过去 100 次任务的燃油消耗和飞行时间。

仅仅把它们读出来（Explorer 的工作）是不够的。
我要知道的是：**平均油耗是多少？哪一次任务最危险（耗时最长）？我们的效率是在提升还是下降？**

这就是 **Data Analysis (数据分析)**。
虽然外面有很多重型武器像 Pandas，但作为一个指挥官，你必须具备用一把匕首（原生 Python）就能解剖数据的能力。

---

## 1. 制造数据 (Mock Data) - 5 min

**总指挥**：
先造点数据。
**(Step 1: Setup)**
新建 `analysis_base.py`。

```python
# 这是一个任务列表
missions = [
    {"id": 101, "fuel": 500, "duration": 45},
    {"id": 102, "fuel": 450, "duration": 40},
    {"id": 103, "fuel": 600, "duration": 55},
    {"id": 104, "fuel": 480, "duration": 42},
    {"id": 105, "fuel": 800, "duration": 90}  # 异常任务
]
```

---

## 2. 战术计算 (Tactical Calculation) - 8 min

**总指挥**：
现在，我要三个指标：总油耗、平均飞行时间、最高油耗。

**(Step 2: Manual Code 手写逻辑)**

```python
total_fuel = 0
total_duration = 0
max_fuel = 0

for m in missions:
    # 累加
    total_fuel += m["fuel"]
    total_duration += m["duration"]
    
    # 寻找最大值 (打擂台法)
    if m["fuel"] > max_fuel:
        max_fuel = m["fuel"]

avg_duration = total_duration / len(missions)

print(f"Total Fuel: {total_fuel}")
print(f"Avg Duration: {avg_duration} mins")
print(f"Max Fuel Burn: {max_fuel}")
```

**总指挥**：
这看起来很简单？
在 Week 1 里，我们要分析的是 Token Usage（Token 使用量）。逻辑是一模一样的。
如果你不会算列表的平均值，你就不知道你的 AI 模型是不是在浪费钱。

---

## 3. AI 参谋：复杂指标 (AI Interaction) - 5 min

**总指挥**：
现在我要一个难的指标：**中位数 (Median)** 飞行时间。
计算中位数需要先排序，再找中间的数。这写起来有点麻烦。

**(Step 3: AI Command)**
把 `missions` 列表贴给 Anti-gravity。
> "Calculate the median duration from this list of dictionaries."

**AI 预期**：
它可能会用 `statistics` 模块，或者写一个排序逻辑：
```python
import statistics
durations = [m["duration"] for m in missions]
median = statistics.median(durations)
print(f"Median Duration: {median}")
```

**总指挥**：
这就是指挥官的效率。
你定义战略目标（我要中位数），AI 参谋提供执行方案。

---

## 4. 课后预告 (Teaser) - 2 min

**总指挥**：
情报分析完毕。我们发现任务 105 油耗异常高。
如果我们要把这份报告发送给总部，我们需要调用总部的 API。
但是，调用 API 需要一个 **Secret Key (密钥)**。

如果你们谁敢把密钥直接写在 Python 代码里上传到 GitHub，我会亲手把你的飞行执照撕碎。
那是极其危险的泄密行为。

下一节课 (Lesson 2)，我们将学习保护机密的最高准则——**Environment Variables (环境变量)**。

**Report filed. Prepare for encryption.**
(报告已归档。准备加密。)
