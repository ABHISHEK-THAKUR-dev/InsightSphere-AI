from fastapi import APIRouter

from backend.services.ai_service import generate_research

router = APIRouter(
    prefix="/research",
    tags=["AI Research"]
)


@router.get("/")
def research(query: str):

    result = generate_research(query)

    return {
        "query": query,
        "analysis": result
    }