# Pravāha: Where IT Flows Intelligently

 Pravāha is a composable agentic AI platform designed to automate technician workflows — from ticket triage to resolution suggestions, time logging, and dashboard updates. Built with LangChain, OpenAI, and Firestore, and deployed on Google Cloud Run, Pravāha offers real-time visibility and modular orchestration.

## 🔧 Features

- `/run` API endpoint to trigger multi-agent workflows
- LangChain agents:
  - ClassifyTicket
  - SuggestResolution
  - LogTime
  - UpdateDashboard
- Firestore-native backend for ticket storage
- Streamlit dashboard for technician metrics
- CI/CD with GitHub Actions
- Secure secret management via Secret Manager

## 🚀 Architecture

- Cloud Run (API + Dashboard)
- LangChain + OpenAI agents
- Firestore (Native mode)
- Streamlit dashboard
- GitHub Actions CI/CD

## 📊 Dashboard

Visualizes:
- Total tickets
- Unique technicians
- Average time logged
- Technician performance bar chart
- Ticket history table

## 🧪 How to Use

### Trigger Workflow

```bash
curl -X POST https://pravaha-api-250841568989.asia-south1.run.app/run \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Resolve ticket #123 with technician insights"}'

Apache-2.0 license