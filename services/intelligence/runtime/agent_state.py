"""
Sentinel DNA Runtime Agent State
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class AgentStatus(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    BUSY = "busy"
    FAILED = "failed"
    OFFLINE = "offline"


@dataclass(slots=True)
class AgentState:
    """
    Runtime state of an AI agent.
    """

    name: str

    status: AgentStatus = AgentStatus.IDLE

    capabilities: list[str] = field(default_factory=list)

    current_task: str | None = None

    heartbeat: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    metadata: dict[str, Any] = field(default_factory=dict)

    def set_status(self, status: AgentStatus) -> None:
        self.status = status
        self.heartbeat = datetime.now(timezone.utc)

    def assign_task(self, task_id: str) -> None:
        self.current_task = task_id
        self.set_status(AgentStatus.RUNNING)

    def clear_task(self) -> None:
        self.current_task = None
        self.set_status(AgentStatus.IDLE)

    def add_capability(self, capability: str) -> None:
        if capability not in self.capabilities:
            self.capabilities.append(capability)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status.value,
            "capabilities": self.capabilities,
            "current_task": self.current_task,
            "heartbeat": self.heartbeat.isoformat(),
            "metadata": self.metadata,
        }