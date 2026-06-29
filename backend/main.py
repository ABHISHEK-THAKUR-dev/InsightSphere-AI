from fastapi import FastAPI

from backend.routes.auth import router as auth_router
from backend.routes.research import router as research_router
from backend.routes.document import router as document_router
from backend.routes.comparison import router as comparison_router
from backend.routes.report import router as report_router

app = FastAPI(
    title="InsightSphere AI",
    description="AI Research, Analysis & Decision Intelligence Platform",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(research_router)
app.include_router(document_router)
app.include_router(comparison_router)
app.include_router(report_router)
@app.get("/")
def root():
    return {
        "message": "InsightSphere AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }