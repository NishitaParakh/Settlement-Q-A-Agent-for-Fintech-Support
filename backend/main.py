
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from logic.tracer import find_transaction, load_data
from logic.diagnosis import diagnose
from logic.confidence import calc_confidence
from logic.recommendations import recommend_action


# ==========================================
# CREATE APP
# ==========================================

app = FastAPI(
    title="ClearSettle - Settlement Q&A Agent",
    version="1.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# HOME / HEALTH CHECK
# ==========================================

@app.get("/")
def home():
    return {
        "message": "ClearSettle Settlement Q&A Agent is running",
        "status": "online"
    }


# ==========================================
# INVESTIGATE ONE TRANSACTION
# ==========================================

@app.get("/investigate/{transaction_id}")
def investigate(transaction_id: str):

    transaction_id = transaction_id.strip().upper()

    data = find_transaction(transaction_id)

    diagnosis = diagnose(data)

    confidence = calc_confidence(data)

    action = recommend_action(confidence)

    return {
        "transaction_id": transaction_id,

        "diagnosis": diagnosis,

        "confidence": confidence,

        "recommended_action": action,

        "evidence": {
            "gateway": data["gateway"],
            "bank": data["bank"],
            "ledger": data["ledger"],
            "settlement": data["settlement"]
        }
    }


# ==========================================
# GET ALL TRANSACTIONS
# ==========================================

@app.get("/transactions")
def get_transactions():

    gateway, bank, ledger, settlements = load_data()

    transactions = []

    transaction_ids = gateway["transaction_id"].tolist()

    for transaction_id in transaction_ids:

        data = find_transaction(transaction_id)

        confidence = calc_confidence(data)

        action = recommend_action(confidence)

        gateway_record = (
            data["gateway"][0]
            if data["gateway"]
            else {}
        )

        bank_record = (
            data["bank"][0]
            if data["bank"]
            else {}
        )

        ledger_record = (
            data["ledger"][0]
            if data["ledger"]
            else {}
        )

        settlement_record = (
            data["settlement"][0]
            if data["settlement"]
            else {}
        )

        transactions.append({

            "transaction_id": transaction_id,

            "amount": gateway_record.get("amount"),

            "gateway_status":
                gateway_record.get(
                    "status",
                    "NOT_FOUND"
                ),

            "bank_status":
                bank_record.get(
                    "status",
                    "NOT_FOUND"
                ),

            "ledger_status":
                ledger_record.get(
                    "status",
                    "NOT_FOUND"
                ),

            "settlement_status":
                settlement_record.get(
                    "status",
                    "NOT_FOUND"
                ),

            "confidence": confidence,

            "action": action
        })

    return {
        "count": len(transactions),
        "transactions": transactions
    }


# ==========================================
# GET ALL SETTLEMENTS
# ==========================================

@app.get("/settlements")
def get_settlements():

    _, _, _, settlements = load_data()

    records = settlements.to_dict(
        orient="records"
    )

    return {
        "count": len(records),
        "settlements": records
    }


# ==========================================
# GET ALL EXCEPTIONS
# ==========================================

@app.get("/exceptions")
def get_exceptions():

    gateway, bank, ledger, settlements = load_data()

    exceptions = []

    transaction_ids = gateway["transaction_id"].tolist()

    for transaction_id in transaction_ids:

        data = find_transaction(transaction_id)

        confidence = calc_confidence(data)

        for exception in confidence["exceptions"]:

            exceptions.append({

                "transaction_id":
                    transaction_id,

                "exception":
                    exception,

                "confidence":
                    confidence["score"],

                "level":
                    confidence["level"]
            })

    return {
        "count": len(exceptions),
        "exceptions": exceptions
    }
