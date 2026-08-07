"""
Sentinel DNA Runtime Resource Manager

Enterprise runtime resource management layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeResourceManager:
    """
    Runtime resource controller.
    """

    resources: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )

    def register(
        self,
        name: str,
        capacity: int,
    ) -> None:
        """
        Register a runtime resource.
        """

        self.resources[name] = {
            "capacity": capacity,
            "allocated": 0,
        }

    def allocate(
        self,
        name: str,
        amount: int = 1,
    ) -> bool:
        """
        Allocate resource capacity.
        """

        resource = self.resources.get(name)

        if resource is None:
            return False

        if resource["allocated"] + amount > resource["capacity"]:
            return False

        resource["allocated"] += amount
        return True

    def release(
        self,
        name: str,
        amount: int = 1,
    ) -> bool:
        """
        Release allocated capacity.
        """

        resource = self.resources.get(name)

        if resource is None:
            return False

        resource["allocated"] = max(
            0,
            resource["allocated"] - amount,
        )

        return True

    def available(
        self,
        name: str,
    ) -> int:
        """
        Return available capacity.
        """

        resource = self.resources.get(name)

        if resource is None:
            return 0

        return (
            resource["capacity"]
            - resource["allocated"]
        )

    def count(
        self,
    ) -> int:
        """
        Return registered resource count.
        """

        return len(self.resources)

    def clear(
        self,
    ) -> None:
        """
        Remove all resources.
        """

        self.resources.clear()

    def status(
        self,
    ) -> dict[str, Any]:
        """
        Resource manager status.
        """

        return {
            "count": self.count(),
            "resources": self.resources,
        }