# Git / GitHub 速查表

## 第一次下载仓库

```bash
git clone https://github.com/muxiaoqing233/001.git
cd 001
```

## 查看当前状态

```bash
git status
```

## 查看修改

```bash
git diff
```

## 提交修改

```bash
git add .
git commit -m "feat: add something"
git push
```

## 拉取远程更新

```bash
git pull
```

## 创建新分支

```bash
git switch -c feature/my-feature
```

旧版 Git 也可以：

```bash
git checkout -b feature/my-feature
```

## 切回 main

```bash
git switch main
```

## 查看提交历史

```bash
git log --oneline --graph --decorate
```

## 撤销未暂存修改

```bash
git restore 文件名
```

注意：撤销前先确认文件内容不再需要。

## 不要提交敏感信息

常见危险内容：

- API Key
- GitHub Token
- OpenAI / Ollama 外部服务密钥
- 密码
- Cookie
- 私钥
- `.env`

发现敏感信息后，不要只“删除文件再 commit”，因为旧提交里仍可能保留它。应立即撤销对应密钥并重新生成。
