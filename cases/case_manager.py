"""
Sentinel DNA
Case Management Engine

Responsible for:
- Creating investigations
- Generating case IDs
- Attaching evidence
- Connecting cases to database
"""

from datetime import datetime
import uuid

from database.repository import create_case



def generate_case_id():

    timestamp = datetime.now().strftime(
        "%Y%m%d"
    )

    unique = str(uuid.uuid4())[:6].upper()

    return f"INC-{timestamp}-{unique}"



def create_investigation(
        title,
        severity,
        description,
        evidence=None
):

    case_id = generate_case_id()


    case = {

        "case_id": case_id,

        "title": title,

        "severity": severity,

        "description": description

    }


    # Save case into database

    create_case(case)


    investigation = {

        "case_id": case_id,

        "title": title,

        "severity": severity,

        "description": description,

        "evidence": evidence or [],

        "status": "OPEN",

        "created":
            datetime.now().isoformat()

    }


    return investigation



if __name__ == "__main__":


    test = create_investigation(

        title="Phishing Attack Investigation",

        severity="HIGH",

        description=
        "Suspicious credential harvesting email detected",

        evidence=[

            {
                "type":"url",
                "value":
                "https://fake-login.xyz"
            }

        ]

    )


    print("🧬 SENTINEL DNA CASE CREATED")

    print("="*40)

    print(test)