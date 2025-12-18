# 第 1 周：提示词工程技术（Prompting Techniques）

在本课程中，我们将学习如何通过不同的提示词技术来增强大语言模型（LLM）的能力。我们将使用 **Ollama** 在本地运行模型，并通过编写 Python 脚本来实践这些技术。

---

## 1. 安装 Ollama

Ollama 是一个能够在本地轻松运行大型语言模型的工具。

### macOS 安装
如果你使用 Homebrew，可以运行：
```bash
brew install --cask ollama 
ollama serve
```

### Linux 安装
运行以下命令：
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows 安装
从 [ollama.com/download](https://ollama.com/download) 下载并运行安装程序。

### 验证安装
在终端运行以下命令，如果显示版本号即表示安装成功：
```bash
ollama -v
```

---

## 2. 安装模型

本周我们将使用两个主要模型：
1.  **ministral-3:3b**: 一个轻量级但功能强大的本地模型。
2.  **gemini-3-flash-preview:cloud**: 通过 Ollama 调用云端的 Gemini 模型。

运行以下命令来准备模型。需要注意的是，通过 Ollama 调用的云端模型（如 `gemini-3-flash-preview:cloud`）由 Ollama 限量免费提供算力，无需配置 API 密钥：
```bash
ollama pull ministral-3:3b
ollama pull gemini-3-flash-preview:cloud
```

然后你可以尝试立即在终端运行它们，并且开始对话。
```bash
ollama run ministral-3:3b
ollama run gemini-3-flash-preview:cloud
```
ollama相关命令可以询问你的AI IDE，比如：
```bash
ollama serve    # 启动 Ollama 后台服务
ollama list     # 查看本地已下载的模型列表
ollama pull     # 从模型库拉取（下载）指定模型
ollama run      # 运行模型并进入交互式对话模式
ollama rm       # 删除本地指定的模型
ollama ps       # 查看当前正在内存中运行的模型
ollama --help   # 查看所有可用命令的详细帮助
```
同时，ollama也推出了UI对话界面，让你和模型对话更加方便。

当然，我们不会满足于在终端对话，而是要开始写代码了。在python代码中，我们使用ollama的chat函数来调用模型。
---

## 3. 技术进阶与源码讲解

在本节中，我们将详细讲解斯坦福 week1 课程提供的每个 Python 脚本，每个脚本都代表了一种核心的提示词技术。

### 3.1 K-shot Prompting (少样本提示)
**源码文件:** `week1/k_shot_prompting.py`

#### 3.1.1 核心概念
K-shot（或 Few-shot）提示是指在提示词中提供 $K$ 个示例。这对于任务定义模糊或需要特定输出格式的情况非常有效。模型通过“模仿”示例来理解预期行为。

#### 3.1.2 脚本初始化与环境配置
```python
import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5
```
**详解:**
- **`ollama.chat`**: 这是与 Ollama 服务交互的核心入口。
- **`load_dotenv`**: 加载 `.env` 文件，虽然本地 Ollama 通常不需要密钥，但这是一个良好的编程习惯。
- **`NUM_RUNS_TIMES`**: 设置运行次数。由于 LLM 输出有随机性，多次运行有助于测试提示词的稳健性。

#### 3.1.3 任务定义与预期输出
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
- **System Prompt**: 你的任务目标。通过在这里加入 K-shot 示例（如 `apple -> elppa`），可以显著提升 `ministral-3:3b` 小模型的表现。
- **User Prompt**: 具体待处理的数据。

#### 3.1.4 测试循环与模型调用
```python
def test_your_prompt(system_prompt: str) -> bool:
    for idx in range(NUM_RUNS_TIMES):
        print(f"执行测试 {idx + 1} / {NUM_RUNS_TIMES}")
        response = chat(
            model="ministral-3:3b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
        output_text = response.message.content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"预期输出: {EXPECTED_OUTPUT}")
            print(f"实际输出: {output_text}")
    return False
```
**详解:**
- **`chat` 函数**: 传入 `messages` 列表（包含 system 和 user 角色）。
- **`temperature: 0.5`**: 平衡生成文本的随机性。
- **`.strip()`**: 极其重要，模型偶尔会多出一个换行符，清理后再比对能提高测试通过率。

---

### 3.2 Chain-of-thought (思维链, CoT)
**源码文件:** `week1/chain_of_thought.py`

#### 3.2.1 核心概念
思维链（CoT）引导模型展示其推理过程。通过要求模型“一步步思考”，可以显著提高其处理复杂逻辑、常识推理或数学问题的能力。

#### 3.2.2 计算任务与正则表达式提取
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
- **数学陷阱**: 这是一个典型的需要寻找周期性规律的问题，直接计算 3 的 12345 次方是不现实的。
- **`re.findall`**: 模型会输出长篇推理，我们需要精准抓取最后一行符合 `Answer: XX` 格式的内容。

#### 3.2.3 严谨性配置
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
- **`temperature: 0.3`**: 对于逻辑性很强的任务，我们通常调低温度，让模型“老老实实”按照逻辑推导，不要发散。
- **模型选择**: 复杂逻辑推荐使用更强的 `gemini-3-flash-preview:cloud`。

---

### 3.3 Tool Calling (工具调用)
**源码文件:** `week1/tool_calling.py`

#### 3.3.1 核心概念
工具调用赋予模型与现实世界交互的能力。模型通过生成结构化的 JSON 数据，告诉程序需要调用哪个函数以及传入什么参数。

#### 3.3.2 工具函数实现 (AST 静态分析)
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
- **`ast` (Abstract Syntax Trees)**: 在不运行代码的前提下，通过解析语法树来提取函数的名称和返回类型。这比直接用正则表达式匹配要可靠得多。

#### 3.3.3 模型产生 JSON 调用
```python
def extract_tool_call(text: str) -> Dict[str, Any]:
    text = text.strip()
    if text.startswith("```") and text.endswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    try: return json.loads(text)
    except json.JSONDecodeError: raise ValueError("模型未返回有效的 JSON")
```
**详解:**
- **JSON 剥离**: 模型有时会画蛇添足加上 MarkDown 标签。这个辅助函数确保我们能拿到纯净的 JSON 字符串进行解析。
- **Tool Registry**: 这种模式让模型像在使用手机 App 一样，按需“点击”按钮（调用函数）。

---

### 3.4 Self-consistency (自洽性)
**源码文件:** `week1/self_consistency_prompting.py`

#### 3.4.1 核心概念
自洽性（Self-consistency）是 CoT 的升级版：让模型走多条路，根据结果的共识程度来决定最终答案。这能有效纠正单次推理中的偶然错误。

#### 3.4.2 多数投票机制 (Majority Voting)
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
- **稳健性**: 即使模型 5 次中有 2 次因为逻辑混乱算错，只要另外 3 次的结果一致且正确，多数投票就能选出正确答案。
- **高温度设计**: 此技术要求 `temperature` 设得较高（如 1.0），以激发不同的推理路径。

---

### 3.5 RAG (检索增强生成)
**源码文件:** `week1/rag.py`

#### 3.5.1 核心概念
RAG 让模型在回答前先查阅资料。这就像考试时给模型发了一份“开卷考试”的参考材料，能有效解决知识过期和幻觉问题。

#### 3.5.2 上下文注入 (Context Injection)
```python
def make_user_prompt(question: str, context_docs: List[str]) -> str:
    context_block = "\n".join(f"- {d}" for d in context_docs)
    return (
        f"上下文 (仅使用此信息):\n{context_block}\n\n"
        f"任务: {question}\n"
    )
```
**详解:**
- **注入策略**: 我们不希望模型用自己的知识瞎猜，而是强迫它阅读 `context_block` 里的文本。
- **验证机制**: 由于是在写代码，我们会检查生成的代码里是否出现了参考资料中提到的特定 API 字段（如 `X-API-Key`）。

---

### 3.6 Reflexion (自我反思)
**源码文件:** `week1/reflexion.py`

#### 3.6.1 核心概念
反思技术允许模型根据错误反馈来自我修正。它包含两个阶段：1. 尝试解决；2. 根据报错信息进行二次修改。

#### 3.6.2 给模型第二次机会
```python
# 阶段 1
code = generate_initial_function(system_prompt)
passed, failures = evaluate_function(func)

# 阶段 2 (反思)
if not passed:
    improved_code = apply_reflexion(reflexion_prompt, build_context, code, failures)
```
**详解:**
- **反馈闭环**: 这里的 `failures` 包含了测试没通过的具体原因。把这些信息喂回模型，模型通常能立刻意识到代码里缺了什么逻辑。
- **提示词技巧**: `YOUR_REFLEXION_PROMPT` 需要扮演一个严谨的代码审查官角色。

---

## 4. 预备知识复习

为了更好地制作 PPT，建议重点突出以下几个模块：

*   **正则表达式**: `re.findall` 的基本用法。
*   **温度调节**: 何时用 0.0 (精确)，何时用 1.0 (发散)。
*   **JSON 结构**: 工具调用所需的结构化参数。
*   **多数投票逻辑**: 统计学在 LLM 推理中的应用。
