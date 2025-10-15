#this file exposes your LangChain-powered agentic
# # workflow as a FastAPI endpoint. It’s clean, secure, 
# and ready for Cloud Run deployment.

from fastapi import FastAPI, Request
from pydantic import BaseModel
from workflows.pravaha_workflow import run_pravaha_workflow
from training.train_classifier import train_model, load_data, save_model


app = FastAPI(
    title="Pravāha Agentic API",
    description="API to trigger agentic workflows for ticket triage, resolution, and tracking.",
    version="1.0.0"
)

class Ticket(BaseModel):
    ticket_id: str
    description: str

#@app.post("/run")
# def run_ticket_workflow(ticket: Ticket):
#     """
#     Trigger the full Pravāha agentic workflow for a given ticket.
#     """
#     result = run_pravaha_workflow(ticket.description, ticket.ticket_id)
#     return {
#         "ticket_id": ticket.ticket_id,
#         "workflow_result": result
#     }

@app.post("/run")
async def run_workflow(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "Resolve ticket #123")
    result = run_pravaha_workflow(prompt)
    return result


@app.post("/retrain")
def retrain_classifier():
    try:
        df = load_data()  # Load from tickets.csv
        model = train_model(df)
        save_model(model)
        return {"status": "success", "message": "Classifier retrained and saved."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def health_check():
    return {"status": "Pravāha API is live"}