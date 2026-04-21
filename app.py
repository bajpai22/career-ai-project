"""
app.py
======
Flask application entry point.
Run with:  python app.py
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
import os

# ── Create Flask app ──────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
FRONTEND  = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND, static_url_path="")
CORS(app)  # Allow requests from the frontend (same origin in prod, different in dev)

# ── Register API blueprint ────────────────────────────────────────────────────
from routes.api_routes import api
app.register_blueprint(api, url_prefix="/api")

# ── Serve frontend pages ──────────────────────────────────────────────────────
@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    full = os.path.join(FRONTEND, path)
    if os.path.isfile(full):
        return send_from_directory(FRONTEND, path)
    # SPA fallback
    return send_from_directory(FRONTEND, "index.html")

# ── Health check ─────────────────────────────────────────────────────────────
@app.route("/health")
def health():
    return {"status": "ok", "message": "AI Career Recommendation API is running 🚀"}

if __name__ == "__main__":
    print("\n🚀  AI Career Recommendation System")
    print("   Backend : http://localhost:5000")
    print("   API     : http://localhost:5000/api/\n")
    app.run(debug=True, port=5000)
