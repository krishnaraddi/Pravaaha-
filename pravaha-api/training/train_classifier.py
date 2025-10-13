import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# ✅ Load ticket data
def load_data(csv_path="tickets.csv"):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    df = pd.read_csv(csv_path)
    if "text" not in df.columns or "classification" not in df.columns:
        raise ValueError("CSV must contain 'text' and 'classification' columns")
    return df

# ✅ Train classifier
def train_model(df):
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    model.fit(df["text"], df["classification"])
    return model

# ✅ Save model
def save_model(model, path="triage_model.pkl"):
    joblib.dump(model, path)
    print(f"✅ Model saved to {path}")

# ✅ Main entry point
if __name__ == "__main__":
    print("🚀 Training ticket classifier...")
    df = load_data()
    model = train_model(df)
    save_model(model)