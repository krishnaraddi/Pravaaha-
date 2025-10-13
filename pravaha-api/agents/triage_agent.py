import openai
import os
from dotenv import load_dotenv
import joblib
model = joblib.load("triage_model.pkl")


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_model():
    model_path = "triage_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def classify_ticket(text):
    model = get_model()
    if model:
        return model.predict([text])[0]
    return "Model not available"


# Optional: few-shot examples to improve classification
EXAMPLES = [
    {"text": "User cannot access shared drive", "classification": "Network Issue"},
    {"text": "Printer not responding", "classification": "Hardware Issue"},
    {"text": "Outlook crashing on startup", "classification": "Software Issue"},
    {"text": "VPN not connecting", "classification": "Connectivity Issue"},
]

def build_prompt(ticket_text):
    prompt = "Classify the following IT support ticket into one of these categories:\n"
    prompt += "Network Issue, Hardware Issue, Software Issue, Connectivity Issue, Access Issue, Other\n\n"
    for ex in EXAMPLES:
        prompt += f"Ticket: {ex['text']}\nClassification: {ex['classification']}\n\n"
    prompt += f"Ticket: {ticket_text}\nClassification:"
    return prompt

# def classify_ticket(text):
#     prompt = build_prompt(text)
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.2,
#             max_tokens=20
#         )
#         classification = response.choices[0].message.content.strip()
#         return f"{classification} → Routed to technician"
#     except Exception as e:
#         return f"Classification failed: {str(e)}"
    

def classify_ticket(text):
    return model.predict([text])[0]
