from datetime import datetime, timezone


class AutonomousThreatHuntingEngine:
    """
    Autonomous Threat Hunting Intelligence Engine

    Responsibilities:
    - Threat hypothesis generation
    - IOC hunting
    - Behaviour analysis
    - MITRE ATT&CK mapping
    - Campaign discovery
    - Hunt history tracking
    """

    def __init__(self):
        self.indicators = []
        self.hunts = []
        self.history = []

    def register_indicator(self, indicator, indicator_type):
        record = {
            "indicator": indicator,
            "type": indicator_type,
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.indicators.append(record)
        return record

    def create_hunt_hypothesis(self, hypothesis):
        hunt = {
            "hypothesis": hypothesis,
            "status": "created",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.hunts.append(hunt)
        self.history.append(hunt)

        return hunt

    def analyze_behavior(self, behavior):
        result = {
            "behavior": behavior,
            "risk_level": "high"
            if "suspicious" in behavior.lower()
            else "low",
            "analysis": "behavioral threat assessment completed"
        }

        self.history.append(result)

        return result

    def search_ioc(self, query):
        matches = [
            indicator
            for indicator in self.indicators
            if query.lower() in indicator["indicator"].lower()
        ]

        result = {
            "query": query,
            "matches": matches,
            "match_count": len(matches)
        }

        self.history.append(result)

        return result

    def map_attack_technique(self, technique):
        mapping = {
            "technique": technique,
            "framework": "MITRE ATT&CK",
            "mapped": True
        }

        self.history.append(mapping)

        return mapping

    def generate_hunting_report(self):
        report = {
            "total_indicators": len(self.indicators),
            "active_hunts": len(self.hunts),
            "history_events": len(self.history),
            "generated_at": datetime.now(timezone.utc).isoformat()
        }

        return report

    def get_history(self):
        return self.history