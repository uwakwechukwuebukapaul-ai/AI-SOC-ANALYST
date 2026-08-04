"""
Autonomous Agent Message Bus

Communication backbone for Sentinel DNA autonomous agents.

Responsibilities:
- Register autonomous agents
- Publish security intelligence messages
- Route messages between agents
- Track communication history
- Monitor agent activity
"""

from datetime import datetime, timezone
from uuid import uuid4


class AutonomousAgentMessageBus:
    """
    Central communication layer for autonomous SOC agents.
    """

    def __init__(self):
        self.agents = {}
        self.subscriptions = {}
        self.messages = []

    def register_agent(self, agent_name, capabilities=None):
        """
        Register an autonomous agent.
        """

        agent = {
            "id": str(uuid4()),
            "name": agent_name,
            "capabilities": capabilities or [],
            "status": "active",
            "registered_at": datetime.now(timezone.utc).isoformat()
        }

        self.agents[agent_name] = agent
        self.subscriptions.setdefault(agent_name, [])

        return agent

    def get_agent(self, agent_name):
        """
        Retrieve registered agent.
        """

        return self.agents.get(agent_name)

    def subscribe(self, agent_name, event_type):
        """
        Subscribe agent to event category.
        """

        if agent_name not in self.agents:
            return False

        self.subscriptions[agent_name].append(event_type)

        return True

    def publish(self, sender, event_type, payload):
        """
        Publish intelligence message.
        """

        message = {
            "message_id": str(uuid4()),
            "sender": sender,
            "event_type": event_type,
            "payload": payload,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        recipients = []

        for agent, events in self.subscriptions.items():
            if event_type in events:
                recipients.append(agent)

        message["recipients"] = recipients

        self.messages.append(message)

        return message

    def get_messages(self):
        """
        Return communication history.
        """

        return self.messages

    def get_agent_health(self):
        """
        Return agent status overview.
        """

        return {
            name: {
                "status": agent["status"],
                "capabilities": agent["capabilities"]
            }
            for name, agent in self.agents.items()
        }

    def clear_history(self):
        """
        Clear message history.
        """

        self.messages.clear()

        return True