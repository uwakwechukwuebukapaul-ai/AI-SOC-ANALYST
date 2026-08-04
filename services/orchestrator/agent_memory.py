"""
Sentinel DNA
Enterprise Agent Memory Engine

Stores agent execution history, performance signals,
and investigation learning data.

Author: Sentinel DNA
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def utc_now():
    return datetime.now(timezone.utc)


@dataclass
class AgentMemoryRecord:
    """
    Single agent memory entry.
    """

    agent_name: str

    investigation_id: Optional[str] = None

    success: bool = False

    performance_score: float = 0.0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=utc_now
    )


class AgentMemory:
    """
    Persistent-ready memory layer for agents.

    Responsibilities:
    - Store execution outcomes
    - Track agent performance
    - Provide historical feedback
    - Support future learning systems
    """

    def __init__(self):

        self.records: List[AgentMemoryRecord] = []


    def remember(
        self,
        agent_name: str,
        success: bool,
        investigation_id: Optional[str] = None,
        performance_score: float = 0.0,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> AgentMemoryRecord:
        """
        Store agent execution memory.
        """

        record = AgentMemoryRecord(
            agent_name=agent_name,
            investigation_id=investigation_id,
            success=success,
            performance_score=performance_score,
            metadata=metadata or {},
        )

        self.records.append(record)

        return record


    def get_agent_history(
        self,
        agent_name: str,
    ) -> List[AgentMemoryRecord]:
        """
        Return history for specific agent.
        """

        return [
            record
            for record in self.records
            if record.agent_name == agent_name
        ]


    def get_success_rate(
        self,
        agent_name: str,
    ) -> float:
        """
        Calculate agent success rate.
        """

        history = self.get_agent_history(
            agent_name
        )

        if not history:
            return 0.0

        successes = sum(
            1
            for item in history
            if item.success
        )

        return successes / len(history)


    def get_all_records(self):
        """
        Return complete memory.
        """

        return self.records


    def clear(self):
        """
        Clear memory storage.
        """

        self.records.clear()