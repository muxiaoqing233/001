# Yggdrasil Lab 🌳

> 以北欧神话“世界树 Yggdrasil”为名的个人编程学习实验室。这里把 Python、Git、自动化、AI 与 Agent 当作不断生长的“枝干”，用一个个可运行的小项目记录成长。

## 🌿 当前枝干

| 项目 | 内容 | 主要知识点 |
|---|---|---|
| [01 · Hello World](projects/01_hello_world) | 交互式问候程序 | 输入输出、变量、字符串、f-string |
| [02 · Number Guess](projects/02_number_guess) | 猜数字小游戏 | while、if、random、输入校验 |
| [03 · Todo CLI](projects/03_todo_cli) | 命令行待办清单 | 函数、列表、循环、程序结构 |

完整项目索引见 [projects/README.md](projects/README.md)。

## 🧭 世界树学习路线

```text
                AI / Agent
                   ▲
                   │
            自动化 / API / 工具
                   ▲
                   │
              Git / GitHub
                   ▲
                   │
               Python 基础
                   ▲
                   │
              Yggdrasil Lab
```

详细规划见 [LEARNING_PATH.md](LEARNING_PATH.md)。

## 🚀 快速开始

### 1. 克隆仓库

当前仓库名仍是 `001`：

```bash
git clone https://github.com/muxiaoqing233/001.git
cd 001
```

> 如果之后把 GitHub 仓库正式重命名为 `yggdrasil-lab`，这里再同步改为新地址。

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
Yggdrasil Lab/
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

## 🌱 仓库原则

- 每个项目都应该能够独立运行。
- 一个项目尽量只聚焦几个新知识点。
- 重要修改使用清晰的 Git commit。
- API Key、密码、Token 等敏感信息绝不提交。
- 代码先做到“能读、能跑、能解释”，再追求复杂度。
- 新知识点不是“收藏”，而是长成世界树上的新枝条。

## 🛠️ Git 提交建议

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
docs: update yggdrasil roadmap
fix: handle invalid number input
```

更多常用命令见 [Git 速查表](docs/GIT_CHEATSHEET.md)。

## 🌲 下一批枝条

计划继续加入：

- 文件批量重命名器
- 简易记账程序
- 英语单词抽查器
- 免费 API 调用项目
- Windows 自动化脚本
- Ollama 本地模型调用
- 简单 AI Agent

## 🪵 关于 Yggdrasil Lab

Yggdrasil 在北欧神话中连接不同世界。这个仓库也采用类似思路：让不同学习方向互相连接，而不是散落成一堆彼此无关的练习。

目标不是一次写出“完美代码”，而是让整棵树持续生长。
