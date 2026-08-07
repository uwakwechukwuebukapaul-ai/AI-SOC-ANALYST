"""
Sentinel DNA Enterprise Runtime Base

Shared functionality for runtime managers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeBase:
    """
    Shared runtime storage and operations.
    """

    items: dict[str, Any] = field(
        default_factory=dict
    )

    def get(
        self,
        name: str,
    ) -> Any | None:
        """
        Retrieve an item.
        """

        return self.items.get(name)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check item existence.
        """

        return name in self.items

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove item.
        """

        self.items.pop(name, None)

    def count(
        self,
    ) -> int:
        """
        Number of stored items.
        """

        return len(self.items)

    def clear(
        self,
    ) -> None:
        """
        Reset storage.
        """

        self.items.clear()

    def keys(
        self,
    ) -> list[str]:
        """
        Return sorted keys.
        """

        return sorted(self.items.keys())

    def status(
        self,
    ) -> dict[str, Any]:
        """
        Generic status.
        """

        return {
            "count": self.count(),
            "items": self.keys(),
        }