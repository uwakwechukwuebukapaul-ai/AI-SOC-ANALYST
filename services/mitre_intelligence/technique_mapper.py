"""
Maps security signals to MITRE ATT&CK techniques.
"""


class TechniqueMapper:

    TECHNIQUES = {
        "password_spray": {
            "id": "T1110.003",
            "name": "Password Spraying",
            "tactic": "Credential Access",
        },

        "phishing": {
            "id": "T1566",
            "name": "Phishing",
            "tactic": "Initial Access",
        },

        "malware_execution": {
            "id": "T1204",
            "name": "User Execution",
            "tactic": "Execution",
        },
    }


    def map_signal(self, signal):

        return self.TECHNIQUES.get(
            signal,
            {
                "id": "UNKNOWN",
                "name": "Unknown Technique",
                "tactic": "Unknown",
            }
        )