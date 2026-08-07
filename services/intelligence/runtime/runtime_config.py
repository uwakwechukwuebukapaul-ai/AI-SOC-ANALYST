"""
Sentinel DNA Runtime Configuration

Central configuration service for Intelligence Runtime Framework.

Responsibilities:

- Runtime settings management
- Configuration overrides
- Environment profiles
- Runtime configuration snapshots
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeConfig:
    """
    Enterprise runtime configuration container.
    """

    environment: str = "development"

    max_workers: int = 4

    task_timeout: int = 300

    auto_start: bool = False

    debug: bool = False

    settings: dict[str, Any] = field(
        default_factory=dict
    )


    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Update runtime configuration.
        """

        self.settings[key] = value



    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve configuration value.
        """

        return self.settings.get(
            key,
            default,
        )



    def update(
        self,
        values: dict[str, Any],
    ) -> None:
        """
        Bulk update configuration.
        """

        self.settings.update(
            values
        )



    def reset(self) -> None:
        """
        Reset custom settings.
        """

        self.settings.clear()



    def profile(
        self,
        environment: str,
    ) -> None:
        """
        Change runtime profile.
        """

        self.environment = environment



    def to_dict(self) -> dict[str, Any]:
        """
        Export configuration.
        """

        return {
            "environment": self.environment,
            "max_workers": self.max_workers,
            "task_timeout": self.task_timeout,
            "auto_start": self.auto_start,
            "debug": self.debug,
            "settings": self.settings,
        }