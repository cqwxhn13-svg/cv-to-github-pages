from fastapi import APIRouter, UploadFile, File, HTTPException
from services.pdf_extractor import extract_from_pdf, extract_from_docx
from services.ai_parser import parse_resume

router = APIRouter()


@router.post("/")
async def upload_and_parse(file: UploadFile = File(...)):
    """
    接收上传的简历文件（PDF 或 Word）
    1. 提取文字
    2. 调用 AI 结构化解析
    3. 返回结构化 JSON
    """
    content = await file.read()

    # 根据文件类型选择提取方式
    if file.filename.endswith(".pdf"):
        raw_text = extract_from_pdf(content)
    elif file.filename.endswith(".docx"):
        raw_text = extract_from_docx(content)
    else:
        raise HTTPException(status_code=400, detail="仅支持 PDF 和 Word(.docx) 格式")

    # 调用 AI 解析为结构化数据
    structured = parse_resume(raw_text)
    return structured