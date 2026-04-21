"""
career_predictor.py
===================
Loads the trained Random Forest model and label encoder,
then predicts the most suitable career given skill ratings.
"""

import pickle
import os
import numpy as np

BASE_DIR   = os.path.join(os.path.dirname(__file__), "..")
MODEL_PATH = os.path.join(BASE_DIR, "models", "career_model.pkl")
LE_PATH    = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

# Feature order must match the training dataset column order
FEATURE_ORDER = [
    "programming", "data_analysis", "machine_learning", "web_dev",
    "database", "cloud", "communication", "project_management",
    "design", "networking", "cybersecurity", "math", "statistics"
]

# ── Lazy-load model once ──────────────────────────────────────────────────────
_model = None
_le    = None

def _load_model():
    global _model, _le
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "Model not found. Please run: python train_model.py"
            )
        with open(MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
        with open(LE_PATH, "rb") as f:
            _le = pickle.load(f)


def predict_career(skill_ratings: dict) -> dict:
    """
    Parameters
    ----------
    skill_ratings : {feature_name: int (1-10)} — must include all FEATURE_ORDER keys

    Returns
    -------
    {
        "predicted_career" : str,
        "confidence"       : float,   # 0-100 %
        "top3"             : [{career, probability}],
    }
    """
    _load_model()

    # Build feature vector in the correct order (default 5 for any missing key)
    vector = np.array(
        [float(skill_ratings.get(feat, 5)) for feat in FEATURE_ORDER]
    ).reshape(1, -1)

    # Probabilities for all classes
    proba      = _model.predict_proba(vector)[0]
    top_idx    = np.argsort(proba)[::-1][:3]
    classes    = _le.classes_

    predicted  = classes[top_idx[0]]
    confidence = round(proba[top_idx[0]] * 100, 1)

    top3 = [
        {"career": classes[i], "probability": round(proba[i] * 100, 1)}
        for i in top_idx
    ]

    return {
        "predicted_career": predicted,
        "confidence"      : confidence,
        "top3"            : top3,
    }
