"""
Sentinel DNA
Autonomous Threat Hunting Engine

Responsible for:
- creating hunting hypotheses
- generating hunting queries
- analyzing hunting results
- tracking threat discovery patterns
"""


class AutonomousThreatHuntingEngine:

    def __init__(self):
        self.hunts = []
        self.results = []
        self.hunting_history = []

    def create_hunting_hypothesis(self, title, description, technique):
        hypothesis = {
            "title": title,
            "description": description,
            "technique": technique,
            "status": "active"
        }

        self.hunts.append(hypothesis)

        return hypothesis

    def generate_query(self, hypothesis):
        query = {
            "technique": hypothesis["technique"],
            "query": (
                f"Search events related to "
                f"{hypothesis['technique']}"
            )
        }

        return query

    def analyze_hunting_result(self, data):
        findings = []

        if data.get("suspicious_process"):
            findings.append("suspicious_process")

        if data.get("unknown_network_connection"):
            findings.append("unknown_network_connection")

        if data.get("credential_activity"):
            findings.append("credential_activity")

        result = {
            "threat_found": len(findings) > 0,
            "findings": findings,
            "confidence": len(findings) * 30
        }

        self.results.append(result)

        return result

    def record_hunt(self, hypothesis, outcome):
        record = {
            "hypothesis": hypothesis,
            "outcome": outcome
        }

        self.hunting_history.append(record)

        return record

    def get_hunting_history(self):
        return {
            "hypotheses": self.hunts,
            "results": self.results,
            "history": self.hunting_history
        }

    def clear_history(self):
        self.hunts.clear()
        self.results.clear()
        self.hunting_history.clear()