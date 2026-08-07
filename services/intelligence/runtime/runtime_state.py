"""
Sentinel DNA Runtime State

Enterprise runtime state management.

Tracks:
- lifecycle state
- component states
- runtime metadata
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class RuntimeState:
    """
    Runtime state container.
    """

    status: str = "initialized"

    components: dict[str, str] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    updated_at: datetime = field(
        default_factory=lambda:
        datetime.now(timezone.utc)
    )



class RuntimeStateManager:
    """
    Controls runtime state.
    """

    def __init__(self):

        self.state = RuntimeState()



    def set_status(
        self,
        status: str,
    ) -> None:
        """
        Update runtime status.
        """

        self.state.status = status

        self._touch()



    def get_status(
        self,
    ) -> str:
        """
        Return runtime status.
        """

        return self.state.status



    def set_component(
        self,
        name: str,
        status: str,
    ) -> None:
        """
        Update component state.
        """

        self.state.components[name] = status

        self._touch()



    def get_component(
        self,
        name: str,
        default=None,
    ):
        """
        Retrieve component state.
        """

        return self.state.components.get(
            name,
            default,
        )



    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store runtime metadata.
        """

        self.state.metadata[key] = value

        self._touch()



    def snapshot(self) -> dict:
        """
        Create runtime snapshot.
        """

        return {
            "status":
                self.state.status,

            "components":
                dict(self.state.components),

            "metadata":
                dict(self.state.metadata),

            "updated_at":
                self.state.updated_at,
        }



    def reset(self) -> None:
        """
        Reset runtime state.
        """

        self.state = RuntimeState()



    def _touch(self):
        self.state.updated_at = (
            datetime.now(timezone.utc)
        )