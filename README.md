# 001 · Python Learning Lab 🚀

> 一个持续迭代的 Python / Git / AI 学习仓库。目标不是“收藏代码”，而是把每个知识点做成能运行的小项目。

## ✨ 目前包含

| 项目 | 内容 | 主要知识点 |
|---|---|---|
| [01 · Hello World](projects/01_hello_world) | 交互式问候程序 | 输入输出、变量、字符串、f-string |
| [02 · Number Guess](projects/02_number_guess) | 猜数字小游戏 | while、if、random、输入校验 |
| [03 · Todo CLI](projects/03_todo_cli) | 命令行待办清单 | 函数、列表、循环、程序结构 |

完整项目索引见 [projects/README.md](projects/README.md)。

## 🧭 学习路线

当前路线：

```text
Python 基础
   ↓
Git / GitHub
   ↓
命令行小项目
   ↓
文件处理 / API
   ↓
自动化脚本
   ↓
Ollama / 本地 AI / Agent
```

详细规划见 [LEARNING_PATH.md](LEARNING_PATH.md)。

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/muxiaoqing233/001.git
cd 001
```

### 2. 检查 Python

推荐 Python 3.10+：

```bash
python --version
```

Windows 上如果 `python` 不可用，可以尝试：

```bash
py --version
```

### 3. 运行项目

例如：

```bash
python projects/02_number_guess/main.py
```

## 📁 目录结构

```text
001/
├─ .github/
│  └─ workflows/
│     └─ python-check.yml
├─ docs/
│  └─ GIT_CHEATSHEET.md
├─ projects/
│  ├─ 01_hello_world/
│  ├─ 02_number_guess/
│  └─ 03_todo_cli/
├─ .editorconfig
├─ .gitignore
├─ CONTRIBUTING.md
├─ LEARNING_PATH.md
└─ README.md
```

## ✅ 仓库原则

- 每个项目都应该能够独立运行。
- 一个项目尽量只聚焦几个新知识点。
- 重要修改使用清晰的 Git commit。
- API Key、密码、Token 等敏感信息绝不提交。
- 代码先做到“能读、能跑、能解释”，再追求复杂度。

## 🛠️ Git 提交建议

推荐使用简单、统一的提交前缀：

```text
feat:     新功能
fix:      修复问题
docs:     文档修改
refactor: 代码重构
chore:    仓库维护
```

例如：

```text
feat: add file renamer project
docs: update learning roadmap
fix: handle invalid number input
```

更多常用命令见 [Git 速查表](docs/GIT_CHEATSHEET.md)。

## 🎯 下一阶段

计划继续加入：

- 文件批量重命名器
- 简易记账程序
- 英语单词抽查器
- 免费 API 调用项目
- Windows 自动化脚本
- Ollama 本地模型调用
- 简单 AI Agent

## 🤝 关于这个仓库

这是个人学习实验室，因此代码会随着学习不断重构。与其追求一次写出“完美代码”，更重要的是留下可追踪、可复现的成长记录。
