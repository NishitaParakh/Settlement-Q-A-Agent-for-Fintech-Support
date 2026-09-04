from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.investigate import router as investigate_router
from routes.search import router as search_router

app = FastAPI(
    title="SETTLEVITTA API",
    description="Settlement investigation and transaction search API",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Existing routes
app.include_router(investigate_router)
app.include_router(search_router)


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
