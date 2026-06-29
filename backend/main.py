from fastapi import FastAPI
from backend.routes.auth import router as auth_router

app = FastAPI(
    title="InsightSphere AI",
    description="AI Research, Analysis & Decision Intelligence Platform",
    version="1.0.0"
)

app.include_router(auth_router)

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