import io
import pdfplumber
import docx


def extract_from_pdf(file_bytes: bytes) -> str:
    """
    从 PDF 文件中提取纯文本
    pdfplumber 会逐页提取，最后合并成一个字符串
    """
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        pages_text = []
        for page in pdf.pages:
            text = page.extract_text()
            if text:  # 跳过空白页
                pages_text.append(text)
    return "\n".join(pages_text)


def extract_from_docx(file_bytes: bytes) -> str:
    """
    从 Word(.docx) 文件中提取纯文本
    逐段落提取，保留换行结构
    """
    doc = docx.Document(io.BytesIO(file_bytes))
    paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(paragraphs)