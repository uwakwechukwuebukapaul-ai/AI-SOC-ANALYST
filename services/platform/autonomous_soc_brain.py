"""
Autonomous SOC Brain

Central intelligence coordinator for Sentinel DNA.

Responsibilities:
- Coordinate autonomous security engines
- Perform investigation reasoning
- Generate security decisions
- Trigger response workflows
- Maintain SOC operational history
"""

from datetime import datetime, timezone


class AutonomousSOCBrain:
    """
    Central autonomous SOC decision coordinator.
    """

    def __init__(self):
        self.events = []
        self.investigations = []
        self.decisions = []
        self.status = "online"

    def process_security_event(self, event):
        """
        Process incoming security event.
        """

        risk_score = event.get("risk_score", 0)

        analysis = {
            "event": event,
            "risk_level": self._calculate_risk(risk_score),
            "analysis": self._analyze_event(event),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.events.append(analysis)

        decision = self.make_security_decision(analysis)

        investigation = {
            "analysis": analysis,
            "decision": decision,
            "status": "completed"
        }

        self.investigations.append(investigation)

        return investigation

    def _calculate_risk(self, score):
        """
        Determine risk classification.
        """

        if score >= 80:
            return "CRITICAL"

        if score >= 50:
            return "HIGH"

        if score >= 25:
            return "MEDIUM"

        return "LOW"

    def _analyze_event(self, event):
        """
        Basic autonomous reasoning layer.
        """

        indicators = event.get("indicators", [])

        if indicators:
            return {
                "threat_detected": True,
                "indicators_found": indicators,
                "confidence": "high"
            }

        return {
            "threat_detected": False,
            "indicators_found": [],
            "confidence": "low"
        }

    def make_security_decision(self, investigation):
        """
        Autonomous response decision engine.
        """

        risk = investigation["risk_level"]

        if risk == "CRITICAL":
            action = "contain_and_investigate"

        elif risk == "HIGH":
            action = "investigate_and_monitor"

        elif risk == "MEDIUM":
            action = "collect_more_context"

        else:
            action = "close"

        decision = {
            "risk_level": risk,
            "recommended_action": action,
            "automated": True,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.decisions.append(decision)

        return decision

    def get_soc_status(self):
        """
        Return SOC brain health.
        """

        return {
            "status": self.status,
            "events_processed": len(self.events),
            "investigations": len(self.investigations),
            "decisions": len(self.decisions)
        }

    def get_history(self):
        """
        Return SOC reasoning history.
        """

        return {
            "events": self.events,
            "investigations": self.investigations,
            "decisions": self.decisions
        }

    def clear_history(self):
        """
        Clear operational memory.
        """

        self.events.clear()
        self.investigations.clear()
        self.decisions.clear()

        return True