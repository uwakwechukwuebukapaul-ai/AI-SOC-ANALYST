"""
Sentinel DNA
Enterprise Investigation Agent Interface

Defines the base contract that every investigation agent
must implement.

Author: Sentinel DNA
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

from .context import InvestigationContext


class BaseAgent(ABC):
    """
    Abstract base class for Sentinel DNA investigation agents.

    Every AI/security agent must implement:
        - name
        - description
        - execute()

    This creates a plugin architecture where new agents
    can be added without modifying the orchestrator core.
    """

    name: str = "base_agent"

    description: str = "Base Sentinel DNA investigation agent"


    @abstractmethod
    def execute(
        self,
        context: InvestigationContext,
    ) -> Dict[str, Any]:
        """
        Execute agent logic against an investigation context.

        Args:
            context:
                Shared investigation state.

        Returns:
            Dictionary containing agent results.
        """

        pass


    def validate_context(
        self,
        context: InvestigationContext,
    ) -> None:
        """
        Validate that the agent received a valid context object.
        """

        if not isinstance(context, InvestigationContext):
            raise TypeError(
                "Agent requires InvestigationContext"
            )


    def get_metadata(self) -> Dict[str, Any]:
        """
        Returns agent metadata.

        Used later for:
        - agent registry
        - UI display
        - capability discovery
        - governance
        """

        return {
            "name": self.name,
            "description": self.description,
        }