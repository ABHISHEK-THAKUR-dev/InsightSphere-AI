from pydantic import BaseModel


class SearchHistoryCreate(BaseModel):
    user_id: int
    query: str
    ai_response: str