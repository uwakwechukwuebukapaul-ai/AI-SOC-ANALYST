"""
Autonomous SOC Command Center

Sentinel DNA Operational Control Interface

Responsibilities:
- provide SOC operational visibility
- aggregate agent status
- track investigations
- summarize threats
- monitor system health
- maintain command history
"""

from datetime import datetime, timezone


class AutonomousSOCCommandCenter:

    def __init__(self):
        self.agents = []
        self.investigations = []
        self.threats = []
        self.history = []

    def register_agent_status(
        self,
        agent_name,
        status
    ):

        agent = {
            "agent": agent_name,
            "status": status
        }

        self.agents.append(agent)
        self.history.append(agent)

        return agent

    def add_investigation(
        self,
        investigation_id,
        severity
    ):

        investigation = {
            "id": investigation_id,
            "severity": severity,
            "status": "active"
        }

        self.investigations.append(investigation)
        self.history.append(investigation)

        return investigation

    def add_threat_event(
        self,
        threat_type,
        risk_score
    ):

        threat = {
            "type": threat_type,
            "risk_score": risk_score
        }

        self.threats.append(threat)
        self.history.append(threat)

        return threat

    def get_dashboard_snapshot(self):

        snapshot = {
            "agents": len(self.agents),
            "active_investigations": len(
                self.investigations
            ),
            "threat_events": len(
                self.threats
            ),
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.history.append(snapshot)

        return snapshot

    def get_system_health(self):

        health = {
            "status": "healthy",
            "agents_online": len(
                self.agents
            ),
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.history.append(health)

        return health

    def get_history(self):

        return self.history