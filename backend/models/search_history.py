from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime

from backend.config.database import Base


class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    query = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))