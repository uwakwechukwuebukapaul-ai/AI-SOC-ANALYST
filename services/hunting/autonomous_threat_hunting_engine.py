"""
Autonomous Threat Hunting Engine

Responsible for:
- threat hypothesis generation
- hunting query creation
- IOC and behavior correlation
- suspicious pattern discovery
- hunting history tracking

Future expansion:
- MITRE ATT&CK technique mapping
- Sigma/YARA query generation
- LLM-powered hunt reasoning
- SIEM telemetry integration
"""

from datetime import datetime, timezone


class AutonomousThreatHuntingEngine:
    def __init__(self):
        self.hunting_history = []
        self.patterns = []

    def create_hypothesis(self, threat_data):
        risk_score = threat_data.get("risk_score", 0)
        behavior = threat_data.get("behavior", "unknown")

        if risk_score >= 80:
            priority = "critical"
        elif risk_score >= 50:
            priority = "high"
        else:
            priority = "low"

        hypothesis = {
            "behavior": behavior,
            "risk_score": risk_score,
            "priority": priority,
            "hypothesis": f"Investigate {behavior} activity for possible compromise",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.hunting_history.append(hypothesis)

        return hypothesis

    def generate_hunt_query(self, indicator):
        query = {
            "indicator": indicator,
            "query": f"search telemetry where indicator='{indicator}'",
            "status": "generated",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        return query

    def detect_pattern(self, events):
        suspicious = []

        for event in events:
            if event.get("severity") in ["high", "critical"]:
                suspicious.append(event)

        pattern = {
            "matches": len(suspicious),
            "events": suspicious,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.patterns.append(pattern)

        return pattern

    def correlate_threat_intelligence(self, intelligence):
        return {
            "matched": True if intelligence else False,
            "confidence": "high" if intelligence else "low",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

    def get_hunting_history(self):
        return self.hunting_history

    def clear_history(self):
        self.hunting_history.clear()
        self.patterns.clear()

        return {
            "status": "cleared"
        }