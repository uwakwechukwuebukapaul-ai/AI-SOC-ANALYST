"""
Autonomous Agent Supervisor Engine

Sentinel DNA AI SOC Control Layer

Responsibilities:
- monitor autonomous agents
- track agent health
- prioritize workloads
- recover failed agents
- score agent performance
- maintain supervisor history
"""

from datetime import datetime, timezone
import uuid


class AutonomousAgentSupervisorEngine:

    def __init__(self):
        self.agents = {}
        self.history = []

    def register_agent(
        self,
        agent_name,
        agent_type
    ):

        agent_id = (
            f"AGT-{uuid.uuid4().hex[:8].upper()}"
        )

        agent = {
            "id": agent_id,
            "name": agent_name,
            "type": agent_type,
            "status": "active",
            "health": "healthy",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.agents[agent_id] = agent
        self.history.append(agent)

        return agent

    def monitor_agent_health(
        self,
        agent_id
    ):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "not_found"
            }

        result = {
            "agent_id": agent_id,
            "health": agent["health"],
            "status": agent["status"]
        }

        self.history.append(result)

        return result

    def assign_priority(
        self,
        task,
        severity
    ):

        if severity >= 90:
            priority = "critical"

        elif severity >= 60:
            priority = "high"

        else:
            priority = "normal"

        result = {
            "task": task,
            "severity": severity,
            "priority": priority
        }

        self.history.append(result)

        return result

    def recover_failed_agent(
        self,
        agent_id
    ):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "not_found"
            }

        agent["status"] = "recovered"
        agent["health"] = "healthy"

        result = {
            "agent_id": agent_id,
            "recovery": "successful"
        }

        self.history.append(result)

        return result

    def evaluate_agent_performance(
        self,
        agent_id,
        completed_tasks,
        failed_tasks
    ):

        total = (
            completed_tasks +
            failed_tasks
        )

        if total == 0:
            score = 0

        else:
            score = round(
                (completed_tasks / total)
                * 100,
                2
            )

        result = {
            "agent_id": agent_id,
            "performance_score": score
        }

        self.history.append(result)

        return result

    def get_history(self):

        return self.history