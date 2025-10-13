import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_resolution_suggestion(text):
    prompt = f"""Suggest a resolution for this IT support ticket:
Ticket: {text}
Resolution:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Resolution suggestion failed: {str(e)}"