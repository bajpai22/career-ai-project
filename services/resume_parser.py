"""
resume_parser.py
================
Extracts plain text from a PDF resume, then identifies skills
present in the text using the central skill keyword list.
"""

import re
import io
import sys
import os

# ── Graceful import of PyPDF2 ─────────────────────────────────────────────────
try:
    import PyPDF2
    _PYPDF2_AVAILABLE = True
except ImportError:
    _PYPDF2_AVAILABLE = False

# Add project root to path so utils can be found from any entry point
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.career_knowledge import SKILL_KEYWORDS


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Given raw PDF bytes, return the extracted plain text.
    Falls back to an empty string if PyPDF2 is unavailable or the PDF is corrupt.
    """
    if not _PYPDF2_AVAILABLE:
        raise RuntimeError(
            "PyPDF2 is not installed. Run: pip install PyPDF2"
        )

    text_parts = []
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    except Exception as exc:
        raise ValueError(f"Could not read PDF: {exc}") from exc

    return "\n".join(text_parts)


def detect_skills(text: str) -> list[str]:
    """
    Scan text (case-insensitive) for any keyword in SKILL_KEYWORDS.
    Returns a de-duped, sorted list of matched skills.
    """
    text_lower = text.lower()
    found = set()

    for kw in SKILL_KEYWORDS:
        # Use word-boundary matching so 'r' doesn't match 'react'
        pattern = r'\b' + re.escape(kw.lower()) + r'\b'
        if re.search(pattern, text_lower):
            # Store in a normalised title-case form
            found.add(kw.title())

    return sorted(found)


def parse_resume(file_bytes: bytes) -> dict:
    """
    Full pipeline: PDF bytes → extracted text → detected skills.

    Returns
    -------
    {
        "text"         : str,        # raw extracted text
        "skills_found" : list[str],  # skills detected in the resume
        "word_count"   : int,
    }
    """
    text         = extract_text_from_pdf(file_bytes)
    skills_found = detect_skills(text)

    return {
        "text"        : text,
        "skills_found": skills_found,
        "word_count"  : len(text.split()),
    }
