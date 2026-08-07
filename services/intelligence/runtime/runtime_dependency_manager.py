"""
Sentinel DNA Runtime Dependency Manager

Enterprise dependency validation layer.

Responsibilities:

- register dependencies
- validate runtime requirements
- track dependency state
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeDependencyManager:
    """
    Runtime dependency manager.
    """

    dependencies: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )


    def register(
        self,
        name: str,
        required: bool = True,
    ) -> None:
        """
        Register dependency.
        """

        self.dependencies[name] = {
            "required": required,
            "available": False,
        }



    def mark_available(
        self,
        name: str,
    ) -> None:
        """
        Mark dependency available.
        """

        if name in self.dependencies:
            self.dependencies[name]["available"] = True



    def available(
        self,
        name: str,
    ) -> bool:
        """
        Check dependency state.
        """

        dependency = self.dependencies.get(
            name
        )

        if dependency is None:
            return False


        return dependency["available"]



    def validate(self) -> bool:
        """
        Validate required dependencies.
        """

        for dependency in self.dependencies.values():

            if (
                dependency["required"]
                and not dependency["available"]
            ):
                return False


        return True



    def count(self) -> int:
        """
        Return dependency count.
        """

        return len(
            self.dependencies
        )



    def clear(self) -> None:
        """
        Reset dependencies.
        """

        self.dependencies.clear()



    def status(self) -> dict[str, Any]:
        """
        Dependency status.
        """

        return {
            "dependencies":
                self.dependencies,

            "valid":
                self.validate(),
        }