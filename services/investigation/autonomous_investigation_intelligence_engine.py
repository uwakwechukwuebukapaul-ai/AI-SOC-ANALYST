from datetime import datetime, timezone


class AutonomousInvestigationIntelligenceEngine:

    def __init__(self):
        self.investigations = []


    def analyze(self, evidence):

        analysis = {
            "type": "evidence_analysis",
            "input": evidence,
            "findings": [],
            "severity": evidence.get(
                "severity",
                "unknown"
            ),
            "status": "completed",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        if evidence.get("event"):
            analysis["findings"].append(
                f"Detected event: {evidence['event']}"
            )

        self.investigations.append(
            analysis
        )

        return analysis


    def investigate(self, alert):

        investigation = {
            "type": "investigation",
            "alert": alert,
            "steps": [
                "alert_received",
                "indicator_analysis",
                "threat_assessment"
            ],
            "status": "completed",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.investigations.append(
            investigation
        )

        return investigation


    def build_timeline(self, events):

        timeline = {
            "type": "timeline",
            "events": [],
            "status": "completed",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }


        for index, event in enumerate(events):

            timeline["events"].append(
                {
                    "order": index + 1,
                    "event": event
                }
            )

        return timeline