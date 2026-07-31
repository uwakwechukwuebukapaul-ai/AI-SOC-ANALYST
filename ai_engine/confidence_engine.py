"""
Sentinel DNA

AI Confidence Engine

Evaluates the confidence level of an investigation
based on available data.
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

from ai_engine.threat_classifier import classify_threat
from ai_engine.risk_engine import calculate_risk


# =====================================
# CONFIDENCE ENGINE
# =====================================

def calculate_confidence(case_id):

    case = get_case(case_id)

    if not case:
        return None

    evidence = get_evidence(case_id)
    timeline = get_timeline(case_id)
    threat = classify_threat(case_id)
    risk = calculate_risk(case_id)

    score = 0

    # Case exists
    score += 30

    # Evidence
    score += min(len(evidence) * 10, 20)

    # Timeline
    score += min(len(timeline) * 3, 20)

    # Threat identified
    if threat["classification"] != "Unknown Threat":
        score += 20
    else:
        score += 5

    # Rich investigation
    if len(evidence) + len(timeline) >= 5:
        score += 10

    if score > 100:
        score = 100

    if score >= 90:
        assessment = (
            "High confidence. The investigation contains "
            "sufficient evidence and activity for reliable analysis."
        )
    elif score >= 70:
        assessment = (
            "Moderate confidence. Additional evidence could improve accuracy."
        )
    else:
        assessment = (
            "Low confidence. More investigation is recommended."
        )

    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "severity": case["severity"],
        "threat": threat["classification"],
        "risk_score": risk["risk_score"],
        "confidence_score": score,
        "assessment": assessment,
        "evidence_items": len(evidence),
        "timeline_events": len(timeline),
    }


# =====================================
# REPORT
# =====================================

def print_report(report):

    print("=" * 60)
    print("🧬 SENTINEL DNA CONFIDENCE ENGINE")
    print("=" * 60)

    print(f"Case ID           : {report['case_id']}")
    print(f"Title             : {report['title']}")
    print(f"Severity          : {report['severity']}")
    print(f"Threat            : {report['threat']}")
    print(f"Risk Score        : {report['risk_score']} / 100")

    print()

    print("Investigation Metrics")
    print("-" * 60)
    print(f"Evidence Items    : {report['evidence_items']}")
    print(f"Timeline Events   : {report['timeline_events']}")

    print()

    print("Confidence")
    print("-" * 60)
    print(f"Confidence Score  : {report['confidence_score']}%")
    print(report["assessment"])

    print("=" * 60)


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA CONFIDENCE ENGINE")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    report = calculate_confidence(case_id)

    if report is None:
        print("\n❌ Case not found.")
    else:
        print()
        print_report(report)