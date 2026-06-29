from fastapi import APIRouter

router = APIRouter(
    prefix="/comparison",
    tags=["AI Comparison"]
)

@router.get("/")
def compare(
    option_a: str,
    option_b: str,
    option_c: str
):

    return {
        "option_a": option_a,
        "option_b": option_b,
        "option_c": option_c,
        "message": "Comparison route working"
    }