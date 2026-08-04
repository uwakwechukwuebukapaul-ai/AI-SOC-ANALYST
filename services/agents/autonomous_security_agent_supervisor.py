"""
Autonomous Security Agent Supervisor

Control layer for Sentinel DNA autonomous agents.

Responsibilities:
- Register supervised agents
- Monitor agent health
- Track confidence scores
- Detect failures
- Generate recovery actions
- Maintain supervisor history
"""

from datetime import datetime


class AutonomousSecurityAgentSupervisor:

    def __init__(self):
        self.agents = {}
        self.events = []
        self.history = []

    def register_agent(self, agent_id, name, role):

        agent = {
            "agent_id": agent_id,
            "name": name,
            "role": role,
            "status": "healthy",
            "confidence": 1.0,
            "registered_at": datetime.utcnow().isoformat()
        }

        self.agents[agent_id] = agent

        self.history.append({
            "event": "agent_registered",
            "agent_id": agent_id,
            "timestamp": datetime.utcnow().isoformat()
        })

        return agent

    def update_agent_health(self, agent_id, status, confidence):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        agent["status"] = status
        agent["confidence"] = confidence

        event = {
            "event": "health_update",
            "agent_id": agent_id,
            "status": status,
            "confidence": confidence,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(event)
        self.history.append(event)

        return agent

    def analyze_agent_health(self, agent_id):

        agent = self.agents.get(agent_id)

        if not agent:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        health_score = agent["confidence"]

        if health_score >= 0.8:
            condition = "healthy"
        elif health_score >= 0.5:
            condition = "degraded"
        else:
            condition = "critical"

        return {
            "agent_id": agent_id,
            "health_score": health_score,
            "condition": condition,
            "timestamp": datetime.utcnow().isoformat()
        }

    def detect_failures(self):

        failures = []

        for agent in self.agents.values():

            if agent["status"] != "healthy":

                failures.append({
                    "agent_id": agent["agent_id"],
                    "status": agent["status"],
                    "confidence": agent["confidence"]
                })

        return failures

    def generate_recovery_action(self, agent_id):

        analysis = self.analyze_agent_health(agent_id)

        if analysis.get("condition") == "critical":

            action = "restart_agent"

        elif analysis.get("condition") == "degraded":

            action = "retrain_agent"

        else:

            action = "continue_operation"

        recovery = {
            "agent_id": agent_id,
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append(recovery)

        return recovery

    def supervisor_state(self):

        return {
            "total_agents": len(self.agents),
            "healthy_agents": len(
                [
                    agent
                    for agent in self.agents.values()
                    if agent["status"] == "healthy"
                ]
            ),
            "events": len(self.events),
            "timestamp": datetime.utcnow().isoformat()
        }

    def supervisor_history(self):

        return self.history