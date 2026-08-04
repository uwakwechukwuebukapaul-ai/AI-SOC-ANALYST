"""
Sentinel DNA - Autonomous Response Executor

Executes approved response actions generated
by the Autonomous Response Planner.
"""


class AutonomousResponseExecutor:

    def __init__(self):
        self.execution_history = []

    def execute_response(self, response_plan):

        execution = {
            "investigation_id": response_plan.get(
                "investigation_id",
                "UNKNOWN"
            ),
            "actions": [],
            "status": "completed",
            "failed_actions": []
        }

        for action in response_plan.get("actions", []):

            result = self._execute_action(action)

            if result["success"]:
                execution["actions"].append(action)
            else:
                execution["failed_actions"].append(action)

        if execution["failed_actions"]:
            execution["status"] = "partial_failure"

        self.execution_history.append(execution)

        return execution

    def _execute_action(self, action):

        supported_actions = [
            "isolate_endpoint",
            "block_ioc",
            "escalate_incident",
            "collect_additional_evidence",
            "notify_analyst",
            "monitor_activity",
            "close_as_low_risk"
        ]

        if action in supported_actions:
            return {
                "action": action,
                "success": True
            }

        return {
            "action": action,
            "success": False
        }

    def execute_single_action(self, action):

        return self._execute_action(action)

    def get_execution_history(self):

        return self.execution_history

    def clear_history(self):

        self.execution_history.clear()