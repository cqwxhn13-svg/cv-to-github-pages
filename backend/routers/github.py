from fastapi import APIRouter
import os, httpx

router = APIRouter()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")


@router.get("/auth")
def github_auth():
    """
    第一步：把用户重定向到 GitHub OAuth 授权页面
    用户在 GitHub 点击"授权"后，GitHub 会带着 code 回调到 /callback
    """
    return {
        "url": f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope=repo"
    }


@router.get("/callback")
async def github_callback(code: str):
    """
    第二步：用 code 换取 access_token
    GitHub 回调时会带上 code，用它换取真正的访问令牌
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://github.com/login/oauth/access_token",
            json={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={"Accept": "application/json"},
        )
    token_data = resp.json()
    access_token = token_data.get("access_token")
    # TODO: 用 JWT 封装 token 返回给前端，避免直接暴露
    return {"access_token": access_token}


@router.post("/deploy")
async def deploy(payload: dict):
    """
    第三步：部署到 GitHub Pages
    接收简历数据 + 模板 ID + 用户 access_token
    调用 github_deployer 服务完成部署
    返回最终的 GitHub Pages URL
    """
    # TODO: 调用 github_deployer.deploy()
    return {"status": "not implemented yet"}