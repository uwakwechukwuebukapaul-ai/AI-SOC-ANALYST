"""
Agent Decision Engine

Responsible for autonomous agent selection and prioritization.
"""

from datetime import datetime, timezone


class AgentDecisionEngine:
    """
    Autonomous decision engine for agent orchestration.
    """

    def __init__(self):
        self.rules = {}
        self.decisions = []

    def register_decision_rule(
        self,
        capability,
        agent_name,
        priority=1,
    ):
        """
        Register agent routing rule.
        """

        self.rules[capability] = {
            "agent": agent_name,
            "priority": priority,
        }

        return self.rules[capability]

    def select_best_agent(self, capability):
        """
        Select most suitable agent for capability.
        """

        if capability not in self.rules:
            return None

        rule = self.rules[capability]

        decision = {
            "capability": capability,
            "selected_agent": rule["agent"],
            "priority": rule["priority"],
            "reason": "Capability match",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        self.decisions.append(decision)

        return decision

    def calculate_priority(self, severity):
        """
        Calculate task priority from severity.
        """

        priorities = {
            "critical": 5,
            "high": 4,
            "medium": 3,
            "low": 2,
            "info": 1,
        }

        return priorities.get(
            severity.lower(),
            1,
        )

    def get_decision_history(self):
        """
        Return previous decisions.
        """

        return self.decisions.copy()

    def clear_decisions(self):
        """
        Clear decision memory.
        """

        self.decisions.clear()

    def handle_unknown_capability(self, capability):
        """
        Handle unsupported capability.
        """

        return {
            "capability": capability,
            "agent": None,
            "status": "unavailable",
        }