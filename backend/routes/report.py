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
@router.get("/")
def get_reports(
    db: Session = Depends(get_db)
):

    reports = db.query(Report).all()

    return reports
@router.get("/{report_id}")
def get_report(
    report_id: int,
    db: Session = Depends(get_db)
):

    report = db.query(Report).filter(
        Report.id == report_id
    ).first()

    if not report:
        return {
            "message": "Report not found"
        }

    return report
@router.delete("/{report_id}")
def delete_report(
    report_id: int,
    db: Session = Depends(get_db)
):

    report = db.query(Report).filter(
        Report.id == report_id
    ).first()

    if not report:
        return {
            "message": "Report not found"
        }

    db.delete(report)
    db.commit()

    return {
        "message": "Report deleted successfully"
    }