"""
Autonomous Security Decision Engine

Sentinel DNA Decision Intelligence Layer

Responsibilities:
- convert intelligence into security decisions
- prioritize incidents
- select response actions
- determine escalation requirements
- maintain decision history
"""

from datetime import datetime, timezone
import uuid


class AutonomousSecurityDecisionEngine:

    def __init__(self):
        self.decisions = []
        self.history = []

    def create_decision(
        self,
        incident_type,
        risk_score,
        confidence=0.85
    ):

        decision_id = (
            f"DEC-{uuid.uuid4().hex[:8].upper()}"
        )

        decision = {
            "id": decision_id,
            "incident_type": incident_type,
            "risk_score": risk_score,
            "confidence": confidence,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.decisions.append(decision)
        self.history.append(decision)

        return decision

    def evaluate_risk_decision(
        self,
        risk_score
    ):

        if risk_score >= 90:
            action = "automatic_containment"
            priority = "critical"

        elif risk_score >= 70:
            action = "incident_response"
            priority = "high"

        elif risk_score >= 40:
            action = "investigation_required"
            priority = "medium"

        else:
            action = "monitor"
            priority = "low"

        result = {
            "risk_score": risk_score,
            "priority": priority,
            "recommended_action": action
        }

        self.history.append(result)

        return result

    def determine_incident_priority(
        self,
        impact,
        likelihood
    ):

        score = (
            impact * likelihood
        )

        if score >= 80:
            priority = "critical"

        elif score >= 50:
            priority = "high"

        elif score >= 25:
            priority = "medium"

        else:
            priority = "low"

        result = {
            "impact": impact,
            "likelihood": likelihood,
            "priority": priority
        }

        self.history.append(result)

        return result

    def select_response_action(
        self,
        threat_type
    ):

        actions = {

            "malware":
                "isolate_endpoint",

            "credential_compromise":
                "reset_credentials",

            "data_exfiltration":
                "block_network_access",

            "phishing":
                "quarantine_email"
        }

        result = {
            "threat_type": threat_type,
            "action":
                actions.get(
                    threat_type,
                    "monitor_activity"
                )
        }

        self.history.append(result)

        return result

    def requires_human_approval(
        self,
        action,
        confidence
    ):

        requires_approval = (
            action == "automatic_containment"
            and confidence < 0.95
        )

        result = {
            "action": action,
            "confidence": confidence,
            "human_approval_required":
                requires_approval
        }

        self.history.append(result)

        return result

    def get_history(self):

        return self.history