from datetime import datetime, timezone


class AutonomousAgentCoordinator:

    def __init__(self):
        self.agents = {}
        self.tasks = []
        self.workflow_history = []

    def register_agent(self, agent_id, agent_type):
        agent = {
            "agent_id": agent_id,
            "agent_type": agent_type,
            "status": "registered",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.agents[agent_id] = agent

        return agent

    def get_agent(self, agent_id):
        return self.agents.get(agent_id)

    def assign_task(self, agent_id, task):
        if agent_id not in self.agents:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        assignment = {
            "agent_id": agent_id,
            "task": task,
            "status": "assigned",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        self.tasks.append(assignment)

        return assignment

    def coordinate_workflow(self, workflow):

        execution = {
            "workflow": workflow,
            "steps": [],
            "status": "completed",
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        for step in workflow:
            execution["steps"].append(
                {
                    "step": step,
                    "status": "completed"
                }
            )

        self.workflow_history.append(execution)

        return execution

    def route_intelligence_request(self, request_type):

        routing = {
            "threat_detection": "detection_agent",
            "threat_hunting": "hunting_agent",
            "incident_response": "response_agent",
            "report_generation": "reporting_agent",
            "analysis": "reasoning_agent"
        }

        return {
            "request": request_type,
            "assigned_agent": routing.get(
                request_type,
                "general_security_agent"
            )
        }

    def system_status(self):
        """
        Internal status provider.
        """

        return {
            "agents": len(self.agents),
            "tasks": len(self.tasks),
            "workflows": len(self.workflow_history),
            "status": "operational"
        }

    def get_system_status(self):
        """
        Public integration API.

        Used by:
        - integration tests
        - health monitoring
        - platform bootstrap
        - orchestration services
        """

        return self.system_status()

    def clear_history(self):

        self.tasks.clear()
        self.workflow_history.clear()

        return {
            "status": "cleared"
        }