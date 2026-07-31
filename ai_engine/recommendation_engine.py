"""
Sentinel DNA

AI Recommendation Engine

Generates AI-driven recommendations based on
investigation data.
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
# PRIORITY ENGINE
# =====================================

def determine_priority(severity):

    severity = (severity or "").upper()

    mapping = {
        "CRITICAL": "IMMEDIATE",
        "HIGH": "HIGH",
        "MEDIUM": "MEDIUM",
        "LOW": "LOW"
    }

    return mapping.get(severity, "MEDIUM")


# =====================================
# RECOMMENDATION ENGINE
# =====================================

def generate_recommendations(case_id):

    case = get_case(case_id)

    if not case:
        return None

    evidence = get_evidence(case_id)
    timeline = get_timeline(case_id)

    severity = case.get("severity", "MEDIUM").upper()

    recommendations = []

    if severity == "CRITICAL":
        recommendations.extend([
            "Isolate affected systems immediately",
            "Block all identified indicators",
            "Notify incident response leadership",
            "Preserve forensic evidence",
            "Begin incident containment"
        ])

    elif severity == "HIGH":
        recommendations.extend([
            "Block malicious URLs and domains",
            "Reset affected user credentials",
            "Search for similar activity across the environment",
            "Monitor endpoints for additional indicators",
            "Notify the SOC team"
        ])

    elif severity == "MEDIUM":
        recommendations.extend([
            "Continue monitoring",
            "Validate suspicious activity",
            "Collect additional evidence"
        ])

    else:
        recommendations.extend([
            "Document findings",
            "Continue observation"
        ])

    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "severity": severity,
        "priority": determine_priority(severity),
        "evidence_items": len(evidence),
        "timeline_events": len(timeline),
        "recommendations": recommendations
    }


# =====================================
# DISPLAY REPORT
# =====================================

def print_report(report):

    print("=" * 60)
    print("🧬 SENTINEL DNA AI RECOMMENDATION ENGINE")
    print("=" * 60)

    print(f"Case ID         : {report['case_id']}")
    print(f"Title           : {report['title']}")
    print(f"Severity        : {report['severity']}")
    print(f"Priority        : {report['priority']}")
    print(f"Evidence Items  : {report['evidence_items']}")
    print(f"Timeline Events : {report['timeline_events']}")

    print("\nRecommended Actions")
    print("-" * 60)

    for i, action in enumerate(report["recommendations"], start=1):
        print(f"{i}. {action}")

    print("\n" + "=" * 60)


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA RECOMMENDATION ENGINE")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    report = generate_recommendations(case_id)

    if report is None:
        print("\n❌ Case not found.")
    else:
        print()
        print_report(report)