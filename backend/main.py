from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from logic.tracer import find_transaction
from logic.diagnosis import diagnose
from logic.confidence import calc_confidence
from logic.recommendations import recommend_action

app = FastAPI(title="Settlement Q&A Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Settlement Q&A Agent is running"}


@app.get("/investigate/{transaction_id}")
def investigate(transaction_id: str):

    data = find_transaction(transaction_id)

    diagnosis = diagnose(data)

    confidence = calc_confidence(data)

    action = recommend_action(confidence)

    return {
        "transaction_id": transaction_id,
        "diagnosis": diagnosis,
        "confidence": confidence,
        "recommended_action": action,
        "evidence": data
    }