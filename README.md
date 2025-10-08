# Pravāha: Where IT Flows Intelligently

Pravāha is a modular agentic AI system for Managed Service Providers (MSPs), designed to automate ticket triage, assist technicians, track time, and visualize service performance — all with intelligent orchestration.

## 🔧 Features

- 🤖 Triage Agent: Classifies and routes tickets using GPT or fine-tuned models
- 💬 Assistant Agent: Suggests resolutions and technician replies
- ⏱️ Time Tracker Agent: Logs technician effort contextually
- 📊 Dashboard: Visualizes KPIs, feedback trends, and retraining readiness
- 📣 Slack Integration: Sends agent summaries and captures technician feedback
- 🔁 Learning Loop: Fine-tunes classifier from historical tickets and feedback

## 🧱 Architecture

- `pravaha-api`: FastAPI microservice with LangChain orchestration
- `pravaha-dashboard`: Streamlit dashboard for KPIs and feedback analytics
- Firestore: Shared state and ticket history
- Slack: Notification + feedback loop
- CI/CD: GitHub Actions + Google Cloud Run

## 🚀 Getting Started

1. Clone the repo  
2. Set up Google Cloud project and Firestore  
3. Add secrets to Secret Manager  
4. Deploy via GitHub Actions  
5. Trigger workflows via API or Slack

## 📂 Repo Structure

See [docs/folder-structure.md](docs/folder-structure.md) for full breakdown.

## 🧠 Roadmap

- [x] Modular agent orchestration  
- [x] Slack feedback loop  
- [x] Firestore-based learning  
- [ ] Auto-retraining pipeline  
- [ ] Voice interface for technicians

## 📄 License

Apache-2.0 license