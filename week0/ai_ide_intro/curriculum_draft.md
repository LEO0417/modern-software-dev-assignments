# Antigravity AI IDE 入门课程大纲 (草案)

## 目标
帮助零基础学员熟练使用 Antigravity IDE，掌握运行 Week 1 代码所需的能够环境配置、依赖管理和调试技巧。

## 模块 1: 初识 Antigravity (Hello World)
*   **界面概览**: 编辑区、终端(Terminal)、侧边栏(Explorer) 的作用。
*   **打开项目**: 如何正确打开 `week1_cn` 文件夹作为一个 Project (Workspace)。
*   **第一个脚本**: 新建一个 `hello.py` 并运行它。
    *   *知识点*: 文件与文件夹的操作，UI 上的 "Run" 按钮 vs 终端命令。

## 模块 2: 掌控终端 (The Terminal)
*   **为什么需要终端**: 很多高级操作（如下载库）需要命令行。
*   **基础命令**: `pwd` (我哪?), `ls` (有什么?), `cd` (去哪?)。
*   **运行 Python**: `python rag.py` 的含义。

## 模块 3: 依赖管理 (Package Management)
*   **问题引入**: 尝试运行 `rag.py`，遇到 `ModuleNotFoundError: No module named 'ollama'`.
*   **解决方法**: `pip install`.
    *   *解释*: 什么是库(Library/Package)，类似于给手机装 App。
    *   *实操*: 安装 `ollama`, `python-dotenv`.
*   **虚拟环境 (进阶)**: 简单提及 `venv` 或 `poetry` 的作用（隔离环境），但在入门阶段可能先演示全局/当前环境安装，避免过早劝退。

## 模块 4: 环境变量与安全 (Environment Variables)
*   **问题引入**: 代码中的 `load_dotenv()` 是做什么的？
*   **概念**: 为什么不能把密码/Key 写在代码里？(.env 文件的重要性)。
*   **实操**:
    *   创建 `.env` 文件。
    *   配置示例变量 (虽然 Ollama 跑本地不需要 Key，但可以模拟一个，或者为了后续 API 课程做准备)。

## 模块 5: AI 辅助编程 (AI Assisted Coding)
*   **代码解释**: 选中 `rag.py` 的一段看不懂的代码，右键 "Explain with AI" (或使用 Chat 面板)。
*   **智能调试**: 当终端报错时，如何用 AI 一键分析错误原因。
*   **补全代码**: 体验 AI 自动补全代码片段。

## 模块 6: 本地 LLM 的准备 (Ollama Setup)
*(针对 Week 1 RAG 课程的特需内容)*
*   **安装 Ollama**: 如何下载并运行 Ollama 服务。
*   **拉取模型**: `ollama pull llama3.1:8b`。
*   **验证**: 在终端测试 `ollama run llama3.1:8b` 确保服务正常。

## 大作业 (Checkpoint)
*   **任务**: 配置好环境，成功运行 `rag.py`，并看到 "SUCCESS" 输出。
