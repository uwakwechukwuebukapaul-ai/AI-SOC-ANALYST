"""
Sentinel DNA

Evidence Management
"""


from datetime import datetime



def add_evidence(
    case,
    evidence_type,
    data
):


    item = {


        "type":

            evidence_type,


        "data":

            data,


        "time":

            str(datetime.now())

    }


    case["evidence"].append(
        item
    )


    return item