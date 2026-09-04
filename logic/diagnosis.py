def diagnose(data):
    gateway = data["gateway"]
    bank = data["bank"]
    ledger = data["ledger"]
    settlement = data["settlement"]

    if not gateway:
        return "Gateway Record Not Found!"

    gateway_status = gateway[0]["status"]
    gateway_amount = gateway[0]["amount"]

    if gateway_status == "FAILED":
        reason = gateway[0].get("error_reason")

        if reason:
            return f"Transaction failed at gateway: {reason}"

        return "Transaction failed at gateway"

    if not bank:
        return "Bank record not found. Settlement cannot be confirmed"

    bank_status = bank[0]["status"]
    bank_amount = bank[0]["amount"]

    if bank_status == "FAILED":
        return "Transaction failed at bank"
    
    if gateway_amount != bank_amount:
        return (
            f"Amount mismatch between Gateway ({gateway_amount}) "
            f"and Bank ({bank_amount})"
        )

    if not ledger:
        return "Ledger record not found. Settlement status is uncertain"

    ledger_status = ledger[0]["status"]
    ledger_amount = ledger[0]["amount"]

    if gateway_amount != ledger_amount:
        return (
            f"Amount mismatch detected. Gateway amount: {gateway_amount}, "
            f"Ledger amount: {ledger_amount}"
        )

    if bank_status == "FAILED" and ledger_status == "SUCCESS":
        return "Conflicting records: Bank shows FAILED but Ledger shows SUCCESS"

    if ledger_status == "PENDING":
        return "Settlement is delayed because the ledger is still pending"

    if not settlement:
        return "Settlement record not found. Final status is uncertain"

    settlement_status = settlement[0]["status"]

    if settlement_status == "PROCESSED":
        return "Transaction is successfully settled"

    if settlement_status == "FAILED":
        return "Settlement failed"

    if settlement_status == "PENDING":
        return "Settlement is still pending"

    return "Unable to determine settlement status"