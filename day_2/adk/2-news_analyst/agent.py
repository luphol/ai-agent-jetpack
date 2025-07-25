from google.adk.agents import Agent
from google.adk.tools import google_search

# สร้าง agent สำหรับวิเคราะห์ข่าวเศรษฐกิจด้วย Google Search Tools
root_agent = Agent(
    name="news_analyst",
    model="gemini-2.5-flash",
    description="Agent สำหรับวิเคราะห์และสรุปข่าวเศรษฐกิจ",
    instruction="""
    คุณคือผู้ช่วยวิเคราะห์ข่าวเศรษฐกิจที่ช่วยผู้ใช้เข้าใจและสรุปข่าวสำคัญ
    เมื่อมีคำถามเกี่ยวกับข่าว:
    1. ใช้เครื่องมือ google_search เพื่อดึงข่าวเศรษฐกิจล่าสุด
    2. สรุปข่าวให้กระชับและเข้าใจง่าย
    3. หากไม่สามารถดึงข่าวได้ ให้แจ้งในคำตอบ
    ตัวอย่างรูปแบบคำตอบ:
    "นี่คือสรุปข่าวเศรษฐกิจล่าสุด:
    - ข่าว 1: ...สรุป...
    - ข่าว 2: ...สรุป..."
    กรุณาตอบกลับเป็นภาษาไทยเสมอ
    """,
    tools=[google_search],
)
