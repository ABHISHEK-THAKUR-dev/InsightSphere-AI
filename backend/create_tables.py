from backend.config.database import Base, engine

from backend.models.user import User
from backend.models.report import Report
from backend.models.document import Document
from backend.models.search_history import SearchHistory

Base.metadata.create_all(bind=engine)

print("All tables created successfully")