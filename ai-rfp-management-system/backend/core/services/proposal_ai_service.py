import json
from openai import OpenAI

client = OpenAI()


def parse_vendor_email(email_text: str) -> dict:
    """
    Extract structured proposal data from vendor email text
    """

    prompt = f"""
You are an AI assistant helping with procurement.

Extract the following fields from the vendor response below:
- total_price
- delivery_timeline
- warranty
- payment_terms
- summary (1–2 sentence explanation)

Return ONLY valid JSON with these keys.
If a value is missing, return null.

Vendor Email:
{email_text}
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
