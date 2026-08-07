"""
Sentinel DNA Enterprise AI Agent Base

Defines the abstract contract implemented by every AI
agent in the platform.

Author:
    Sentinel DNA

License:
    Internal
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseAgent(ABC):
    """
    Enterprise AI Agent Base.

    Every AI agent inside Sentinel DNA inherits from
    this class.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human readable agent name.
        """

    @property
    @abstractmethod
    def version(self) -> str:
        """
        Agent version.
        """

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Agent description.
        """

    @property
    @abstractmethod
    def capabilities(self) -> list[str]:
        """
        Supported capabilities.
        """

    @abstractmethod
    def validate(
        self,
        context: Any,
    ) -> bool:
        """
        Validate execution context.
        """

    @abstractmethod
    def execute(
        self,
        context: Any,
    ) -> Any:
        """
        Execute agent.
        """

    @abstractmethod
    def summarize(
        self,
        result: Any,
    ) -> str:
        """
        Produce summary.
        """

    @abstractmethod
    def cleanup(self) -> None:
        """
        Release resources.
        """

    def metadata(self) -> dict[str, Any]:
        """
        Standard metadata.

        Returns
        -------
        dict
        """

        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "capabilities": self.capabilities,
        }

    def __repr__(self) -> str:

        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, "
            f"version={self.version!r})"
        )