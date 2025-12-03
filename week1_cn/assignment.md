# Week 1 — Prompting Techniques / 第一周 — 提示工程技术

You will practice multiple prompting techniques by crafting prompts to complete specific tasks. Each task’s instructions are at the top of its corresponding source file.

你将通过编写提示词来完成特定任务，从而练习多种提示工程技术。每个任务的说明都位于其相应源文件的顶部。

## Installation / 安装

Make sure you have first done the installation described in the top-level `README.md`.

请确保你已经完成了顶层 `README.md` 中描述的安装步骤。

## Ollama installation / Ollama 安装

We will be using a tool to run different state-of-the-art LLMs locally on your machine called [Ollama](https://ollama.com/). Use one of the following methods:

我们将使用一个名为 [Ollama](https://ollama.com/) 的工具在你的本地机器上运行各种最先进的 LLM。请使用以下方法之一：

- macOS (Homebrew):
  ```bash
  brew install --cask ollama 
  ollama serve
  ```

- Linux (recommended / 推荐):
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- Windows:
  Download and run the installer from [ollama.com/download](https://ollama.com/download).
  从 [ollama.com/download](https://ollama.com/download) 下载并运行安装程序。

Verify installation / 验证安装:
```bash
ollama -v
```

Before running the test scripts, make sure you have the following models pulled. You only need to do this once (unless you remove the models later):

在运行测试脚本之前，请确保你已经拉取了以下模型。你只需要做一次（除非你后来删除了模型）：

```bash
ollama run mistral-nemo:12b
ollama run llama3.1:8b
```

## Techniques and source files / 技术与源文件

- K-shot prompting (K-shot 提示) — `week1/k_shot_prompting.py`
- Chain-of-thought (思维链) — `week1/chain_of_thought.py`
- Tool calling (工具调用) — `week1/tool_calling.py`
- Self-consistency prompting (自洽性提示) — `week1/self_consistency_prompting.py`
- RAG (Retrieval-Augmented Generation / 检索增强生成) — `week1/rag.py`
- Reflexion (反思) — `week1/reflexion.py`

## Deliverables / 交付物

- Read the task description in each file.
  阅读每个文件中的任务描述。
- Design and run prompts (look for all the places labeled `TODO` in the code). That should be the only thing you have to change (i.e. don't tinker with the model).
  设计并运行提示词（查找代码中所有标记为 `TODO` 的地方）。这应该是你需要更改的唯一内容（即不要修改模型部分）。
- Iterate to improve results until the test script passes.
  迭代改进结果，直到测试脚本通过。
- Save your final prompt(s) and output for each technique.
  保存每种技术的最终提示词和输出。
- Make sure to include in your submission the completed code for each prompting technique file. ***Double check that all `TODO`s have been resolved.***
  确保在提交中包含每个提示工程技术文件的完整代码。***仔细检查所有 `TODO` 是否已解决。***

## Evaluation rubric (60 pts total) / 评分标准 (总分 60 分)

- 10 for each completed prompt across the 6 different prompting techniques
  6 种不同的提示工程技术，每完成一种得 10 分。
