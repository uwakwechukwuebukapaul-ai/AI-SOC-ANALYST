"""
Sentinel DNA

Investigation Timeline Engine

Responsible for:
- Tracking incident history
- Recording analyst actions
- Recording evidence collection
- Tracking automated responses
- Providing case timeline visibility
"""


from datetime import datetime
import uuid
import sys
from pathlib import Path


# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


from database.connection import database



# =====================================
# EVENT ID GENERATOR
# =====================================

def generate_event_id():

    return (
        "EVT-"
        + uuid.uuid4().hex[:8].upper()
    )



# =====================================
# NORMALIZE CASE ID
# =====================================

def normalize_case_id(case):

    """
    Accepts:
    - Case ID string
    - Dictionary containing case_id

    Returns:
    - Case ID string
    """

    if isinstance(case, dict):

        return case.get("case_id")


    return case




# =====================================
# ADD TIMELINE EVENT
# =====================================

def add_timeline_event(
        case_id,
        event_type,
        description,
        actor="SYSTEM"
):

    """
    Create a timeline event.

    Example:

    add_timeline_event(
        "INC-20260731-ABC123",
        "ALERT",
        "Phishing email detected",
        "AI ENGINE"
    )

    """


    case_id = normalize_case_id(case_id)


    if not case_id:

        raise ValueError(
            "Case ID is required"
        )



    event = {

        "event_id":
            generate_event_id(),

        "case_id":
            case_id,

        "event_type":
            event_type,

        "description":
            description,

        "actor":
            actor,

        "timestamp":
            datetime.now().isoformat()

    }



    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(

            """
            INSERT INTO timeline
            (
                case_id,
                event_type,
                description,
                actor,
                created
            )

            VALUES (?, ?, ?, ?, ?)

            """,

            (

                event["case_id"],

                event["event_type"],

                event["description"],

                event["actor"],

                event["timestamp"]

            )

        )



    return event





# =====================================
# GET CASE TIMELINE
# =====================================

def get_timeline(case_id):

    case_id = normalize_case_id(case_id)



    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(

            """
            SELECT *
            FROM timeline
            WHERE case_id=?

            ORDER BY id ASC

            """,

            (case_id,)

        )


        rows = cursor.fetchall()



        return [

            dict(row)

            for row in rows

        ]





# =====================================
# DELETE CASE TIMELINE
# =====================================

def delete_timeline(case_id):

    case_id = normalize_case_id(case_id)



    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(

            """
            DELETE FROM timeline
            WHERE case_id=?

            """,

            (case_id,)

        )


    return True





# =====================================
# TEST ENGINE
# =====================================

if __name__ == "__main__":


    from database.repository import create_case



    print(
        "🧬 SENTINEL DNA TIMELINE ENGINE"
    )

    print("=" * 50)



    test_case = {


        "case_id":
            "INC-20260731-TEST01",


        "title":
            "Timeline Test Investigation",


        "severity":
            "HIGH",


        "description":
            "Testing Sentinel DNA Timeline Engine"

    }




    # Create parent case

    try:

        create_case(test_case)

        print(
            "✅ Test case created"
        )


    except Exception:

        print(
            "ℹ️ Test case already exists"
        )






    # Add timeline events


    add_timeline_event(

        test_case["case_id"],

        "ALERT",

        "Suspicious phishing email detected",

        "AI ENGINE"

    )



    add_timeline_event(

        test_case["case_id"],

        "EVIDENCE",

        "Malicious URL extracted",

        "IOC ENGINE"

    )



    add_timeline_event(

        test_case["case_id"],

        "RESPONSE",

        "Domain blocked",

        "SOC ANALYST"

    )





    print("\nTIMELINE EVENTS")

    print("=" * 50)




    events = get_timeline(

        test_case["case_id"]

    )



    for event in events:

        print(event)