"""
Sentinel DNA
Autonomous Security Decision Engine

Purpose:
Transforms security intelligence into autonomous SOC decisions.

Flow:

Detection
    ↓
Reasoning
    ↓
Decision Engine
    ↓
Response Recommendation
"""


from datetime import datetime


class AutonomousSecurityDecisionEngine:
    """
    Autonomous decision-making layer for Sentinel DNA.
    """

    def __init__(self):
        self.decisions = []

    def evaluate_threat(self, threat_data):
        """
        Analyze threat information and generate security decisions.
        """

        risk_score = threat_data.get("risk_score", 0)
        threat_type = threat_data.get("threat_type", "unknown")
        asset = threat_data.get("asset", "unknown")

        if risk_score >= 90:
            severity = "critical"
            action = [
                "isolate_asset",
                "disable_compromised_account",
                "create_incident",
                "notify_security_team"
            ]

        elif risk_score >= 60:
            severity = "high"
            action = [
                "create_incident",
                "collect_more_evidence",
                "notify_analyst"
            ]

        elif risk_score >= 30:
            severity = "medium"
            action = [
                "monitor_activity",
                "increase_logging"
            ]

        else:
            severity = "low"
            action = [
                "continue_monitoring"
            ]

        decision = {
            "threat_type": threat_type,
            "asset": asset,
            "risk_score": risk_score,
            "severity": severity,
            "recommended_actions": action,
            "created_at": datetime.utcnow().isoformat()
        }

        self.decisions.append(decision)

        return decision


    def generate_response_priority(self, decision):
        """
        Assign response priority.
        """

        severity = decision.get("severity")

        priorities = {
            "critical": "immediate",
            "high": "urgent",
            "medium": "scheduled",
            "low": "monitor"
        }

        return priorities.get(
            severity,
            "monitor"
        )


    def should_auto_respond(self, decision):
        """
        Determine whether automated response is allowed.
        """

        return decision.get("severity") in [
            "critical",
            "high"
        ]


    def get_decision_history(self):
        """
        Return all previous decisions.
        """

        return self.decisions


    def clear_history(self):
        """
        Clear stored decisions.
        """

        self.decisions.clear()