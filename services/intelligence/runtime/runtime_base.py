"""
Sentinel DNA Runtime Base

Provides a common container implementation for runtime
components such as registries and managers.
"""

from __future__ import annotations

from typing import Any


class RuntimeBase:
    """
    Base runtime container.
    """

    def __init__(self) -> None:
        """
        Initialize the runtime container.
        """
        self.items: dict[str, Any] = {}

    def exists(self, name: str) -> bool:
        """
        Check whether an item exists.
        """
        return name in self.items

    def get(
        self,
        name: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve an item.
        """
        return self.items.get(name, default)

    def remove(self, name: str) -> None:
        """
        Remove an item if present.
        """
        self.items.pop(name, None)

    def clear(self) -> None:
        """
        Remove all items.
        """
        self.items.clear()

    def count(self) -> int:
        """
        Return the number of registered items.
        """
        return len(self.items)

    def status(self) -> dict[str, Any]:
        """
        Return runtime status information.
        """
        return {
            "count": self.count(),
            "items": list(self.items.keys()),
        }