# Lesson 4: Autopilot Engaged (自动驾驶 - 综合实战) 🕹️ (口播稿)

> **场景建议**：背景音有雷达扫描的声效。
> **预计时长**：20 分钟
> **角色**：领航员 (Instructor)

---

## 0. 开场与回顾 (Intro & Recap) - 3 min

**领航员**：
飞行员们，这是 Phase 2 的终极挑战。
我们要制造一台真正的**自动化机器**。

想象一下，你是个交易员。你想盯着比特币的价格。
你现在的做法是：打开网页 -> 刷新 -> 看一眼 -> 等一会 -> 再刷新。
这是人类的做法。
机器的做法是：写个脚本，让它 24 小时盯着，价格到了就叫我。

今天，我们要用到所有学过的 Pilot 技能：
1.  **Modules**: 用 `time` 模块控制时间。
2.  **Pip lib**: 用 `requests` 抓数据。
3.  **Error Handling**: 防止网络波动让脚本挂掉。

---

## 1. 任务简报 (The Mission) - 5 min

**领航员**：
我们的目标是：写一个比特币价格监控器。
由于我们没有真实的交易账户 API，我们用免费的 CoinGecko API。

**(Step 1: Setup)**
新建 `crypto_bot.py`。
我们需要两个库：
```python
import requests
import time
```

---

## 2. 编写核心逻辑 (Core Logic) - 10 min

**领航员**：
这里我们不再手写所有代码，我们要练习**指挥 AI**。

**(Step 2: AI Command 1 - The Fetcher)**
在 IDE 里输入注释作为 Prompt：
> \# Function to fetch current bitcoin price from CoinGecko API in USD
> \# Handle potential network errors gracefully

选中它，让 AI 生成代码。
它应该会给你一个用 `try/except` 包裹的 `requests.get`。

**(Step 3: AI Command 2 - The Loop)**
然后，我们写主循环。
> \# Main loop: 
> \# Check price every 5 seconds.
> \# If price > 80000, print "SELL SELL SELL"
> \# Else, print "HODL..."

选中它，让 AI 生成。

**预期代码概览**：
```python
def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

while True:
    price = get_btc_price()
    if price:
        print(f"Current Bitcoin Price: ${price}")
        if price > 80000: # 假设值
            print("🚨 SELL SELL SELL!")
        else:
            print("🍵 HODL...")
            
    # 这就是我们要学的 time 模块
    time.sleep(5)
```

**领航员**：
运行它。
看着屏幕上一行行跳出的价格。
你可以把手拿开键盘了。你的飞船正在自动巡航。
这就是 **Automation**。

---

## 3. 课后预告 (Teaser) - 2 min

**领航员**：
做得好，Pilot。
这个脚本你可以挂在服务器上跑一年。

但是，这里有一个问题。
它只是打印在屏幕上。如果我关了电脑，或者我想回头看看上个月的价格走势，数据就丢了。
我们需要把这些珍贵的数据**保存**下来。存到文件里，或者数据库里。

下一阶段，我们将晋升为 **Explorer (探险家)**。
探险家的核心能力不是“飞”，而是“记录”和“分析”。
我们要学习 File I/O（文件读写），学习如何把这些数据持久化。

**Autopilot stable. Preparing for data archival.**
(自动驾驶稳定。准备数据归档。)
