def format_investigation_response(
    transaction_id,
    gateway,
    bank,
    ledger,
    settlement,
    timeline,
    confidence,
    exceptions,
    recommended_action,
    ai_explanation
):
    return {
        "transaction_id": transaction_id,
        "gateway": gateway,
        "bank": bank,
        "ledger": ledger,
        "settlement": settlement,
        "timeline": timeline,
        "confidence": confidence,
        "exceptions": exceptions,
        "recommended_action": recommended_action,
        "ai_explanation": ai_explanation
    }