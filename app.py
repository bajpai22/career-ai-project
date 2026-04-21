"""
app.py
======
Flask application entry point.
Run with: python app.py
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
import os

# ── Paths ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND = os.path.join(BASE_DIR, "frontend")

# ── Create Flask app ──────────────────────────────────────────────────
app = Flask(__name__, static_folder=FRONTEND, static_url_path="")
CORS(app)

# ── Register API routes ───────────────────────────────────────────────
from routes.api_routes import api
app.register_blueprint(api, url_prefix="/api")

# ── Serve frontend ────────────────────────────────────────────────────
@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    file_path = os.path.join(FRONTEND, path)

    if os.path.exists(file_path):
        return send_from_directory(FRONTEND, path)

    # fallback (important for SPA or direct routes)
    return send_from_directory(FRONTEND, "index.html")

# ── Health check ──────────────────────────────────────────────────────
@app.route("/health")
def health():
    return {
        "status": "ok",
        "message": "AI Career Recommendation API is running 🚀"
    }

# ── Run server ────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 AI Career Recommendation System")
    print("Running locally...\n")

    app.run(
        host="0.0.0.0",                          # 🔥 REQUIRED for deployment
        port=int(os.environ.get("PORT", 5000)),  # 🔥 REQUIRED for Render
        debug=False                              # 🔥 IMPORTANT (prod mode)
    )