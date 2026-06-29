from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.config.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    filename = Column(String, nullable=False)

    upload_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))