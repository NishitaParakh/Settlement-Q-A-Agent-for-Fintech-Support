def calc_confidence(data):
    gateway = data["gateway"]
    bank = data["bank"]
    ledger = data["ledger"]
    settlement = data["settlement"]

    confidence = 100
    exceptions = []

    if not gateway:
        confidence -= 40
        exceptions.append("Gateway Record is Missing")

    if not bank:
        confidence -= 25
        exceptions.append("Bank Record is Missing")

    if not ledger:
        confidence -= 25
        exceptions.append("Ledger Record is Missing")

    if not settlement:
        confidence -= 10
        exceptions.append("Settlement Record is Missing")

    if gateway and gateway[0]["status"] == "FAILED":
        confidence -= 30
        exceptions.append("Gateway transaction failed")

    if bank and ledger:
        bank_status = bank[0]["status"]
        ledger_status = ledger[0]["status"]
        if (bank_status != ledger_status):
            confidence -= 20
            exceptions.append(
                f"Status conflict: Bank={bank_status}, Ledger={ledger_status}"
                )

    if gateway and ledger:
            gateway_amount = gateway[0]["amount"]
            ledger_amount = ledger[0]["amount"]
            if (gateway_amount != ledger_amount):
                confidence -= 20
                exceptions.append(
                    f"Amount mismatch: Gateway={gateway_amount}, Ledger={ledger_amount}"
                    )

    if settlement:
        settlement_status = settlement[0]["status"]

        if settlement_status == "FAILED":
            confidence -= 30
            exceptions.append("Settlement failed")

        elif settlement_status == "PENDING":
            confidence -= 20
            exceptions.append("Settlement is still pending")

    confidence = max(0, confidence)

    if confidence >= 89:
        level = "HIGH"
    elif confidence >= 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": confidence,
        "level": level,
        "exceptions": exceptions
    }



