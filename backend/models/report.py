from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from backend.config.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    report_type = Column(String, nullable=False)

    report_content = Column(Text, nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))