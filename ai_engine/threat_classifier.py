"""
Sentinel DNA

AI Threat Classifier

Responsible for:
- Classifying investigations
- Detecting likely threat type
- Assigning confidence score
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
# THREAT PATTERNS
# =====================================

THREAT_PATTERNS = {


    "Credential Phishing": [

        "phishing",
        "credential",
        "login",
        "password",
        "verify",
        "microsoft",
        "office365",
        "email",
        "account",
        "suspended"

    ],



    "Malware": [

        "malware",
        "trojan",
        "payload",
        "powershell",
        "virus",
        "exe"

    ],



    "Ransomware": [

        "ransom",
        "encrypted",
        "encryption",
        "bitcoin",
        "decrypt"

    ],



    "Data Exfiltration": [

        "exfiltration",
        "download",
        "upload",
        "ftp",
        "transfer"

    ],



    "Privilege Escalation": [

        "administrator",
        "admin",
        "privilege",
        "escalation"

    ],



    "Command and Control": [

        "c2",
        "beacon",
        "callback",
        "command",
        "control"

    ],



    "Insider Threat": [

        "employee",
        "internal",
        "insider"

    ]

}




# =====================================
# CLASSIFIER ENGINE
# =====================================


def classify_threat(case_id):


    case = get_case(case_id)


    if not case:

        return None



    evidence = get_evidence(case_id)

    timeline = get_timeline(case_id)



    text = " ".join([

        str(case.get("title", "")),

        str(case.get("description", ""))

    ]).lower()



    for item in evidence:

        text += " " + str(
            item.get("data", "")
        ).lower()



    for event in timeline:

        text += " " + str(
            event.get("description", "")
        ).lower()




    best_match = "Unknown Threat"

    highest_score = 0

    matched_keywords = []



    for threat, keywords in THREAT_PATTERNS.items():


        score = 0

        matches = []



        for keyword in keywords:


            if keyword in text:

                score += 1

                matches.append(keyword)



        if score > highest_score:

            highest_score = score

            best_match = threat

            matched_keywords = matches




    confidence_score = min(

        60 + highest_score * 10,

        99

    )




    return {


        "case_id":
            case["case_id"],


        "title":
            case["title"],


        "severity":
            case["severity"],



        # Dashboard compatible

        "threat_type":
            best_match,


        # Engine compatible

        "classification":
            best_match,



        "confidence":
            f"{confidence_score}%",



        "confidence_score":
            confidence_score,



        "matched_keywords":
            highest_score,



        "matched_terms":
            matched_keywords,



        "timeline_events":
            len(timeline),



        "evidence_items":
            len(evidence)

    }





# =====================================
# REPORT DISPLAY
# =====================================


def print_report(report):


    print("=" * 60)

    print("🧬 SENTINEL DNA THREAT CLASSIFIER")

    print("=" * 60)



    print(
        f"Case ID          : {report['case_id']}"
    )

    print(
        f"Title            : {report['title']}"
    )

    print(
        f"Severity         : {report['severity']}"
    )

    print(
        f"Threat Type      : {report['threat_type']}"
    )

    print(
        f"Confidence       : {report['confidence']}"
    )

    print(
        f"Keyword Matches  : {report['matched_keywords']}"
    )

    print(
        f"Evidence Items   : {report['evidence_items']}"
    )

    print(
        f"Timeline Events  : {report['timeline_events']}"
    )


    print("=" * 60)




# =====================================
# TEST MODE
# =====================================


if __name__ == "__main__":


    print("=" * 60)

    print("🧬 SENTINEL DNA THREAT CLASSIFIER")

    print("=" * 60)



    case_id = input(
        "\nEnter Case ID: "
    ).strip()



    report = classify_threat(case_id)



    if report is None:


        print(
            "\n❌ Case not found."
        )


    else:


        print()

        print_report(report)