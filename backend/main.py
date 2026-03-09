from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import parse, github, templates

app = FastAPI(title="cv-to-github-pages API", version="0.1.0")

# 允许前端跨域请求（开发阶段允许 localhost:3000）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由模块
app.include_router(parse.router, prefix="/api/parse", tags=["parse"])
app.include_router(github.router, prefix="/api/github", tags=["github"])
app.include_router(templates.router, prefix="/api/templates", tags=["templates"])


@app.get("/")
def root():
    return {"status": "ok", "message": "cv-to-github-pages API"}