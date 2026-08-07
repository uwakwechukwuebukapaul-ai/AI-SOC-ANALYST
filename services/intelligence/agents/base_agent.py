"""
Sentinel DNA Enterprise AI Agent Base
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from services.intelligence.agents.agent_capability import (
    AgentCapability,
)
from services.intelligence.agents.agent_context import (
    AgentContext,
)
from services.intelligence.agents.agent_metadata import (
    AgentMetadata,
)
from services.intelligence.agents.agent_result import (
    AgentResult,
)


class BaseAgent(ABC):
    """
    Base class for every Sentinel DNA AI agent.
    """

    @property
    @abstractmethod
    def metadata(self) -> AgentMetadata:
        """
        Agent metadata.
        """

    @property
    @abstractmethod
    def capabilities(
        self,
    ) -> list[AgentCapability]:
        """
        Supported capabilities.
        """

    @abstractmethod
    def validate(
        self,
        context: AgentContext,
    ) -> bool:
        """
        Validate execution context.
        """

    @abstractmethod
    def execute(
        self,
        context: AgentContext,
    ) -> AgentResult:
        """
        Execute the agent.
        """

    @abstractmethod
    def summarize(
        self,
        result: AgentResult,
    ) -> str:
        """
        Produce a summary.
        """

    @abstractmethod
    def cleanup(self) -> None:
        """
        Cleanup resources.
        """

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name={self.metadata.name!r}, "
            f"version={self.metadata.version!r})"
        )