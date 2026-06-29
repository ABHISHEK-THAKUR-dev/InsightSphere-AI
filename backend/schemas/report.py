from pydantic import BaseModel


class ReportCreate(BaseModel):
    user_id: int
    title: str
    report_type: str
    report_content: str