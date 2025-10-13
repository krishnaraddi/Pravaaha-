from google.cloud import firestore
from datetime import datetime

def update_dashboard(ticket_id, triage, resolution, time_logged):
    db = firestore.Client()

    doc = {
        "ticket_id": ticket_id,
        "triage": triage,
        "resolution": resolution,
        "time_logged": time_logged,
        "timestamp": datetime.now().isoformat()
    }

    try:
        db.collection("dashboard").document(ticket_id).set(doc)
        return "Dashboard updated in Firestore."
    except Exception as e:
        return f"Firestore update failed: {str(e)}"