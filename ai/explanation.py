import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def generate_explanation(data, diagnosis, confidence, action):

    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        return "AI explanation unavailable because Groq API key is not configured."

    client = Groq(api_key=api_key)

    prompt = f"""
You are a FinTech settlement support assistant.

Analyze only the verified transaction information below.

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
{action["action"]}

Action Reason:
{action["reason"]}

Explain in simple English:

1. What happened
2. Where the issue occurred
3. Why it happened
4. What the support agent should do next

Do not invent information.
If records conflict or information is missing, clearly say that the result is uncertain.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a FinTech settlement support assistant. "
                    "Only use the verified transaction information provided. "
                    "Never invent missing information."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content



