"""
Evidence Pipeline

Processes evidence through
Sentinel DNA intelligence flow.
"""


from datetime import datetime, timezone



class EvidencePipeline:


    def __init__(self):

        self.evidence = []


    def process(self, evidence):

        result = {

            "input": evidence,

            "status": "processed",

            "findings": [],

            "created_at": datetime.now(
                timezone.utc
            ).isoformat()

        }


        if evidence.get("event"):

            result["findings"].append(

                f"Observed {evidence['event']}"

            )


        self.evidence.append(result)


        return result