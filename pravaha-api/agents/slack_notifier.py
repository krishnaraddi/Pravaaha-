import requests
from utils.secrets import get_secret

def notify_slack(ticket_id, triage, resolution, time_logged):
    webhook_url = get_secret("SLACK_WEBHOOK_URL")

    payload = {
        "text": f"""
:robot_face: *Pravāha Agent Workflow Completed*

*Ticket ID:* `{ticket_id}`
*Classification:* {triage}
*Resolution:* {resolution}
*Time Logged:* {time_logged}

✅ Dashboard updated.
"""
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            return "Slack notification sent."
        else:
            return f"Slack error: {response.status_code}"
    except Exception as e:
        return f"Slack notification failed: {str(e)}"