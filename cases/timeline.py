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



def generate_event_id():

    return (
        "EVT-"
        + str(uuid.uuid4())[:8].upper()
    )



def add_timeline_event(
        case,
        event_type,
        description,
        actor="SYSTEM"
):


    event = {

        "event_id":
            generate_event_id(),


        "type":
            event_type,


        "description":
            description,


        "actor":
            actor,


        "timestamp":
            datetime.now().isoformat()

    }



    if "timeline" not in case:

        case["timeline"] = []



    case["timeline"].append(
        event
    )


    return event



def get_timeline(case):

    return case.get(
        "timeline",
        []
    )



if __name__ == "__main__":


    test_case = {

        "case_id":
            "INC-20260731-TEST"

    }


    add_timeline_event(

        test_case,

        "ALERT",

        "Suspicious phishing email detected"

    )


    add_timeline_event(

        test_case,

        "EVIDENCE",

        "Malicious URL collected",

        "AI ENGINE"

    )


    add_timeline_event(

        test_case,

        "RESPONSE",

        "Blocked malicious domain",

        "SOC ANALYST"

    )


    print(
        "🧬 SENTINEL DNA TIMELINE"
    )

    print("=" * 40)


    for event in get_timeline(test_case):

        print(event)