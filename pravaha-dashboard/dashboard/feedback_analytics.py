import streamlit as st
import pandas as pd
from google.cloud import firestore

def load_feedback_data():
    db = firestore.Client()
    docs = db.collection("ticket_history").stream()
    data = []
    for doc in docs:
        d = doc.to_dict()
        data.append({
            "Ticket": d.get("ticket_id"),
            "Feedback": d.get("feedback", "Unrated")
        })
    return pd.DataFrame(data)

def show_feedback_trends():
    df = load_feedback_data()
    st.subheader("🧠 Technician Feedback Trends")
    feedback_counts = df["Feedback"].value_counts()
    st.bar_chart(feedback_counts)

    correct_ratio = feedback_counts.get("Correct", 0) / len(df)
    st.metric("Retraining Readiness", f"{correct_ratio:.0%} of tickets validated")

    if correct_ratio > 0.8 and len(df) > 50:
        st.success("✅ Enough validated data for retraining!")
    else:
        st.warning("⚠️ Need more technician feedback before retraining.")