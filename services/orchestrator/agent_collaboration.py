"""
Agent Collaboration Layer

Provides communication and coordination between multiple Sentinel DNA agents.

Responsibilities:
- Create collaboration groups
- Register participating agents
- Exchange messages between agents
- Execute collaborative workflows
- Maintain collaboration history
"""

from datetime import datetime, timezone


class AgentCollaboration:
    """
    Multi-agent collaboration coordinator.
    """

    def __init__(self):
        self.groups = {}
        self.messages = []
        self.history = []

    def register_collaboration_group(self, group_name):
        """
        Create a new collaboration group.
        """

        if group_name in self.groups:
            raise ValueError("Collaboration group already exists")

        self.groups[group_name] = {
            "agents": [],
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": "active",
        }

        return self.groups[group_name]

    def add_agent_to_group(self, group_name, agent_name):
        """
        Add an agent to collaboration group.
        """

        if group_name not in self.groups:
            raise ValueError("Unknown collaboration group")

        if agent_name not in self.groups[group_name]["agents"]:
            self.groups[group_name]["agents"].append(agent_name)

        return self.groups[group_name]

    def send_message(
        self,
        group_name,
        sender,
        receiver,
        message,
    ):
        """
        Exchange messages between agents.
        """

        if group_name not in self.groups:
            raise ValueError("Unknown collaboration group")

        event = {
            "group": group_name,
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self.messages.append(event)

        return event

    def execute_collaboration(self, group_name, task):
        """
        Execute collaborative task.
        """

        if group_name not in self.groups:
            raise ValueError("Unknown collaboration group")

        result = {
            "group": group_name,
            "task": task,
            "agents": self.groups[group_name]["agents"],
            "status": "completed",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self.history.append(result)

        return result

    def get_collaboration_history(self):
        """
        Return collaboration execution history.
        """

        return self.history.copy()

    def clear_history(self):
        """
        Clear collaboration records.
        """

        self.history.clear()
        self.messages.clear()