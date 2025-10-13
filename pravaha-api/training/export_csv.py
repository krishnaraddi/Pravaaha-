from google.cloud import firestore
import pandas as pd

def export_tickets_to_csv(csv_path="tickets.csv"):
    db = firestore.Client()
    docs = db.collection("dashboard").stream()

    rows = []
    for doc in docs:
        data = doc.to_dict()
        rows.append({
            "text": data.get("description", ""),  # Optional: add this field to Firestore
            "classification": data.get("triage", "").split("→")[0].strip()
        })

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)
    print(f"✅ Exported {len(df)} tickets to {csv_path}")

if __name__ == "__main__":
    export_tickets_to_csv()