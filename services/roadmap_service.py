"""
roadmap_service.py
==================
Returns a structured learning roadmap for a given career,
optionally customised to skip topics the user already has.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.career_knowledge import ROADMAPS


def get_roadmap(career: str, missing_skills: list[str] | None = None) -> dict:
    """
    Parameters
    ----------
    career        : target career
    missing_skills: list of skills the user is currently missing (optional)
                    – if provided, highlights relevant topics

    Returns
    -------
    {
        "career"       : str,
        "phases"       : [...],   # full roadmap phases
        "highlighted"  : [str],   # topics flagged as especially relevant
        "total_duration": str,
    }
    """
    roadmap = ROADMAPS.get(career)
    if not roadmap:
        # Fallback: generic roadmap
        roadmap = [
            {"phase": "Phase 1 – Foundations", "duration": "2 months",
             "topics": ["Research the field", "Online courses (Coursera / Udemy)", "Build fundamentals"]},
            {"phase": "Phase 2 – Practice", "duration": "3 months",
             "topics": ["Hands-on projects", "Community participation", "Portfolio building"]},
            {"phase": "Phase 3 – Job Readiness", "duration": "2 months",
             "topics": ["Resume polishing", "Mock interviews", "Networking"]},
        ]

    # Highlight topics that relate to the user's missing skills
    highlighted = []
    if missing_skills:
        missing_lower = [s.lower() for s in missing_skills]
        for phase in roadmap:
            for topic in phase["topics"]:
                for ms in missing_lower:
                    # simple keyword overlap
                    if any(word in topic.lower() for word in ms.split()):
                        highlighted.append(topic)
                        break

    # Calculate total duration (rough sum)
    total_months = 0
    for phase in roadmap:
        dur = phase.get("duration", "")
        try:
            total_months += int(dur.split()[0])
        except Exception:
            pass

    return {
        "career"         : career,
        "phases"         : roadmap,
        "highlighted"    : list(dict.fromkeys(highlighted)),  # de-dup, preserve order
        "total_duration" : f"{total_months} months",
    }
