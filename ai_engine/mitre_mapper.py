"""
Sentinel DNA

MITRE ATT&CK Mapper

Maps AI threat classifications to
MITRE ATT&CK techniques.
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

from ai_engine.threat_classifier import classify_threat


# =====================================
# MITRE DATABASE
# =====================================

MITRE_MAPPING = {

    "Credential Phishing": {
        "technique_id": "T1566.002",
        "technique": "Phishing: Spearphishing Link",
        "tactic": "Initial Access"
    },

    "Malware": {
        "technique_id": "T1204",
        "technique": "User Execution",
        "tactic": "Execution"
    },

    "Ransomware": {
        "technique_id": "T1486",
        "technique": "Data Encrypted for Impact",
        "tactic": "Impact"
    },

    "Data Exfiltration": {
        "technique_id": "T1567",
        "technique": "Exfiltration Over Web Service",
        "tactic": "Exfiltration"
    },

    "Privilege Escalation": {
        "technique_id": "T1068",
        "technique": "Exploitation for Privilege Escalation",
        "tactic": "Privilege Escalation"
    },

    "Command and Control": {
        "technique_id": "T1071",
        "technique": "Application Layer Protocol",
        "tactic": "Command and Control"
    },

    "Insider Threat": {
        "technique_id": "T1078",
        "technique": "Valid Accounts",
        "tactic": "Defense Evasion"
    },

    "Unknown Threat": {
        "technique_id": "N/A",
        "technique": "No mapping available",
        "tactic": "Unknown"
    }
}


# =====================================
# MITRE MAPPER
# =====================================

def map_to_mitre(case_id):

    classification = classify_threat(case_id)

    if not classification:
        return None

    threat = classification["classification"]

    mitre = MITRE_MAPPING.get(
        threat,
        MITRE_MAPPING["Unknown Threat"]
    )

    return {

        "case_id": classification["case_id"],

        "title": classification["title"],

        "severity": classification["severity"],

        "threat": threat,

        "confidence": classification["confidence"],

        "technique_id": mitre["technique_id"],

        "technique": mitre["technique"],

        "tactic": mitre["tactic"]

    }


# =====================================
# REPORT
# =====================================

def print_report(report):

    print("=" * 60)
    print("🧬 SENTINEL DNA MITRE ATT&CK MAPPER")
    print("=" * 60)

    print(f"Case ID        : {report['case_id']}")
    print(f"Title          : {report['title']}")
    print(f"Severity       : {report['severity']}")

    print()

    print("Threat Classification")
    print("-" * 60)
    print(report["threat"])

    print()

    print("MITRE ATT&CK")
    print("-" * 60)
    print(f"Technique ID   : {report['technique_id']}")
    print(f"Technique      : {report['technique']}")
    print(f"Tactic         : {report['tactic']}")

    print()

    print(f"Confidence     : {report['confidence']}")

    print("=" * 60)


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("🧬 SENTINEL DNA MITRE ATT&CK MAPPER")
    print("=" * 60)

    case_id = input("\nEnter Case ID: ").strip()

    report = map_to_mitre(case_id)

    if report is None:
        print("\n❌ Case not found.")
    else:
        print()
        print_report(report)