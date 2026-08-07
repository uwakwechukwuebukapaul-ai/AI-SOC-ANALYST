"""
Sentinel DNA Agent Metadata

Strongly typed metadata model for AI agents.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class AgentMetadata:
    """
    Metadata describing an AI agent.
    """

    name: str

    version: str

    description: str

    author: str = "Sentinel DNA"

    capabilities: list[str] = field(
        default_factory=list
    )

    investigation_types: list[str] = field(
        default_factory=list
    )

    tags: list[str] = field(
        default_factory=list
    )

    runtime_version: str = "1.0"

    experimental: bool = False

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize metadata.
        """

        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "capabilities": self.capabilities,
            "investigation_types": self.investigation_types,
            "tags": self.tags,
            "runtime_version": self.runtime_version,
            "experimental": self.experimental,
        }