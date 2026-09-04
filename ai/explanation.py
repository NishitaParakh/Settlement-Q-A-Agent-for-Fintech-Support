import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import os
from dotenv import load_dotenv
from groq import Groq
from prompts import create_prompt

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def generate_explanation(data, diagnosis, confidence, action):

    prompt = create_prompt(
        data,
        diagnosis,
        confidence,
        action
    )

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



