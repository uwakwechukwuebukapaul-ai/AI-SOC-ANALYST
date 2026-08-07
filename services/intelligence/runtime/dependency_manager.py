"""
Sentinel DNA Runtime Dependency Manager

Manages runtime service dependencies and component resolution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DependencyManager:
    """
    Runtime dependency registry.
    """

    dependencies: dict[str, Any] = field(
        default_factory=dict
    )


    def register(
        self,
        name: str,
        component: Any,
    ) -> None:
        """
        Register runtime dependency.
        """

        self.dependencies[name] = component



    def resolve(
        self,
        name: str,
        default=None,
    ) -> Any:
        """
        Resolve dependency.
        """

        return self.dependencies.get(
            name,
            default,
        )



    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove dependency.
        """

        self.dependencies.pop(
            name,
            None,
        )



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check dependency existence.
        """

        return name in self.dependencies



    def clear(self) -> None:
        """
        Clear dependencies.
        """

        self.dependencies.clear()



    def size(self) -> int:
        """
        Dependency count.
        """

        return len(
            self.dependencies
        )



    def to_dict(self) -> dict:
        """
        Export dependency state.
        """

        return {
            "count": self.size(),
            "dependencies": list(
                self.dependencies.keys()
            ),
        }