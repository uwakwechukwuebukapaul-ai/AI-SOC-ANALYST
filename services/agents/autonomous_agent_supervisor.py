"""
Sentinel DNA
Autonomous Agent Supervisor

Responsible for:
- registering security agents
- monitoring agent state
- assigning tasks
- coordinating autonomous workflows
- tracking execution history
"""

from datetime import datetime, timezone


class AutonomousAgentSupervisor:

    def __init__(self):
        self.agents = {}
        self.task_history = []

    def register_agent(self, agent_name, capabilities):
        agent = {
            "name": agent_name,
            "capabilities": capabilities,
            "status": "active",
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.agents[agent_name] = agent

        return agent

    def get_agent(self, agent_name):
        return self.agents.get(agent_name)

    def list_agents(self):
        return list(self.agents.values())

    def assign_task(self, agent_name, task):

        agent = self.agents.get(agent_name)

        if not agent:
            return {
                "status": "failed",
                "message": "Agent not found"
            }

        execution = {
            "agent": agent_name,
            "task": task,
            "status": "assigned",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.task_history.append(execution)

        return execution

    def execute_workflow(self, workflow):

        results = []

        for step in workflow:

            agent_name = step.get("agent")
            task = step.get("task")

            result = self.assign_task(
                agent_name,
                task
            )

            results.append(result)

        return {
            "workflow_status": "completed",
            "steps": results
        }

    def monitor_agent_health(self):

        health = {}

        for name, agent in self.agents.items():

            health[name] = {
                "status": agent["status"],
                "healthy": agent["status"] == "active"
            }

        return health

    def get_task_history(self):

        return self.task_history

    def clear_history(self):

        self.task_history.clear()

        return {
            "status": "cleared"
        }