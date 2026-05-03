AI Agent Workflow

一个基于大模型的多 Agent 自动化工作流项目，用于开发辅助、脚本生成和内容处理。

---

🚀 Overview

该项目用于将日常 AI 使用，从简单对话升级为可复用的自动化流程。

核心流程：

User Input → Task Planning → Multi-Agent Execution → Validation → Output

---

🧠 Architecture

- MainAgent：任务解析与流程控制
- CodeAgent：生成自动化脚本（Python / Shell）
- TextAgent：文本处理与结构化输出
- LogicAgent：逻辑分析与结果校验

---

⚙️ Example

def main():
    user_input = "Generate a batch video processing script"
    print(f"Processing: {user_input}")

---

📌 Use Cases

- 自动生成批处理脚本（视频处理 / 文件整理）
- 技术问题分析
- 文档总结与内容生成

---

📊 Notes

- 当前为个人工作流原型（prototype）
- 已在日常使用中
- 持续优化中

---

⭐ Usage

Used in daily workflow for automation tasks and development assistance.

## 📁 Project Structure

- agents/
- docs/
- main.py


AI Agent Workflow

A lightweight multi-agent workflow system powered by LLMs, designed to automate development tasks, script generation, and content processing.

---

🚀 Overview

This project transforms traditional prompt-based usage into a structured and reusable workflow:

User Input → Task Planning → Multi-Agent Execution → Validation → Output

---

🧠 Architecture

- MainAgent: Orchestrates task parsing and workflow control
- CodeAgent: Generates automation scripts (Python / Shell)
- TextAgent: Handles formatting and structured output
- LogicAgent: Performs reasoning and validation

---

⚙️ Example

from agents.main_agent import MainAgent

agent = MainAgent()
result = agent.run("Generate a batch video processing script")

print(result)

---

📌 Use Cases

- Automation script generation
- Technical problem analysis
- Content summarization and structuring

---

📁 Project Structure

- agents/
- utils/
- docs/
- examples/
- main.py

---

📊 Status

- Personal workflow prototype
- Actively used in daily tasks
- Continuously evolving

---

🔧 Future Work

- API integration
- Task automation execution
- Deployment on server / container

---

⭐ Usage

Used as part of a personal workflow for automation and development assistance.
