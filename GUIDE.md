# 📖 GitHub 入门操作手册

> 整理自 2026-03-29 的实操记录，适合完全零基础的新手。

---

## 目录

1. [安装 gh 命令行工具](#1-安装-gh-命令行工具)
2. [登录 GitHub 账号](#2-登录-github-账号)
3. [创建仓库](#3-创建仓库)
4. [修改 README](#4-修改-readme)
5. [上传文件](#5-上传文件)
6. [Fork 别人的项目](#6-fork-别人的项目)
7. [给项目点 Star](#7-给项目点-star)
8. [创建 Issue](#8-创建-issue)
9. [开启 GitHub Pages](#9-开启-github-pages)
10. [常用 Git 命令速查](#10-常用-git-命令速查)

---

## 1. 安装 gh 命令行工具

`gh` 是 GitHub 官方命令行工具，让你在终端里操作 GitHub。

```bash
# macOS 安装（需要先有 Homebrew）
brew install gh

# 验证安装成功
gh --version
```

---

## 2. 登录 GitHub 账号

```bash
gh auth login
```

按提示操作：
1. 选择 `GitHub.com`
2. 选择 `HTTPS`
3. 选择 `Login with a web browser`
4. **复制终端显示的验证码**（如 `ABCD-1234`）
5. 按回车，浏览器自动打开
6. 在网页粘贴验证码，点击授权

验证是否登录成功：
```bash
gh auth status
# 应该显示：✓ Logged in to github.com account 你的用户名
```

---

## 3. 创建仓库

```bash
# 创建一个公开仓库，并自动生成 README
gh repo create 仓库名 --public --description "仓库描述" --add-readme

# 示例
gh repo create my-first-repo --public --description "我的第一个 GitHub 仓库" --add-readme
```

创建成功后会返回仓库地址，如：
```
https://github.com/你的用户名/my-first-repo
```

---

## 4. 修改 README

README 是仓库的"门面"，访问仓库时第一眼看到的内容。

```bash
# 先把仓库下载到本地
git clone https://github.com/你的用户名/my-first-repo.git
cd my-first-repo

# 编辑 README.md 文件（用任意文本编辑器）
# 修改完成后，上传到 GitHub
git add README.md
git commit -m "更新 README"
git push
```

---

## 5. 上传文件

```bash
# 进入本地仓库文件夹
cd my-first-repo

# 把文件复制进来，或直接在这里新建文件
# 然后执行以下命令上传

git add .              # 添加所有新文件
git commit -m "说明这次上传了什么"
git push               # 推送到 GitHub
```

**三步口诀：add → commit → push**

---

## 6. Fork 别人的项目

Fork = 把别人的仓库复制一份到自己账号。

```bash
# 命令格式
gh repo fork 用户名/仓库名 --clone=false

# 示例：Fork awesome 项目
gh repo fork sindresorhus/awesome --clone=false
```

Fork 后，你的账号下会多出一个同名仓库，可以自由修改。

---

## 7. 给项目点 Star

Star = 收藏 + 点赞，表示你喜欢这个项目。

```bash
# 命令格式
gh api user/starred/用户名/仓库名 -X PUT

# 示例：Star 中文大模型资源库
gh api user/starred/HqWu-HITCS/Awesome-Chinese-LLM -X PUT
```

查看你 Star 过的所有项目：
```
https://github.com/你的用户名?tab=stars
```

---

## 8. 创建 Issue

Issue = 给仓库贴便利贴，用来记录问题、想法、待办事项。

```bash
# 命令格式
gh issue create --repo 用户名/仓库名 --title "标题" --body "内容"

# 示例
gh issue create \
  --repo Devops-senao/my-first-repo \
  --title "未来计划" \
  --body "- [ ] 上传第一个代码文件\n- [ ] 学习 Git 基本命令"
```

---

## 9. 开启 GitHub Pages

GitHub Pages 可以把仓库里的 HTML 文件变成真实可访问的网站，**完全免费**。

**前提：** 仓库里有 `index.html` 文件

```bash
# 通过 API 开启 Pages
gh api repos/你的用户名/仓库名/pages \
  -X POST \
  --input - <<'EOF'
{"source":{"branch":"main","path":"/"}}
EOF
```

开启后，网站地址为：
```
https://你的用户名.github.io/仓库名/
```

> ⏳ 首次部署需要等 1~2 分钟

---

## 10. 常用 Git 命令速查

| 命令 | 作用 |
|------|------|
| `git clone 地址` | 下载仓库到本地 |
| `git add .` | 把所有修改加入暂存区 |
| `git commit -m "说明"` | 保存一个版本快照 |
| `git push` | 上传到 GitHub |
| `git pull` | 从 GitHub 拉取最新内容 |
| `git status` | 查看当前状态 |
| `git log` | 查看历史记录 |

---

## 🎯 今日成果回顾

| # | 操作 | 结果 |
|---|------|------|
| 1 | 安装 gh | ✅ 完成 |
| 2 | 登录账号 | ✅ Devops-senao |
| 3 | 创建仓库 | ✅ my-first-repo |
| 4 | 修改 README | ✅ 完成 |
| 5 | 上传 HTML 网页 | ✅ index.html |
| 6 | 上传 Python 程序 | ✅ quote.py |
| 7 | Fork 项目 | ✅ awesome |
| 8 | 点 Star | ✅ Awesome-Chinese-LLM |
| 9 | 创建 Issue | ✅ #1 |
| 10 | 开启 GitHub Pages | ✅ 网站已上线 |

---

**你的仓库地址：** https://github.com/Devops-senao/my-first-repo
**你的个人网站：** https://devops-senao.github.io/my-first-repo/

> 🌱 从今天开始，你已经是一名 GitHub 用户了！
