import streamlit as st
import pandas as pd
from datetime import datetime
import os
import subprocess


st.subheader("🧠 Model Accuracy & Retraining Readiness")

# Simulated metrics — replace with real logs or Firestore stats
accuracy = 0.89
last_trained = "2025-09-15"
tickets_since_last_train = 120

st.metric("Current Accuracy", f"{accuracy * 100:.1f}%")
st.metric("Tickets Since Last Training", tickets_since_last_train)
st.metric("Last Trained On", last_trained)

# Retraining threshold
if tickets_since_last_train > 100:
    st.warning("⚠️ Retraining recommended")
else:
    st.success("✅ Model is up-to-date")

# Optional: show accuracy trend
trend_data = pd.DataFrame({
    "Date": ["Aug", "Sep", "Oct"],
    "Accuracy": [0.85, 0.88, accuracy]
})
st.line_chart(trend_data.set_index("Date"))


st.subheader("🔁 Manual Retraining")

if st.button("Trigger Retraining Now"):
    with st.spinner("Retraining in progress..."):
        result = subprocess.run(["python", "training/train_classifier.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("✅ Retraining completed successfully")
        else:
            st.error("❌ Retraining failed")
            st.text(result.stderr)
#This assumes your dashboard container has access to the 
# training script and Python environment. 
# For Cloud Run, you’ll want to expose retraining as an API endpoint instead.