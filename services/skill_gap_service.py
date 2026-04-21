"""
skill_gap_service.py
====================
Compares a user's self-rated skills (from questionnaire) or resume-detected
skills against the requirements for a target career.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.career_knowledge import CAREER_SKILLS


def analyze_gap(career: str, user_skills: dict | None = None,
                resume_skills: list[str] | None = None) -> dict:
    """
    Parameters
    ----------
    career       : target career string (must exist in CAREER_SKILLS)
    user_skills  : {skill_name: current_level (1-10)} from questionnaire (optional)
    resume_skills: list of skill names detected in resume (optional)

    Returns
    -------
    {
        "career"           : str,
        "required_skills"  : {skill: min_level},
        "present_skills"   : list[str],   # skills user already has
        "missing_skills"   : list[str],   # skills user is lacking
        "gap_details"      : list[dict],  # per-skill breakdown
        "match_score"      : float,       # 0-100 percentage
    }
    """
    required = CAREER_SKILLS.get(career, {})
    if not required:
        return {"error": f"Career '{career}' not found in knowledge base."}

    # Normalise resume skills to lower for comparison
    resume_lower = {s.lower() for s in (resume_skills or [])}

    present   = []
    missing   = []
    gap_details = []

    for skill, min_level in required.items():
        skill_lower = skill.lower()

        # Check questionnaire rating
        questionnaire_level = None
        if user_skills:
            for k, v in user_skills.items():
                if k.lower() in skill_lower or skill_lower in k.lower():
                    questionnaire_level = int(v)
                    break

        # Check resume presence
        in_resume = any(
            skill_lower in r or r in skill_lower
            for r in resume_lower
        )

        # Determine status
        if questionnaire_level is not None:
            has_skill   = questionnaire_level >= min_level
            current_lvl = questionnaire_level
        elif in_resume:
            has_skill   = True
            current_lvl = min_level  # assume meets minimum if listed on resume
        else:
            has_skill   = False
            current_lvl = 0

        status = "Present" if has_skill else "Missing"

        if has_skill:
            present.append(skill)
        else:
            missing.append(skill)

        gap_details.append({
            "skill"        : skill,
            "required_level": min_level,
            "current_level" : current_lvl,
            "status"        : status,
            "gap"           : max(0, min_level - current_lvl),
        })

    total       = len(required)
    match_score = round((len(present) / total) * 100, 1) if total else 0

    return {
        "career"          : career,
        "required_skills" : required,
        "present_skills"  : present,
        "missing_skills"  : missing,
        "gap_details"     : gap_details,
        "match_score"     : match_score,
    }
