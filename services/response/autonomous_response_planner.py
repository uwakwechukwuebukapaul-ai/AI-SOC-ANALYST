"""
Sentinel DNA - Autonomous Response Planner

Responsible for generating response recommendations
based on investigation intelligence and risk context.
"""


class AutonomousResponsePlanner:

    def __init__(self):
        self.response_history = []

    def create_response_plan(self, investigation):
        risk = investigation.get("risk", "LOW")

        plan = {
            "investigation_id": investigation.get(
                "id",
                "UNKNOWN"
            ),
            "risk": risk,
            "actions": self._select_actions(risk),
            "approval_required": risk != "CRITICAL"
        }

        self.response_history.append(plan)

        return plan

    def _select_actions(self, risk):

        if risk == "CRITICAL":
            return [
                "isolate_endpoint",
                "block_ioc",
                "escalate_incident"
            ]

        if risk == "HIGH":
            return [
                "block_ioc",
                "collect_additional_evidence",
                "notify_analyst"
            ]

        if risk == "MEDIUM":
            return [
                "monitor_activity",
                "request_review"
            ]

        return [
            "close_as_low_risk",
            "continue_monitoring"
        ]

    def evaluate_action_priority(self, action):

        priorities = {
            "isolate_endpoint": 100,
            "block_ioc": 90,
            "escalate_incident": 80,
            "collect_additional_evidence": 60,
            "notify_analyst": 50,
            "monitor_activity": 30
        }

        return priorities.get(action, 10)

    def get_response_history(self):
        return self.response_history

    def clear_history(self):
        self.response_history.clear()