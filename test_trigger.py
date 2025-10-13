import requests

# Local FastAPI server
API_URL = "http://localhost:8080/run"

# Sample ticket payload
payload = {
    "ticket_id": "TKT-2025-001",
    "description": "User cannot connect to VPN from home"
}

response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    print("✅ Workflow executed successfully")
    print("Result:\n", response.json()["workflow_result"])
else:
    print(f"❌ Error {response.status_code}: {response.text}")