from fastapi import APIRouter

router = APIRouter()

# 目前内置两套模板，后续可扩展
TEMPLATES = [
    {
        "id": "minimal",
        "name": "Minimal",
        "description": "简洁风格，突出内容",
        "preview": "/previews/minimal.png"
    },
    {
        "id": "modern",
        "name": "Modern",
        "description": "现代风格，视觉丰富",
        "preview": "/previews/modern.png"
    },
]


@router.get("/")
def list_templates():
    """返回所有可用模板列表"""
    return TEMPLATES