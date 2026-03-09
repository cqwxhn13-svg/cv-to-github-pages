# cv-to-github-pages

<div align="center">

**🇨🇳 中文** | **🇬🇧 English**

Upload your resume → AI parses it → Pick a template → Deploy to GitHub Pages in one click.

上传简历 → AI 解析 → 选择模板 → 一键部署到 GitHub Pages

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-green.svg)
![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)
![Status](https://img.shields.io/badge/status-WIP-orange.svg)

</div>

---

## ✨ What it does / 它做什么

Most resume tools stop at exporting a PDF. This tool goes one step further — it turns your resume into a **live personal website hosted on GitHub Pages**, with a real URL you can share anywhere.

大多数简历工具到导出 PDF 就结束了。这个工具更进一步——将你的简历变成一个**托管在 GitHub Pages 上的个人网站**，拥有真实 URL，随时分享。

```
📄 Upload PDF / Word resume
        ↓
🤖 AI extracts structured data (name, experience, skills, education...)
        ↓
🎨 Choose a resume page template
        ↓
🔑 Authorize GitHub (OAuth — just click, no config needed)
        ↓
🚀 Auto-create repo → push → enable Pages → done!
        ↓
🌐 yourusername.github.io/resume
```

---

## 🎯 Features / 功能

- **AI-powered parsing** — Upload PDF/Word, AI extracts all key info automatically / 上传 PDF/Word，AI 自动提取所有关键信息
- **Zero config for users** — No Git, no YAML, no terminal needed / 用户无需 Git、YAML、命令行，开箱即用
- **GitHub OAuth** — Secure one-click authorization, no password stored / 一键安全授权，不存储用户密码
- **Multiple templates** — Pick the style that fits you / 多套模板可选
- **One-click update** — Re-upload resume to refresh your page / 重新上传即可更新页面

---

## 🚀 For Users / 普通用户使用方法

> 直接访问线上地址即可，无需任何配置。
> Just open the website — no setup needed.

1. 打开网址（部署后填入）/ Open the website (URL coming soon)
2. 上传你的简历 PDF 或 Word 文件 / Upload your resume PDF or Word file
3. 预览 AI 解析结果，选择喜欢的模板 / Preview parsed info, choose a template
4. 点击"授权 GitHub"，跳转 GitHub 点击允许 / Click "Authorize GitHub", approve on GitHub
5. 一键部署，获得你的专属链接 🎉 / Deploy in one click and get your personal URL 🎉

---

## 🛠️ Tech Stack / 技术栈

| Layer | Tech |
|---|---|
| Frontend | Next.js 14 + Tailwind CSS |
| Backend | FastAPI (Python 3.11+) |
| AI Parsing | Claude API |
| PDF Extract | pdfplumber |
| GitHub Deploy | GitHub REST API (PyGithub) |
| Frontend Deploy | Vercel |
| Backend Deploy | Railway |

---

## 💻 For Developers / 开发者本地运行

> 以下内容面向想在本地运行或二次开发本项目的开发者。
> The following is for developers who want to run or contribute to this project locally.

### Prerequisites / 前置要求

- Python 3.11+
- Node.js 18+
- 一个 Anthropic 账号（用于 AI 解析）/ An Anthropic account (for AI parsing)
- 一个 GitHub OAuth App（用于授权部署）/ A GitHub OAuth App (for deploy authorization)

### Step 1 — 申请必要的密钥 / Get required credentials

**Anthropic API Key**

1. 注册并登录 [https://console.anthropic.com](https://console.anthropic.com)
2. 左侧菜单 → **API Keys** → **Create Key**
3. 复制生成的 key（只显示一次）/ Copy the key (shown only once)

**GitHub OAuth App**

1. GitHub 右上角头像 → **Settings** → **Developer settings** → **OAuth Apps** → **New OAuth App**
2. 填写以下信息 / Fill in:
   - Application name: `cv-to-github-pages`
   - Homepage URL: `http://localhost:3000`
   - Authorization callback URL: `http://localhost:8000/api/github/callback`
3. 点击 **Register application**
4. 记录 `Client ID`，并点击 **Generate a new client secret** 获取 `Client Secret`

### Step 2 — 配置环境变量 / Configure environment variables

```bash
cd backend
cp .env.example .env
```

编辑 `.env` 填入真实值 / Edit `.env` with your real credentials:

```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxx
GITHUB_CLIENT_ID=Ov23lixxxxxx
GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxx
SECRET_KEY=用下面命令生成 / generate with command below
FRONTEND_URL=http://localhost:3000
```

生成 `SECRET_KEY` / Generate `SECRET_KEY`:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

> ⚠️ `.env` 包含真实密钥，永远不要提交到 Git！/ Never commit `.env` to Git!

### Step 3 — 启动后端 / Start backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

后端运行在 [http://localhost:8000](http://localhost:8000)

### Step 4 — 启动前端 / Start frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

前端运行在 [http://localhost:3000](http://localhost:3000)

---

## 📁 Project Structure / 项目结构

```
cv-to-github-pages/
├── frontend/                  # Next.js 前端
│   └── src/
│       ├── components/        # UI 组件
│       ├── pages/             # 页面路由
│       └── lib/               # API 客户端、工具函数
├── backend/                   # FastAPI 后端
│   ├── main.py                # 应用入口
│   ├── requirements.txt       # Python 依赖
│   ├── .env.example           # 环境变量模板（可提交）
│   ├── routers/
│   │   ├── parse.py           # 简历上传与解析接口
│   │   ├── github.py          # GitHub OAuth + 部署接口
│   │   └── templates.py       # 模板列表接口
│   ├── services/
│   │   ├── ai_parser.py       # Claude AI 结构化解析
│   │   ├── pdf_extractor.py   # PDF/Word 文字提取
│   │   └── github_deployer.py # GitHub Pages 自动部署
│   └── templates/             # 简历 HTML 模板文件
└── docs/
    └── architecture.md
```

---

## 🗺️ Roadmap / 开发计划

- [x] Project setup / 项目初始化
- [ ] PDF text extraction / PDF 文字提取
- [ ] AI structured parsing / AI 结构化解析
- [ ] Resume HTML template v1 / 简历 HTML 模板 v1
- [ ] GitHub OAuth integration / GitHub OAuth 接入
- [ ] Auto-deploy to GitHub Pages / 自动部署到 GitHub Pages
- [ ] Frontend UI / 前端界面
- [ ] Multiple templates / 多模板支持
- [ ] Custom domain guide / 自定义域名引导

---

## 🤝 Contributing / 贡献

PRs and issues are welcome! / 欢迎提 PR 和 Issue

---

## 📄 License

MIT