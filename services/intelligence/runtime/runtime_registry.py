"""
Sentinel DNA Runtime Registry

Component discovery and registration layer
for Intelligence Runtime Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeRegistry:
    """
    Stores runtime components.
    """

    agents: dict[str, Any] = field(
        default_factory=dict
    )

    handlers: dict[str, Any] = field(
        default_factory=dict
    )

    capabilities: dict[str, Any] = field(
        default_factory=dict
    )


    def register_agent(
        self,
        name: str,
        agent: Any,
    ) -> None:

        self.agents[name] = agent


    def get_agent(
        self,
        name: str,
    ) -> Any | None:

        return self.agents.get(name)


    def register_handler(
        self,
        name: str,
        handler: Any,
    ) -> None:

        self.handlers[name] = handler


    def get_handler(
        self,
        name: str,
    ) -> Any | None:

        return self.handlers.get(name)


    def register_capability(
        self,
        name: str,
        capability: Any,
    ) -> None:

        self.capabilities[name] = capability


    def get_capability(
        self,
        name: str,
    ) -> Any | None:

        return self.capabilities.get(name)


    def clear(self) -> None:

        self.agents.clear()
        self.handlers.clear()
        self.capabilities.clear()


    def to_dict(self) -> dict:

        return {
            "agents": list(self.agents.keys()),
            "handlers": list(self.handlers.keys()),
            "capabilities": list(self.capabilities.keys()),
        }