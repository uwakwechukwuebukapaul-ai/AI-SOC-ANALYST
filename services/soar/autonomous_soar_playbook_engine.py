"""
Sentinel DNA
Autonomous SOAR Playbook Engine

Responsible for:
- Creating automated response playbooks
- Executing security response actions
- Tracking execution history
- Supporting containment workflows
- Providing rollback-ready execution records
"""

from datetime import datetime, timezone
import uuid


class AutonomousSOARPlaybookEngine:

    def __init__(self):
        self.playbooks = {}
        self.execution_history = []

    def create_playbook(self, name, trigger, actions):
        playbook_id = str(uuid.uuid4())

        playbook = {
            "id": playbook_id,
            "name": name,
            "trigger": trigger,
            "actions": actions,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.playbooks[playbook_id] = playbook

        return playbook

    def execute_playbook(self, playbook_id, context=None):

        if playbook_id not in self.playbooks:
            return {
                "status": "failed",
                "message": "Playbook not found"
            }

        playbook = self.playbooks[playbook_id]

        results = []

        for action in playbook["actions"]:
            results.append(
                self.execute_action(
                    action,
                    context
                )
            )

        execution = {
            "execution_id": str(uuid.uuid4()),
            "playbook_id": playbook_id,
            "status": "completed",
            "results": results,
            "executed_at": datetime.now(timezone.utc).isoformat()
        }

        self.execution_history.append(execution)

        return execution

    def execute_action(self, action, context=None):

        action_map = {
            "isolate_host": "Endpoint isolated",
            "block_ioc": "IOC blocked",
            "disable_account": "Account disabled",
            "collect_evidence": "Evidence collected",
            "notify_soc": "SOC notified",
            "create_case": "Incident case created"
        }

        return {
            "action": action,
            "status": "success",
            "result": action_map.get(
                action,
                "Action executed"
            ),
            "context": context or {}
        }

    def recommend_response(self, severity):

        if severity == "critical":
            return [
                "isolate_host",
                "block_ioc",
                "disable_account",
                "create_case"
            ]

        if severity == "high":
            return [
                "block_ioc",
                "collect_evidence",
                "notify_soc"
            ]

        return [
            "notify_soc"
        ]

    def get_execution_history(self):

        return self.execution_history

    def rollback_execution(self, execution_id):

        for execution in self.execution_history:

            if execution["execution_id"] == execution_id:

                execution["rollback"] = {
                    "status": "completed",
                    "timestamp": datetime.now(
                        timezone.utc
                    ).isoformat()
                }

                return execution

        return {
            "status": "failed",
            "message": "Execution not found"
        }

    def clear_history(self):

        self.execution_history.clear()