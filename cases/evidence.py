"""
Sentinel DNA

Evidence Management Engine

Handles:
- Evidence creation
- Integrity hashing
- Case attachment
- Chain of custody foundation
"""


from datetime import datetime
import hashlib
import uuid



def generate_evidence_id():

    return (
        "EVD-"
        + str(uuid.uuid4())[:8].upper()
    )



def calculate_hash(data):

    if isinstance(data, dict):

        data = str(data)


    return hashlib.sha256(
        data.encode("utf-8")
    ).hexdigest()



def add_evidence(
        case,
        evidence_type,
        data
):


    evidence_id = generate_evidence_id()


    evidence_hash = calculate_hash(
        data
    )


    item = {


        "evidence_id":

            evidence_id,


        "case_id":

            case.get(
                "case_id",
                "UNKNOWN"
            ),


        "type":

            evidence_type,


        "data":

            data,


        "sha256":

            evidence_hash,


        "collected_at":

            datetime.now().isoformat(),


        "status":

            "COLLECTED"

    }



    if "evidence" not in case:

        case["evidence"] = []



    case["evidence"].append(
        item
    )


    return item