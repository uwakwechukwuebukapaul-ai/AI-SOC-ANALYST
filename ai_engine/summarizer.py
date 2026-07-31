"""
Sentinel DNA

AI Investigation Summarizer

Responsible for:
- Loading investigation data
- Summarizing case information
- Counting evidence and timeline events
- Producing an analyst-friendly summary
"""

from pathlib import Path
import sys

# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# =====================================
# IMPORTS
# =====================================

from database.repository import (
    get_case,
    get_evidence,
)

from cases.timeline import get_timeline


# =====================================
# SUMMARY ENGINE
# =====================================

def generate_summary(case_id):
    """
    Generate an investigation summary.
    """

    case = get_case(case_id)

    if not case:
        return None

    evidence = get_evidence(case_id)
    timeline = get_timeline(case_id)

    evidence_count = len(evidence)
    timeline_count = len(timeline)

    severity = case.get("severity", "LOW").upper()

    # =====================================
    # BASIC AI ASSESSMENT
    # =====================================

    if severity == "CRITICAL":
        confidence = 98
    elif severity == "HIGH":
        confidence = 92
    elif severity == "MEDIUM":
        confidence = 75
    else:
        confidence = 50

    overall_assessment = (
        f"This investigation contains "
        f"{evidence_count} evidence item(s) and "
        f"{timeline_count} timeline event(s). "
        f"Based on the recorded severity, the incident "
        f"is currently assessed as {severity} priority."
    )

    return {

        "case_id": case["case_id"],

        "title": case["title"],

        "severity": severity,

        "description": case["description"],

        "evidence_count": evidence_count,

        "timeline_count": timeline_count,

        "confidence": confidence,

        "overall_assessment": overall_assessment

    }


# =====================================
# REPORT PRINTER
# =====================================

def print_summary(summary):

    print()

    print("=" * 60)

    print("🧬 SENTINEL DNA AI SUMMARY")

    print("=" * 60)

    print(f"Case ID           : {summary['case_id']}")
    print(f"Title             : {summary['title']}")
    print(f"Severity          : {summary['severity']}")
    print(f"Confidence        : {summary['confidence']}%")

    print()

    print("Description")
    print("-" * 60)
    print(summary["description"])

    print()

    print("Statistics")
    print("-" * 60)
    print(f"Evidence Items    : {summary['evidence_count']}")
    print(f"Timeline Events   : {summary['timeline_count']}")

    print()

    print("AI Assessment")
    print("-" * 60)
    print(summary["overall_assessment"])

    print()

    print("=" * 60)


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA AI INVESTIGATION SUMMARY")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    summary = generate_summary(case_id)

    if summary is None:

        print("\n❌ Case not found.")

    else:

        print_summary(summary)