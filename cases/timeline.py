"""
Sentinel DNA

Investigation Timeline Engine

Tracks:
- Alert events
- Evidence collection
- Analyst actions
- Response activities
- Case history
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

    sys.path.append(
        str(PROJECT_ROOT)
    )



from database.connection import database
from database.repository import create_case




# =====================================
# GENERATE EVENT ID
# =====================================

def generate_event_id():

    return (
        "EVT-"
        + str(uuid.uuid4())[:8].upper()
    )





# =====================================
# ADD TIMELINE EVENT
# =====================================

def add_timeline_event(
        case_id,
        event_type,
        description,
        actor="SYSTEM"
):


    event = {


        "event_id":

            generate_event_id(),


        "case_id":

            case_id,


        "type":

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
                event,
                actor,
                created
            )

            VALUES (?,?,?,?)
            """,

            (

                case_id,

                description,

                actor,

                event["timestamp"]

            )

        )



    return event






# =====================================
# GET TIMELINE
# =====================================

def get_timeline(case_id):


    with database.session() as conn:


        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT *

            FROM timeline

            WHERE case_id=?

            ORDER BY id ASC

            """,

            (

                case_id,

            )

        )



        return [

            dict(row)

            for row in cursor.fetchall()

        ]






# =====================================
# TEST MODE
# =====================================

if __name__ == "__main__":


    print(
        "🧬 SENTINEL DNA TIMELINE TEST"
    )

    print("=" * 40)



    test_case_id = (

        "INC-20260731-TEST"

    )



    # Create case first
    # Required because timeline
    # depends on cases table


    try:


        create_case({

            "case_id":

                test_case_id,


            "title":

                "Timeline Test Investigation",


            "severity":

                "HIGH",


            "description":

                "Testing Sentinel DNA timeline engine"

        })


    except Exception:


        pass





    add_timeline_event(

        test_case_id,

        "ALERT",

        "Suspicious phishing email detected"

    )



    add_timeline_event(

        test_case_id,

        "EVIDENCE",

        "Malicious URL collected",

        "AI ENGINE"

    )



    add_timeline_event(

        test_case_id,

        "RESPONSE",

        "Blocked malicious domain",

        "SOC ANALYST"

    )





    print("\n🧬 TIMELINE EVENTS")

    print("=" * 40)



    events = get_timeline(

        test_case_id

    )



    for event in events:

        print(event)