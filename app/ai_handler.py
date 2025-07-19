# app/ai_handler.py
from datetime import datetime  # 日期时间模块 生成当前日期


def generate_structured_text(raw_text: str) -> dict:
    if not raw_text.strip():
        raw_text = "（示例）为贯彻落实公司数字化战略，我部门拟开展基础调研。"
    return {
        "标题": "关于开展数字化基础调研工作的通知",
        "主送单位": "公司各部门",
        "正文": raw_text + "\n\n请相关部门积极配合，按期反馈。",
        "发文单位": "AI 办公室",
        "发文日期": datetime.now().strftime("%Y年%m月%d日")  # 定义了日期，其他的是确定的
    }
# 可以加入：文号、抄送单位、附件、落款 等字段
# 可以做一个 schema 校验（比如用 pydantic）
