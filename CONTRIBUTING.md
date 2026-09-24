# Contributing

这个仓库主要用于个人学习，但仍然按照真实项目的方式维护。

## 开发约定

1. 一个提交尽量只做一件事。
2. 新项目放在 `projects/` 下，并使用编号目录。
3. 每个项目至少包含：
   - `main.py`
   - 简短 `README.md`
   - 明确的运行方式
4. 不提交密码、API Key、Token、Cookie、私钥或个人隐私数据。
5. 修改后至少确认 Python 文件可以通过语法检查。

## Commit Message

推荐格式：

```text
feat: add new project
fix: handle invalid input
docs: update README
refactor: simplify todo logic
chore: update repository config
```

## Pull Request

如果以后使用分支开发，建议：

```text
main
 └─ feature/xxx
      └─ Pull Request → main
```

保持 PR 小而清晰，更容易检查和回滚。
