"""
Sentinel DNA

Investigation Timeline
"""


from datetime import datetime



def add_event(
    case,
    event
):


    timeline_event = {


        "event":

            event,


        "time":

            str(datetime.now())

    }


    case["timeline"].append(
        timeline_event
    )


    return timeline_event