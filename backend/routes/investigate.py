from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class InvestigateRequest(BaseModel):
    transaction_id: str


TRANSACTIONS = {
    "TXN1025": {
        "transaction_id": "TXN1025",

        "gateway": {
            "status": "SUCCESS",
            "amount": 1500
        },

        "bank": {
            "status": "SUCCESS",
            "amount": 1500
        },

        "ledger": {
            "status": "PENDING",
            "amount": 1500
        },

        "timeline": [
            {
                "time": "10:30 AM",
                "event": "Transaction initiated"
            },
            {
                "time": "10:31 AM",
                "event": "Gateway payment successful"
            },
            {
                "time": "10:31 AM",
                "event": "Bank payment successful"
            },
            {
                "time": "10:32 AM",
                "event": "Ledger update pending"
            }
        ]
    }
}


@router.post("/investigate")
def investigate(request: InvestigateRequest):

    transaction_id = request.transaction_id.strip().upper()

    transaction = TRANSACTIONS.get(transaction_id)

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "Transaction not found",
                "transaction_id": transaction_id
            }
        )

    gateway = transaction["gateway"]
    bank = transaction["bank"]
    ledger = transaction["ledger"]

    # Settlement diagnosis
    if ledger["status"] == "PENDING":

        settlement_status = "DELAYED"
        reason = "Ledger update is pending"
        recommended_action = "MONITOR"
        confidence = "HIGH"

    elif gateway["status"] != "SUCCESS":

        settlement_status = "FAILED"
        reason = "Gateway transaction failed"
        recommended_action = "CHECK_GATEWAY"
        confidence = "HIGH"

    elif bank["status"] != "SUCCESS":

        settlement_status = "FAILED"
        reason = "Bank transaction failed"
        recommended_action = "CHECK_BANK"
        confidence = "HIGH"

    else:

        settlement_status = "COMPLETED"
        reason = "Transaction successfully settled"
        recommended_action = "NO_ACTION"
        confidence = "HIGH"

    # Exception detection
    exceptions = []

    if gateway["amount"] != bank["amount"]:
        exceptions.append(
            "Gateway and bank amounts do not match"
        )

    if bank["amount"] != ledger["amount"]:
        exceptions.append(
            "Bank and ledger amounts do not match"
        )

    if not exceptions:
        exceptions.append(
            "No amount mismatch detected"
        )

    # Plain-English explanation
    ai_explanation = (
        f"Transaction {transaction_id} was successful "
        f"at the gateway and bank level, but the ledger "
        f"is still {ledger['status'].lower()}. "
        f"Therefore, settlement is "
        f"{settlement_status.lower()}. "
        f"Reason: {reason}."
    )

    return {
        "transaction_id": transaction_id,
        "gateway": gateway,
        "bank": bank,
        "ledger": ledger,

        "settlement": {
            "status": settlement_status,
            "reason": reason
        },

        "timeline": transaction["timeline"],

        "confidence": confidence,

        "exceptions": exceptions,

        "recommended_action": recommended_action,

        "ai_explanation": ai_explanation
    }