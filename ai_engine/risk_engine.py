"""
Sentinel DNA

AI Risk Engine

Calculates a dynamic risk score based on
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

from database.repository import get_case, get_evidence
from cases.timeline import get_timeline
from ai_engine.threat_classifier import classify_threat


# =====================================
# SCORING TABLES
# =====================================

SEVERITY_SCORE = {
    "LOW": 20,
    "MEDIUM": 40,
    "HIGH": 60,
    "CRITICAL": 80
}

THREAT_SCORE = {
    "Credential Phishing": 20,
    "Malware": 25,
    "Ransomware": 35,
    "Data Exfiltration": 30,
    "Privilege Escalation": 30,
    "Command and Control": 30,
    "Insider Threat": 25,
    "Unknown Threat": 10
}


# =====================================
# RISK LEVEL
# =====================================

def get_risk_level(score):

    if score >= 90:
        return "CRITICAL"

    if score >= 75:
        return "HIGH"

    if score >= 50:
        return "MEDIUM"

    return "LOW"


# =====================================
# RISK CALCULATION
# =====================================

def calculate_risk(case_id):

    case = get_case(case_id)

    if not case:
        return None

    evidence = get_evidence(case_id)
    timeline = get_timeline(case_id)
    classification = classify_threat(case_id)

    severity = case.get("severity", "MEDIUM").upper()

    score = SEVERITY_SCORE.get(severity, 40)

    score += len(evidence) * 5
    score += len(timeline) * 2

    threat = classification["classification"]

    score += THREAT_SCORE.get(threat, 10)

    if score > 100:
        score = 100

    return {

        "case_id": case["case_id"],

        "title": case["title"],

        "severity": severity,

        "threat": threat,

        "evidence_items": len(evidence),

        "timeline_events": len(timeline),

        "risk_score": score,

        "risk_level": get_risk_level(score),

        "confidence": classification["confidence"]

    }


# =====================================
# REPORT
# =====================================

def print_report(report):

    print("=" * 60)
    print("🧬 SENTINEL DNA RISK ENGINE")
    print("=" * 60)

    print(f"Case ID         : {report['case_id']}")
    print(f"Title           : {report['title']}")
    print(f"Severity        : {report['severity']}")
    print(f"Threat          : {report['threat']}")

    print()

    print("Investigation Metrics")
    print("-" * 60)

    print(f"Evidence Items  : {report['evidence_items']}")
    print(f"Timeline Events : {report['timeline_events']}")

    print()

    print("Risk Assessment")
    print("-" * 60)

    print(f"Risk Score      : {report['risk_score']} / 100")
    print(f"Risk Level      : {report['risk_level']}")
    print(f"Confidence      : {report['confidence']}")

    print("=" * 60)


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA RISK ENGINE")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    report = calculate_risk(case_id)

    if report is None:
        print("\n❌ Case not found.")
    else:
        print()
        print_report(report)