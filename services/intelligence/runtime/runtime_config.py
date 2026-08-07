"""
Sentinel DNA Runtime Configuration

Central runtime configuration layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeConfig:
    """
    Enterprise runtime configuration.
    """

    max_workers: int = 4

    max_queue_size: int = 1000

    retry_enabled: bool = True

    max_retries: int = 3

    execution_timeout: int = 300

    telemetry_enabled: bool = True

    audit_enabled: bool = True

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def update(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Update configuration value.
        """

        if hasattr(self, key):
            setattr(
                self,
                key,
                value,
            )

        else:
            self.metadata[key] = value



    def get(
        self,
        key: str,
        default=None,
    ):
        """
        Retrieve configuration value.
        """

        return getattr(
            self,
            key,
            self.metadata.get(
                key,
                default
            ),
        )



    def to_dict(self) -> dict[str, Any]:
        """
        Export configuration.
        """

        return {
            "max_workers": self.max_workers,
            "max_queue_size": self.max_queue_size,
            "retry_enabled": self.retry_enabled,
            "max_retries": self.max_retries,
            "execution_timeout": self.execution_timeout,
            "telemetry_enabled": self.telemetry_enabled,
            "audit_enabled": self.audit_enabled,
            "metadata": self.metadata,
        }