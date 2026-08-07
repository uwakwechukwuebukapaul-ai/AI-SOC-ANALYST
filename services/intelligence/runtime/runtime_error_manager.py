"""
Sentinel DNA Runtime Error Manager

Enterprise runtime error handling layer.

Responsibilities:

- capture runtime errors
- classify failures
- expose error history
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any



@dataclass
class RuntimeErrorManager:
    """
    Runtime error controller.
    """

    errors: list[dict[str, Any]] = field(
        default_factory=list
    )



    def record(
        self,
        component: str,
        message: str,
        severity: str = "error",
    ) -> None:
        """
        Record runtime error.
        """

        self.errors.append(
            {
                "component":
                    component,

                "message":
                    message,

                "severity":
                    severity,

                "timestamp":
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
            }
        )



    def latest(
        self,
    ) -> dict[str, Any] | None:
        """
        Return latest error.
        """

        if not self.errors:
            return None

        return self.errors[-1]



    def count(self) -> int:
        """
        Return error count.
        """

        return len(
            self.errors
        )



    def by_component(
        self,
        component: str,
    ) -> list[dict[str, Any]]:
        """
        Return component errors.
        """

        return [
            error
            for error in self.errors
            if error["component"] == component
        ]



    def clear(self) -> None:
        """
        Reset errors.
        """

        self.errors.clear()



    def status(self) -> dict[str, Any]:
        """
        Error status.
        """

        return {
            "errors":
                self.errors,

            "count":
                self.count(),
        }