"""
Autonomous Security Governance Engine

Sentinel DNA Governance Intelligence Layer

Responsibilities:
- define security policies
- validate autonomous actions
- manage risk acceptance
- map controls to compliance frameworks
- enforce analyst override controls
- maintain governance history
"""

from datetime import datetime, timezone
import uuid


class AutonomousSecurityGovernanceEngine:

    def __init__(self):
        self.policies = []
        self.history = []

    def create_policy(
        self,
        name,
        rule,
        severity="medium"
    ):

        policy_id = (
            f"POL-{uuid.uuid4().hex[:8].upper()}"
        )

        policy = {
            "id": policy_id,
            "name": name,
            "rule": rule,
            "severity": severity,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.policies.append(policy)
        self.history.append(policy)

        return policy

    def validate_action_policy(
        self,
        action,
        risk_score
    ):

        if risk_score >= 90:
            decision = "requires_approval"

        elif action == "automatic_containment":
            decision = "allowed_with_monitoring"

        else:
            decision = "allowed"

        result = {
            "action": action,
            "risk_score": risk_score,
            "decision": decision
        }

        self.history.append(result)

        return result

    def create_risk_acceptance(
        self,
        risk,
        owner,
        justification
    ):

        acceptance = {
            "risk": risk,
            "owner": owner,
            "justification": justification,
            "status": "pending_review"
        }

        self.history.append(acceptance)

        return acceptance

    def map_compliance_control(
        self,
        framework,
        control
    ):

        mapping = {
            "framework": framework,
            "control": control,
            "mapped": True
        }

        self.history.append(mapping)

        return mapping

    def override_control(
        self,
        analyst,
        action,
        reason
    ):

        override = {
            "analyst": analyst,
            "action": action,
            "reason": reason,
            "status": "override_applied"
        }

        self.history.append(override)

        return override

    def get_history(self):

        return self.history