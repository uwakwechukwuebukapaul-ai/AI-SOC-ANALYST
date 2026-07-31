"""
Sentinel DNA

Analyst Actions
"""


from datetime import datetime



def record_action(
        case,
        action,
        analyst
):


    event = {

        "action": action,

        "analyst": analyst,

        "time":
            datetime.now().isoformat()

    }


    if "actions" not in case:

        case["actions"] = []


    case["actions"].append(
        event
    )


    return event