"""
Sentinel DNA Runtime Configuration Manager

Enterprise runtime configuration layer.

Responsibilities:

- store runtime configuration
- manage feature flags
- provide configuration lookup
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeConfigurationManager:
    """
    Runtime configuration controller.
    """

    settings: dict[str, Any] = field(
        default_factory=dict
    )

    flags: dict[str, bool] = field(
        default_factory=dict
    )



    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store configuration value.
        """

        self.settings[key] = value



    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve configuration.
        """

        return self.settings.get(
            key,
            default,
        )



    def enable(
        self,
        feature: str,
    ) -> None:
        """
        Enable feature flag.
        """

        self.flags[feature] = True



    def disable(
        self,
        feature: str,
    ) -> None:
        """
        Disable feature flag.
        """

        self.flags[feature] = False



    def enabled(
        self,
        feature: str,
    ) -> bool:
        """
        Check feature state.
        """

        return self.flags.get(
            feature,
            False,
        )



    def clear(self) -> None:
        """
        Reset configuration.
        """

        self.settings.clear()

        self.flags.clear()



    def status(self) -> dict[str, Any]:
        """
        Configuration status.
        """

        return {
            "settings":
                self.settings,

            "flags":
                self.flags,
        }