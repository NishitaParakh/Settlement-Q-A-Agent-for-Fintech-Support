from fastapi import FastAPI
from routes.investigate import router as investigate_router

app = FastAPI(
    title="SETTLEVITTA API",
    description="Settlement investigation and transaction tracing API",
    version="1.0.0"
)

app.include_router(investigate_router)


@app.get("/")
def home():
    return {
        "message": "SETTLEVITTA backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }