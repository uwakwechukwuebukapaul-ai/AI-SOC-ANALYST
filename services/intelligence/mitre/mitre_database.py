"""
Sentinel DNA MITRE Technique Database

Temporary in-memory ATT&CK knowledge store.

Future:
- STIX ingestion
- MITRE TAXII API
- Enterprise ATT&CK sync
"""


from services.intelligence.mitre.mitre_technique import (
    MitreTechnique,
)


class MitreDatabase:


    def __init__(self):

        self.techniques = {

            "T1566":
                MitreTechnique(
                    technique_id="T1566",
                    name="Phishing",
                    tactic="Initial Access",
                    description=
                    "Adversaries send phishing messages.",
                ),


            "T1204":
                MitreTechnique(
                    technique_id="T1204",
                    name="User Execution",
                    tactic="Execution",
                    description=
                    "Users execute malicious content.",
                ),


            "T1059":
                MitreTechnique(
                    technique_id="T1059",
                    name="Command and Scripting Interpreter",
                    tactic="Execution",
                    description=
                    "Execution through command interpreters.",
                ),
        }



    def get(
        self,
        technique_id: str,
    ):

        return self.techniques.get(
            technique_id
        )



    def all(self):

        return list(
            self.techniques.values()
        )