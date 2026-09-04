def create_prompt(data, diagnosis, confidence, action):

    prompt = f"""
You are a FinTech settlement support assistant.

Analyze only the verified transaction information provided below.

Transaction ID:
{data["transaction_id"]}

Gateway:
{data["gateway"]}

Bank:
{data["bank"]}

Ledger:
{data["ledger"]}

Settlement:
{data["settlement"]}

Diagnosis:
{diagnosis}

Confidence:
{confidence["score"]}% ({confidence["level"]})

Exceptions:
{confidence["exceptions"]}

Recommended Action:
{action}

Explain the transaction in simple English.

Include:
1. What happened
2. Where the issue occurred
3. Why it happened
4. What the support agent should do next

Do not invent information.
If the records conflict or information is missing, clearly say that the result is uncertain.
"""

    return prompt
if __name__ == "__main__":
    test_data = {
        "transaction_id": "TXN1005",
        "gateway": [{"amount": 3000, "status": "SUCCESS"}],
        "bank": [{"amount": 3000, "status": "SUCCESS"}],
        "ledger": [{"amount": 2900, "status": "SUCCESS"}],
        "settlement": [{"amount": 2900, "status": "PROCESSED"}]
    }

    confidence = {
        "score": 80,
        "level": "MEDIUM",
        "exceptions": [
            "Amount mismatch: Gateway=3000, Ledger=2900"
        ]
    }

    diagnosis = "Amount mismatch detected"

    action = "INVESTIGATE"

    prompt = create_prompt(test_data, diagnosis, confidence, action)

    print(prompt)