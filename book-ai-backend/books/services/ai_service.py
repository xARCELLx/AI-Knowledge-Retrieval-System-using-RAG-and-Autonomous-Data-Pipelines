from openai import OpenAI
from django.conf import settings

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)


def generate_summary(text):
    if not text:
        return ""

    prompt = f"""
    Summarize the following book description in 3-4 concise lines:

    {text}
    """

    response = client.chat.completions.create(
    model="openai/gpt-oss-120b:free",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=300
    
    )

    return response.choices[0].message.content.strip()