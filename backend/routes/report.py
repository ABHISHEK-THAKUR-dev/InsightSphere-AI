from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import SessionLocal
from backend.models.report import Report
from backend.schemas.report import ReportCreate

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_report(
    report: ReportCreate,
    db: Session = Depends(get_db)
):

    new_report = Report(
        user_id=report.user_id,
        title=report.title,
        report_type=report.report_type,
        report_content=report.report_content
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return {
        "message": "Report saved successfully",
        "report_id": new_report.id
    }