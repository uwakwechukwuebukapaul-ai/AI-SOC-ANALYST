"""
Sentinel DNA Runtime Resource Manager

Enterprise runtime resource control layer.

Responsibilities:

- register resources
- allocate resources
- release resources
- track utilization
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
        Register resource pool.
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
        Allocate resource.
        """

        resource = self.resources.get(
            name
        )

        if resource is None:
            return False


        available = (
            resource["capacity"]
            -
            resource["allocated"]
        )


        if amount > available:
            return False


        resource["allocated"] += amount

        return True



    def release(
        self,
        name: str,
        amount: int = 1,
    ) -> None:
        """
        Release resource.
        """

        resource = self.resources.get(
            name
        )

        if resource is None:
            return


        resource["allocated"] = max(
            0,
            resource["allocated"] - amount,
        )



    def utilization(
        self,
        name: str,
    ) -> float:
        """
        Calculate utilization.
        """

        resource = self.resources.get(
            name
        )

        if resource is None:
            return 0.0


        if resource["capacity"] == 0:
            return 0.0


        return (
            resource["allocated"]
            /
            resource["capacity"]
        )



    def count(self) -> int:
        """
        Return resource count.
        """

        return len(
            self.resources
        )



    def clear(self) -> None:
        """
        Reset resources.
        """

        self.resources.clear()



    def status(self) -> dict[str, Any]:
        """
        Resource status.
        """

        return {
            "resources":
                self.resources,

            "count":
                self.count(),
        }