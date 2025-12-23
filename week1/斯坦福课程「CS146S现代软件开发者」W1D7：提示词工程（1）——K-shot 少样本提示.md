# 斯坦福课程「CS146S现代软件开发者」W1D7：提示词工程（1）——K-shot 少样本提示

在 W1D6 中，我们学习了 Python 的核心逻辑零件。今天，我们将进入 **Prompt Engineering (提示词工程)** 的核心实战。

我们将通过两个截然不同的案例——从“成功”到“失败”，来彻底理解 **K-shot (少样本提示)** 的威力和边界。

---

## 1. 案例一：让话痨 AI 闭嘴 (格式映射)

假设你正在为一套智能家居系统编写后端代码。你的用户会用自然语言下指令（如“把声音调大点”），而你的程序需要接收一个标准的系统指令码（如 `SYS_VOLUME_UP`）。

对于这个任务，普通的 AI 助手往往会“好心办坏事”。

### 1.1 全景预览：代码分片解析

*(我们将整段 `k_shot_prompting.py` 代码拆解为 4 页演示片，并在每一页中复现我们 W1D6 掌握的逻辑手术刀)*

#### 片段 1：基础设施与环境准备
```python
import os
from dotenv import load_dotenv
from ollama import chat  # 这是 SDK，我们的贴身翻译秘书

load_dotenv()
```
- **W1D6 联动：SDK 的外交逻辑**。
    - 还记得上节课讲的“数据的出海之旅”吗？这里的 `from ollama import chat` 就是我们请来的专业翻译官（SDK）。
    - 它的职责是帮我们处理复杂的 JSON 序列化和网络请求，让我们只需关注业务逻辑。

#### 片段 2：教案与判分标准
```python
# 这里的测试次数设为 5 次，确保稳定性
NUM_RUNS_TIMES = 5

# TODO: 这是我们要填写的“教案区域” (K-shot 例子)
YOUR_SYSTEM_PROMPT = ""

# 用户提问与预期标准
USER_PROMPT = "把音量调大一点"
EXPECTED_OUTPUT = "SYS_VOLUME_UP"
```
- **W1D6 联动：定标与准备**。
    - 我们定义了 `EXPECTED_OUTPUT`，这在逻辑上相当于建立了一个“正确答案”的参照。稍后我们会用 W1D6 学的 `==` 运算符，将它与 AI 的实际产出进行“撞击实验”。

#### 片段 3：核心测试逻辑 (逻辑工厂与对话容器)
```python
def test_your_prompt(system_prompt: str) -> bool:
    success_count = 0
    
    for idx in range(NUM_RUNS_TIMES):
        # 调用 SDK：这是 AI 与世界的连接点
        response = chat(
            model="ministral-3:3b",
            # 💡 联动：这就是字典组成的列表 (List of Dicts)
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
```
- **W1D6 联动：容器与循环的力量**。
    - **数据结构**：`messages` 列表里装着两个字典，这正是我们上节课重点演练的“AI 对话容器”。
    - **自动化阀门**：`for idx in range(NUM_RUNS_TIMES)` 正是我们上节课提到的“复读机”精神——不相信单次成功，用循环进行压力测试。

#### 片段 4：自动化裁判与任务闭环
```python
        output_text = response.message.content.strip()
        
        # 💡 联动：布尔值的裁判逻辑
        if output_text == EXPECTED_OUTPUT:
            print(f"Test {idx+1}: SUCCESS ✅")
            success_count += 1
        else:
            print(f"Test {idx+1}: FAILED ❌ (Output: {output_text})")
            
    # 计算最终成功率
    return success_count == NUM_RUNS_TIMES

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)
```
- **W1D6 联动：布尔判官与入口函数**。
    - **逻辑门**：`if ... == ...` 操作符生成了一个布尔值。这是程序做决定的地基。
    - **入口封装**：通过 `if __name__ == "__main__":` 将逻辑锁死，确保脚本被直接运行时才会启动这台“自动化测试工厂”。

### 1.2 失败现场：Zero-shot 的困境

如果你直接运行脚本（System Prompt 为空），你会看到类似这样的惨状：

```text
Test 1: FAILED ❌ (Output: 好的，没问题！我已为您把音量调大了。 🔊)
Test 2: FAILED ❌ (Output: 收到，正在执行音量调节指令...)
```

**问题所在**：模型把你当成了**聊天对象**，而不是**编译器**。它不懂你的“私有协议”。

### 1.3 K-shot 救场：样卷效应

这时候，与其费劲解释“请不要输出任何多余字符，只输出指令码...”，不如直接甩给它几个例子。这就是 **K-shot (少样本提示)**。

请将以下内容填入 `YOUR_SYSTEM_PROMPT`：

```python
# 这里的例子就像是“词典”，教 AI 将 A 翻译成 B
YOUR_SYSTEM_PROMPT = """
你是一个智能家居指令转换器。
Example 1:
Input: 打开空调
Output: SYS_AC_ON

Example 2:
Input: 关闭所有灯
Output: SYS_LIGHTS_OFF_ALL

Example 3:
Input: 播放音乐
Output: SYS_MUSIC_PLAY
"""
```

再次运行脚本：
```text
Test 1: SUCCESS ✅
Test 2: SUCCESS ✅
Test 3: SUCCESS ✅
```

**✅ 结论 1**：K-shot 极擅长解决 **Format (格式)** 和 **Protocol (协议)** 问题。它能强迫 AI 遵循某种特定的说话方式。

---

## 2. 案例二：教不会的“把式” (逻辑硬伤)

既然 K-shot 这么好用，是不是所有问题给了例子就能解决？
让我们试一个更难的任务：**单词字母倒序**。

### 2.1 变身：从智能家居到算法大师

这就需要我们对代码进行一次“大换血”。既然我们已经验证了 K-shot 在格式转换上的成功，现在让我们保留底层的测试逻辑（不用动），只修改顶部的**配置区域**。

请回到 `k_shot_prompting.py`，执行以下**三步走**：

1.  **修改题目 (`USER_PROMPT`)**：把之前的“打开电视”改成更难的“倒序”。
2.  **修改标准答案 (`EXPECTED_OUTPUT`)**：把系统指令码改成倒序后的字符串。
3.  **重写教案 (`YOUR_SYSTEM_PROMPT`)**：**关键一步！** 请务必删掉之前的“智能家居”例子（否则 AI 会精神分裂），并填入新的“倒序”例子。

为了方便，你可以直接复制下面的代码，**完整覆盖**掉你代码中原来的 `TODO` 和 `PROMPT` 区域：

```python
# --- ✂️ 请从这里开始复制，覆盖原有的配置区域 ✂️ ---

# 任务变更：我们要测试 AI 的逻辑能力（倒序）
# 注意：这是一个逻辑陷阱，看 K-shot 能不能教会它
USER_PROMPT = "将单词 httpstatus 的字母顺序反转"
EXPECTED_OUTPUT = "sutatsptth"

# 这里的 K-shot 例子如果不换，AI 就会不知所措
# 所以我们要填入新的“倒序样卷”
YOUR_SYSTEM_PROMPT = """
你是一个单词倒序机器人。
Example 1:
Input: apple
Output: elppa

Example 2:
Input: data
Output: atad

Example 3:
Input: network
Output: krowten
"""
# --- ✂️ 复制结束 ✂️ ---
```

运行脚本，你会发现一个令人绝望的现象：即使你给了 3 个甚至 10 个例子，`ministral-3:3b` 依然大概率**做不对**。
它可能会输出：`statushttp` 或者 `stutptth`（丢三落四）。

### 2.3 核心解密：Tokenization 与 智力边界

为什么“翻译指令”能学会，但在“倒序”上 K-shot 失效了？

1.  **散光眼 (Tokenizer)**：模型看到的根本不是 `network` 这 7 个字母，而是一个 ID 为 `9231` 的 Token。它甚至“看不见”里面的 `w` 和 `k`。
2.  **只有“把式”没有“内功”**：K-shot 只能教 AI **“输出的样子长得像倒序”**（比如结尾可能是元音，或者乱序排列），但无法赋予小模型它本身不具备的**复杂字符操作逻辑**。

**🚨 结论 2**：如果任务涉及复杂的**逻辑推理 (Logic/Reasoning)** 或 **底层认知盲区**，K-shot 往往无能为力。

---

## 3. 核心复盘：K-shot 的能力边界

实验结果告诉我们，虽然 K-shot 是一个强大的工具，但它并不是万能的。

### 3.1 格式 vs 逻辑
*   **在“智能家居”案例中**，AI 只需要模仿你的**格式 (Format)**。这就像是学骑自行车，你演示几遍，它就学会了动作。
*   **在“单词倒序”案例中**，AI 需要进行底层的**逻辑运算 (Logic)**。这就像是解微积分，光看答案（Input/Output）是学不会解题步骤的。

### 3.2 预告：如何突破逻辑瓶颈？
既然光给“样卷”不够，我们需要教 AI 学会“打草稿”。
在下一节课 **(W1D8)** 中，我们将不再满足于 Input/Output 的简单映射，而是引入 Prompt Engineering 中最令人兴奋的技术——**思维链 (Chain of Thought, CoT)**。

我们将教 AI 把思考过程“写出来”，看它能不能打破这个逻辑魔咒。

---

## 4. 课后作业：挑战上帝的骰子 (Temperature)

在脚本中，你可能注意到了 `options={"temperature": 0.5}`。这是 AI 的“脾气调节阀”。

**Temperature (温度)** 控制了 AI 输出的随机性：
*   **0.0 (绝对理性)**：每次回答一模一样，适合 Coding、API 转换。
*   **1.0 (灵感爆发)**：每次回答都不一样，适合写小说、头脑风暴。

**你的任务**：
1.  回到“案例一（智能家居）”。
2.  将 temp 改为 **1.5** (极高)。
3.  运行脚本，看看 AI 是否开始胡言乱语，甚至编造出不存在的指令码？
4.  思考：对于 API 接口对接这种任务，应该用高温度还是低温度？

---

## 本课总结

1.  **K-shot (少样本)** 是解决**格式规范 (Formatting)** 和 **私有协议** 的最佳手段。
2.  不要指望 K-shot 能神奇地提升模型本身的**智力 (Reasoning)**。
3.  遇到逻辑硬伤时，我们需要更高级的 Prompt 技巧（下节课见）。
