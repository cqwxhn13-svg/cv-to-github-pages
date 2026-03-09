import os
import json
import anthropic


# 告诉 AI 只返回 JSON，定义好我们需要的简历数据结构
SYSTEM_PROMPT = """你是一个专业的简历解析器。
从用户提供的简历文本中提取结构化信息，只返回如下格式的 JSON，不要包含任何其他文字：

{
  "name": "姓名",
  "email": "邮箱",
  "phone": "电话",
  "location": "所在城市",
  "summary": "个人简介",
  "experience": [
    {
      "title": "职位名称",
      "company": "公司名称",
      "duration": "在职时间，如 2023.06 - 2025.01",
      "description": "工作内容描述"
    }
  ],
  "education": [
    {
      "degree": "学位，如 硕士",
      "school": "学校名称",
      "major": "专业",
      "year": "毕业年份"
    }
  ],
  "skills": ["技能1", "技能2", "技能3"]
}"""


def parse_resume(raw_text: str) -> dict:
    """
    调用 Claude API，将简历原始文本解析为结构化 JSON
    raw_text: 从 PDF/Word 中提取的原始文字
    返回: 结构化的简历数据字典
    """
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"{SYSTEM_PROMPT}\n\n简历内容如下：\n\n{raw_text}"
            }
        ]
    )

    # 解析返回的 JSON 字符串
    result_text = message.content[0].text
    return json.loads(result_text)