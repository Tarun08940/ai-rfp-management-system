import json
from openai import OpenAI

client = OpenAI()


def generate_structured_rfp(user_input: str) -> dict:
    """
    Convert natural language procurement request into structured RFP JSON
    """

    prompt = f"""
You are an AI assistant helping with procurement.

Convert the following request into structured JSON with these fields:
- title
- budget
- delivery_deadline (ISO date if possible)
- payment_terms
- warranty_requirement
- items (list with name, quantity, specifications)

Only return valid JSON. No explanations.

Request:
{user_input}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You output strictly valid JSON."},
            {"role": "user", "content": prompt},
        ],
    )

    content = response.choices[0].message.content

    return json.loads(content)
