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
    Runtime configuration service.
    """

    settings: dict[str, Any] = field(
        default_factory=dict
    )

    features: dict[str, bool] = field(
        default_factory=dict
    )


    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store runtime setting.
        """

        self.settings[key] = value



    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve runtime setting.
        """

        return self.settings.get(
            key,
            default,
        )



    def enable_feature(
        self,
        name: str,
    ) -> None:
        """
        Enable runtime feature.
        """

        self.features[name] = True



    def disable_feature(
        self,
        name: str,
    ) -> None:
        """
        Disable runtime feature.
        """

        self.features[name] = False



    def feature_enabled(
        self,
        name: str,
    ) -> bool:
        """
        Check feature state.
        """

        return self.features.get(
            name,
            False,
        )



    def clear(self) -> None:
        """
        Reset configuration.
        """

        self.settings.clear()

        self.features.clear()



    def status(self) -> dict[str, Any]:
        """
        Configuration status.
        """

        return {
            "settings":
                self.settings,

            "features":
                self.features,
        }