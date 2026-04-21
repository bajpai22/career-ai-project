"""
api_routes.py
=============
Registers all REST API blueprints on the Flask application.
"""

from flask import Blueprint, request, jsonify
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from services.career_predictor  import predict_career
from services.resume_parser     import parse_resume
from services.skill_gap_service import analyze_gap
from services.roadmap_service   import get_roadmap

api = Blueprint("api", __name__)


# ── /predict-career ───────────────────────────────────────────────────────────
@api.route("/predict-career", methods=["POST"])
def route_predict_career():
    """
    Expects JSON body:
    {
      "programming": 8, "data_analysis": 7, "machine_learning": 9,
      "web_dev": 3, "database": 6, "cloud": 5,
      "communication": 5, "project_management": 4,
      "design": 2, "networking": 3, "cybersecurity": 2,
      "math": 8, "statistics": 7
    }
    """
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    try:
        result = predict_career(data)
        return jsonify(result), 200
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── /analyze-resume ───────────────────────────────────────────────────────────
@api.route("/analyze-resume", methods=["POST"])
def route_analyze_resume():
    """
    Expects multipart/form-data with key 'resume' (PDF file).
    """
    if "resume" not in request.files:
        return jsonify({"error": "No file with key 'resume' in request"}), 400

    file       = request.files["resume"]
    file_bytes = file.read()

    if not file_bytes:
        return jsonify({"error": "Uploaded file is empty"}), 400

    try:
        result = parse_resume(file_bytes)
        # Don't send full text to frontend — send a snippet only
        snippet = result["text"][:500] + ("…" if len(result["text"]) > 500 else "")
        return jsonify({
            "skills_found": result["skills_found"],
            "word_count"  : result["word_count"],
            "text_snippet": snippet,
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── /skill-gap ────────────────────────────────────────────────────────────────
@api.route("/skill-gap", methods=["POST"])
def route_skill_gap():
    """
    Expects JSON body:
    {
      "career"       : "Data Scientist",
      "user_skills"  : {"Python Programming": 7, ...},   // optional
      "resume_skills": ["Python", "SQL", ...]              // optional
    }
    """
    data = request.get_json(force=True)
    if not data or "career" not in data:
        return jsonify({"error": "JSON body with 'career' key required"}), 400

    try:
        result = analyze_gap(
            career       = data["career"],
            user_skills  = data.get("user_skills"),
            resume_skills= data.get("resume_skills"),
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── /roadmap ──────────────────────────────────────────────────────────────────
@api.route("/roadmap", methods=["POST"])
def route_roadmap():
    """
    Expects JSON body:
    {
      "career"        : "Web Developer",
      "missing_skills": ["React", "Docker"]   // optional
    }
    """
    data = request.get_json(force=True)
    if not data or "career" not in data:
        return jsonify({"error": "JSON body with 'career' key required"}), 400

    try:
        result = get_roadmap(
            career        = data["career"],
            missing_skills= data.get("missing_skills", []),
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── /careers (utility - list all available careers) ───────────────────────────
@api.route("/careers", methods=["GET"])
def route_list_careers():
    from utils.career_knowledge import CAREER_SKILLS
    return jsonify({"careers": sorted(CAREER_SKILLS.keys())}), 200
