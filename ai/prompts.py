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