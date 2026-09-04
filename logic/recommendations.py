def recommend_action(confidence_result):
    score = confidence_result["score"]
    exceptions = confidence_result["exceptions"]

    if score >= 89 and not exceptions:
        return {
            "action": "MONITOR",
            "reason": "All systems are consistent and no exceptions were detected."
        }

    if score < 50:
        return {
            "action": "ESCALATE",
            "reason": "The transaction has serious inconsistencies or failures."
        }

    if any("missing" in e.lower() for e in exceptions):
        return {
            "action": "ESCALATE",
            "reason": "Required transaction records are missing."
        }

    if any("conflict" in e.lower() or "mismatch" in e.lower() for e in exceptions):
        return {
            "action": "INVESTIGATE",
            "reason": "Conflicting or mismatched records need investigation."
        }

    return {
        "action": "INVESTIGATE",
        "reason": "The transaction is not fully settled yet."
    }
