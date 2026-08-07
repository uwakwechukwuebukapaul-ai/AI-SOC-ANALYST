"""
Sentinel DNA Runtime Intelligence Registry

Enterprise intelligence capability registry.

Responsibilities:

- register intelligence services
- discover capabilities
- lookup providers
- maintain registry state
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeIntelligenceRegistry:
    """
    Intelligence module registry.
    """

    modules: dict[str, dict[str, Any]] = field(
        default_factory=dict
    )


    def register(
        self,
        name: str,
        capabilities: list[str],
    ) -> None:
        """
        Register intelligence module.
        """

        self.modules[name] = {
            "capabilities": capabilities,
            "active": True,
        }



    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove module.
        """

        self.modules.pop(
            name,
            None,
        )



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check module.
        """

        return name in self.modules



    def find_provider(
        self,
        capability: str,
    ) -> str | None:
        """
        Find module supporting capability.
        """

        for name, module in self.modules.items():

            if capability in module["capabilities"]:
                return name

        return None



    def count(self) -> int:
        """
        Return module count.
        """

        return len(
            self.modules
        )



    def clear(self) -> None:
        """
        Reset registry.
        """

        self.modules.clear()



    def status(self) -> dict[str, Any]:
        """
        Registry status.
        """

        return {
            "modules":
                self.count(),

            "registered":
                list(
                    self.modules.keys()
                ),
        }