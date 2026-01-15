import json
from openai import OpenAI

client = OpenAI()


def recommend_vendor(rfp_title: str, proposals: list) -> str:
    prompt = f"""
You are a procurement assistant.

RFP: {rfp_title}

Vendor proposals:
{json.dumps(proposals, indent=2)}

Based on price, delivery timeline, warranty, and payment terms,
recommend the best vendor and explain why in 2–3 sentences.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Be concise and practical."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
