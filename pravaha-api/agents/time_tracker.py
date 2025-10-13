from datetime import datetime
import random

def log_time(ticket_text):
    # Simulate time based on keywords
    keywords = {
        "network": 45,
        "hardware": 60,
        "software": 30,
        "vpn": 40,
        "access": 25
    }

    lower_text = ticket_text.lower()
    for key, minutes in keywords.items():
        if key in lower_text:
            return f"Logged {minutes} minutes for technician Alice at {datetime.now().strftime('%H:%M')}"

    # Default fallback
    fallback = random.randint(20, 50)
    return f"Logged {fallback} minutes for technician Alice at {datetime.now().strftime('%H:%M')}"