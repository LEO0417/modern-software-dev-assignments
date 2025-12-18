# week1 课程（下）：进阶提示词工程

在本节课中，我们将深入探讨更高级的提示词技术，包括思维链、工具调用、自洽性、RAG 和自我反思。我们将继续使用斯坦福 week1 提供的脚本进行实践。

---

## 1. 技术进阶与源码讲解

### 1.1 K-shot Prompting (少样本提示)
**源码文件:** `week1/k_shot_prompting.py`

#### 1.1.1 核心概念
K-shot（或 Few-shot）提示是指在提示词中提供 $K$ 个示例。这对于任务定义模糊或需要特定输出格式的情况非常有效。模型通过“模仿”示例来理解预期行为。

#### 1.1.2 脚本初始化与环境配置
```python
import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()
NUM_RUN_TIMES = 5
```
**详解:**
- **`load_dotenv`**: 加载运行环境。
- **`NUM_RUN_TIMES`**: 设置重复测试次数，以验证提示词在不同生成中的稳健性。

#### 1.1.3 任务定义与核心提示词
```python
# TODO: 在这里填入你的系统提示词！
YOUR_SYSTEM_PROMPT = ""

USER_PROMPT = """
将下列单词中的字母顺序反转。只输出反转后的单词，不要包含其他任何文本：
httpstatus
"""
EXPECTED_OUTPUT = "sutatsptth"
```
**详解:**
- **任务**: 反转字符串字母。
- **K-shot 策略**: 在 `YOUR_SYSTEM_PROMPT` 中不仅要描述任务，还要给出示例，例如：`示例：apple -> elppa`。

#### 1.1.4 测试循环与比对逻辑
```python
def test_your_prompt(system_prompt: str) -> bool:
    response = chat(
        model="ministral-3:3b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": USER_PROMPT},
        ],
        options={"temperature": 0.5},
    )
    if response.message.content.strip() == EXPECTED_OUTPUT:
        return True
```
**详解:**
- **`chat` 调用**: 使用 `ministral-3:3b` 小模型进行测试。
- **`.strip()`**: 清洗输出文本，确保匹配过程不受白字符干扰。

---

### 1.2 Chain-of-thought (思维链, CoT)
**源码文件:** `week1/chain_of_thought.py`

#### 1.1.1 核心概念
思维链（CoT）引导模型展示其推理过程。通过要求模型“一步步思考”，可以显著提高其处理复杂逻辑、常识推理或数学问题的能力。

#### 1.1.2 计算任务与正则表达式提取
```python
USER_PROMPT = """
解决这个问题，然后在最后一行以 "Answer: <数字>" 的格式给出最终答案。

计算 3^{12345} (mod 100) 的值是多少？
"""

def extract_final_answer(text: str) -> str:
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        if num_match:
            return f"Answer: {num_match.group(0)}"
        return f"Answer: {value}"
    return text.strip()
```
**详解:**
- **数学陷阱**: 这是一个典型的需要寻找周期性规律的问题。
- **`re.findall`**: 模型会输出长篇推理，我们需要精准抓取最后一行符合 `Answer: XX` 格式的内容。

#### 1.1.3 严谨性配置
```python
response = chat(
    model="gemini-3-flash-preview:cloud",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": USER_PROMPT},
    ],
    options={"temperature": 0.3},
)
```
**详解:**
- **`temperature: 0.3`**: 对于逻辑性很强的任务，我们通常调低温度。
- **模型选择**: 复杂逻辑推荐使用更强的 `gemini-3-flash-preview:cloud`。

---

### 1.2 Tool Calling (工具调用)
**源码文件:** `week1/tool_calling.py`

#### 1.2.1 核心概念
工具调用赋予模型与现实世界交互的能力。模型通过生成结构化的 JSON 数据，告诉程序需要调用哪个函数。

#### 1.2.2 工具函数实现 (AST 静态分析)
```python
def _list_function_return_types(file_path: str) -> List[Tuple[str, str]]:
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source)
    results: List[Tuple[str, str]] = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            return_str = _annotation_to_str(node.returns)
            results.append((node.name, return_str))
    return results
```
**详解:**
- **`ast` (Abstract Syntax Trees)**: 在不运行代码的前提下解析源码。

#### 1.2.3 模型产生 JSON 调用
```python
def extract_tool_call(text: str) -> Dict[str, Any]:
    text = text.strip()
    if text.startswith("```") and text.endswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    try: return json.loads(text)
    except json.JSONDecodeError: raise ValueError("模型未返回有效的 JSON")
```
**详解:**
- **JSON 剥离**: 确保我们能拿到纯净的 JSON 字符串。

---

### 1.3 Self-consistency (自洽性)
**源码文件:** `week1/self_consistency_prompting.py`

#### 1.3.1 核心概念
让模型走多条路，根据结果的共识程度来决定最终答案。

#### 1.3.2 多数投票机制 (Majority Voting)
```python
answers: list[str] = []
for idx in range(NUM_RUNS_TIMES):
    # ... 获取模型输出 ...
    final_answer = extract_final_answer(response.message.content)
    answers.append(final_answer.strip())

counts = Counter(answers)
majority_answer, majority_count = counts.most_common(1)[0]
```
**详解:**
- **`Counter`**: 统计每个答案出现的次数。
- **稳健性**: 提高任务的可靠性。

---

### 1.4 RAG (检索增强生成)
**源码文件:** `week1/rag.py`

#### 1.4.1 核心概念
RAG 让模型在回答前先查阅资料，解决知识过期问题。

#### 1.4.2 上下文注入 (Context Injection)
```python
def make_user_prompt(question: str, context_docs: List[str]) -> str:
    context_block = "\n".join(f"- {d}" for d in context_docs)
    return (
        f"上下文 (仅使用此信息):\n{context_block}\n\n"
        f"任务: {question}\n"
    )
```
**详解:**
- **注入策略**: 强迫模型阅读 `context_block` 里的文本。

---

### 1.5 Reflexion (自我反思)
**源码文件:** `week1/reflexion.py`

#### 1.5.1 核心概念
反思技术允许模型根据错误反馈来自我修正。

#### 1.5.2 给模型第二次机会
```python
# 阶段 1
code = generate_initial_function(system_prompt)
passed, failures = evaluate_function(func)

# 阶段 2 (反思)
if not passed:
    improved_code = apply_reflexion(reflexion_prompt, build_context, code, failures)
```
**详解:**
- **反馈闭环**: 逻辑修正的核心。

---

## 2. 预备知识复习

*   **正则表达式**: `re.findall` 的基本用法。
*   **温度调节**: 0.0 vs 1.0 的应用场景。
*   **JSON 结构**: 结构化输出的重要性。
*   **多数投票逻辑**: 稳健性提升。
