from google.cloud import firestore
from datetime import datetime

db = firestore.Client(project="pravaha-project")

sample_tickets = [
    {
        "ticket_id": "TKT-001",
        "triage": "Assigned to Arjun",
        "resolution": "Restarted router and updated firmware",
        "time_logged": "15 min",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "ticket_id": "TKT-002",
        "triage": "Assigned to Meera",
        "resolution": "Replaced faulty cable",
        "time_logged": "10 min",
        "timestamp": datetime.utcnow().isoformat()
    },
    {
        "ticket_id": "TKT-003",
        "triage": "Assigned to Ravi",
        "resolution": "Cleared cache and rebooted system",
        "time_logged": "20 min",
        "timestamp": datetime.utcnow().isoformat()
    }
]

for ticket in sample_tickets:
    db.collection("pravaha-db").add(ticket)

print("✅ Sample tickets added to Firestore.")
