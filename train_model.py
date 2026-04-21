"""
train_model.py
==============
Trains a Random Forest classifier on career dataset and saves the model + label encoder.
Run this ONCE before starting the Flask server: python train_model.py
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import pickle
import os

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "career_data.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# ── Feature columns (must match questionnaire order) ─────────────────────────
FEATURES = [
    "programming", "data_analysis", "machine_learning", "web_dev",
    "database", "cloud", "communication", "project_management",
    "design", "networking", "cybersecurity", "math", "statistics"
]

def train():
    print("📂  Loading dataset …")
    df = pd.read_csv(DATA_PATH)
    print(f"    {len(df)} samples, columns: {list(df.columns)}")

    X = df[FEATURES].values
    y = df["career"].values

    # Encode string labels → integers
    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    print(f"\n🎯  Careers found: {list(le.classes_)}")

    # Train / test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_enc, test_size=0.2, random_state=42, stratify=y_enc
    )

    # ── Model ────────────────────────────────────────────────────────────────
    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        class_weight="balanced"
    )
    print("\n🌲  Training Random Forest …")
    clf.fit(X_train, y_train)

    # ── Evaluation ───────────────────────────────────────────────────────────
    y_pred = clf.predict(X_test)
    acc    = accuracy_score(y_test, y_pred)
    print(f"\n✅  Test Accuracy: {acc * 100:.1f}%")
    print("\n" + classification_report(y_test, y_pred, target_names=le.classes_))

    # ── Save artifacts ───────────────────────────────────────────────────────
    model_path = os.path.join(MODEL_DIR, "career_model.pkl")
    le_path    = os.path.join(MODEL_DIR, "label_encoder.pkl")

    with open(model_path, "wb") as f:
        pickle.dump(clf, f)
    with open(le_path, "wb") as f:
        pickle.dump(le, f)

    print(f"\n💾  Model saved  → {model_path}")
    print(f"💾  Encoder saved → {le_path}")
    return clf, le

if __name__ == "__main__":
    train()
