"""
Sentinel DNA
Investigation Pipeline

End-to-end investigation workflow.

Flow:
Email
    ↓
Email Analysis
    ↓
Case Creation
    ↓
Evidence Storage
    ↓
Timeline
    ↓
Analyst Assignment
"""

from datetime import datetime
import uuid

from evidence_engine.email_analyzer import analyze_email

from database.repository import (
    create_case,
    add_evidence_record,
    assign_analyst
)

from cases.timeline import add_timeline_event


DEFAULT_ANALYST = "SOC ANALYST"


# =====================================
# GENERATE CASE ID
# =====================================

def generate_case_id():
    return (
        "INC-"
        + datetime.now().strftime("%Y%m%d")
        + "-"
        + uuid.uuid4().hex[:6].upper()
    )


# =====================================
# INVESTIGATE EMAIL
# =====================================

def investigate_email(
    subject,
    sender,
    body
):
    """
    Complete Sentinel DNA investigation.
    """

    # ---------------------------------
    # Analyze Email
    # ---------------------------------

    analysis = analyze_email(
        subject,
        sender,
        body
    )

    # ---------------------------------
    # Create Case
    # ---------------------------------

    case_id = generate_case_id()

    create_case({

        "case_id": case_id,

        "title": "Email Investigation",

        "severity": analysis["risk"],

        "description":
            f"Email investigation from {sender}"

    })

    # ---------------------------------
    # Assign Analyst
    # ---------------------------------

    assign_analyst(
        case_id,
        DEFAULT_ANALYST
    )

    # ---------------------------------
    # Timeline
    # ---------------------------------

    add_timeline_event(

        case_id,

        "ALERT",

        "Email received for investigation",

        "SYSTEM"

    )

    # ---------------------------------
    # Save Evidence
    # ---------------------------------

    evidence_saved = 0

    for item in analysis["evidence"]:

        add_evidence_record(

            case_id,

            item["type"].upper(),

            item["value"]

        )

        evidence_saved += 1

    # ---------------------------------
    # Timeline
    # ---------------------------------

    add_timeline_event(

        case_id,

        "EVIDENCE",

        f"{evidence_saved} evidence items collected",

        "AI ENGINE"

    )

    add_timeline_event(

        case_id,

        "ASSIGNMENT",

        f"Assigned to {DEFAULT_ANALYST}",

        "SYSTEM"

    )

    # ---------------------------------
    # Investigation Summary
    # ---------------------------------

    return {

        "case_id": case_id,

        "risk": analysis["risk"],

        "score": analysis["score"],

        "analyst": DEFAULT_ANALYST,

        "status": "OPEN",

        "evidence_count": evidence_saved,

        "timeline_events": 3,

        "analysis": analysis

    }


# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":

    report = investigate_email(

        subject="URGENT: Verify your account",

        sender="security@micr0soft-login.xyz",

        body="""
Your Microsoft account has been suspended.

Click here immediately:

https://micr0soft-login.xyz/verify

Verify your password now.
"""

    )

    print()

    print("🧬 SENTINEL DNA INVESTIGATION")

    print("=" * 50)

    for key, value in report.items():

        print(f"{key}: {value}")