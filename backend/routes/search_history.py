from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import SessionLocal
from backend.models.search_history import SearchHistory
from backend.schemas.search_history import SearchHistoryCreate

router = APIRouter(
    prefix="/history",
    tags=["Search History"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_history(
    history: SearchHistoryCreate,
    db: Session = Depends(get_db)
):

    new_history = SearchHistory(
        user_id=history.user_id,
        query=history.query,
        ai_response=history.ai_response
    )

    db.add(new_history)
    db.commit()
    db.refresh(new_history)

    return {
        "message": "History saved successfully",
        "history_id": new_history.id
    }


@router.get("/")
def get_history(
    db: Session = Depends(get_db)
):

    return db.query(SearchHistory).all()


@router.delete("/{history_id}")
def delete_history(
    history_id: int,
    db: Session = Depends(get_db)
):

    history = db.query(SearchHistory).filter(
        SearchHistory.id == history_id
    ).first()

    if not history:
        return {
            "message": "History not found"
        }

    db.delete(history)
    db.commit()

    return {
        "message": "History deleted successfully"
    }