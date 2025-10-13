import streamlit as st
from google.cloud import firestore
import pandas as pd

st.set_page_config(page_title="Pravāha Dashboard", layout="wide")
st.title("📊 Pravāha Agentic Dashboard")

db = firestore.Client()
docs = db.collection("dashboard").stream()

# Collect ticket data
tickets = []
for doc in docs:
    data = doc.to_dict()
    tickets.append(data)

if not tickets:
    st.warning("No ticket data found.")
else:
    df = pd.DataFrame(tickets)

    # 🔹 Section 1: Ticket Flow Summary
    st.subheader("🎫 Ticket Flow Summary")
    st.metric("Total Tickets", len(df))
    st.metric("Unique Technicians", df["triage"].str.extract(r'Assigned to (\w+)')[0].nunique())
    st.metric("Avg Time Logged", f"{df['time_logged'].str.extract(r'(\d+)')[0].astype(int).mean():.1f} min")

    # 🔹 Section 2: Agent Performance
    st.subheader("👨‍💻 Technician Performance")
    tech_times = df["triage"].str.extract(r'Assigned to (\w+)')[0]
    df["minutes"] = df["time_logged"].str.extract(r'(\d+)')[0].astype(int)
    tech_summary = df.groupby(tech_times)["minutes"].sum()
    st.bar_chart(tech_summary)

    # 🔹 Section 3: Ticket History Table
    st.subheader("📋 Ticket History")
    st.dataframe(df[["ticket_id", "triage", "resolution", "time_logged", "timestamp"]])