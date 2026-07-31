"""
Sentinel DNA
Case Investigation Route

Displays complete investigation details.
"""

from pathlib import Path
import sys

from flask import render_template


# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


# =====================================
# IMPORTS
# =====================================

from database.repository import (
    get_case,
    get_evidence,
    get_notes
)

from cases.timeline import get_timeline


# AI ENGINES

try:
    from ai_engine.summarizer import generate_summary
except ImportError:

    def generate_summary(case_id):
        return {}


try:
    from ai_engine.recommendation_engine import generate_recommendations
except ImportError:

    def generate_recommendations(case_id):
        return []


try:
    from ai_engine.threat_classifier import classify_threat
except ImportError:

    def classify_threat(case_id):
        return {}


try:
    from ai_engine.confidence_engine import calculate_confidence
except ImportError:

    def calculate_confidence(case_id):
        return {}



# =====================================
# CASE VIEW
# =====================================

def case_view(case_id):

    case = get_case(case_id)


    if not case:

        return "Case not found", 404



    evidence = get_evidence(case_id)

    timeline = get_timeline(case_id)

    notes = get_notes(case_id)



    summary = generate_summary(case_id)

    recommendations = generate_recommendations(case_id)

    threat = classify_threat(case_id)

    confidence = calculate_confidence(case_id)



    return render_template(

        "case.html",

        case=case,

        evidence=evidence,

        timeline=timeline,

        notes=notes,

        summary=summary,

        recommendations=recommendations,

        threat=threat,

        confidence=confidence

    )