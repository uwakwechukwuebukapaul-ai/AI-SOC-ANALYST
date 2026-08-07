"""
End-to-end Sentinel DNA investigation execution.

The orchestrator coordinates runtime services and the
investigation intelligence layer without coupling itself
to individual intelligence implementations.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from services.investigation_intelligence import (
    InvestigationEngine,
)
from services.investigation_runtime.integration import (
    InvestigationServiceBridge,
)


class InvestigationExecutionOrchestrator:
    """
    Executes a complete Sentinel DNA investigation.

    Responsibilities:

    1. Validate investigation input.
    2. Discover available runtime services.
    3. Execute each intelligence service.
    4. Collect intelligence outputs.
    5. Pass collected intelligence into the investigation
       intelligence layer.
    6. Return one normalized investigation execution result.

    The orchestrator does not contain intelligence logic.
    """

    def __init__(
        self,
        service_bridge: InvestigationServiceBridge | None = None,
        intelligence_engine: InvestigationEngine | None = None,
    ) -> None:
        self.service_bridge = (
            service_bridge
            or InvestigationServiceBridge()
        )

        self.intelligence_engine = (
            intelligence_engine
            or InvestigationEngine()
        )

    def execute(
        self,
        investigation: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Execute the complete investigation lifecycle.
        """

        self._validate_investigation(
            investigation
        )

        started_at = self._timestamp()

        services = (
            self.service_bridge.available_services()
        )

        intelligence: dict[
            str,
            dict[str, Any],
        ] = {}

        execution_errors: list[
            dict[str, Any]
        ] = []

        for service_name in services:
            try:
                result = self.service_bridge.execute(
                    service_name,
                    investigation,
                )

                if not isinstance(result, dict):
                    raise TypeError(
                        f"Service '{service_name}' "
                        "must return a dictionary."
                    )

                intelligence[
                    service_name
                ] = result

            except Exception as exc:
                execution_errors.append(
                    {
                        "service": service_name,
                        "error": str(exc),
                        "type": type(exc).__name__,
                    }
                )

        analysis = (
            self.intelligence_engine.analyze_results(
                investigation,
                intelligence,
            )
        )

        completed_at = self._timestamp()

        status = (
            "completed"
            if not execution_errors
            else "completed_with_errors"
        )

        return {
            "type": "investigation_execution",
            "status": status,
            "investigation": investigation,
            "execution": {
                "services": services,
                "executed": list(
                    intelligence.keys()
                ),
                "failed": [
                    error["service"]
                    for error in execution_errors
                ],
                "started_at": started_at,
                "completed_at": completed_at,
            },
            "intelligence": intelligence,
            "errors": execution_errors,
            "correlation": analysis[
                "correlation"
            ],
            "confidence": analysis[
                "confidence"
            ],
            "finding": analysis[
                "finding"
            ],
        }

    @staticmethod
    def _validate_investigation(
        investigation: dict[str, Any],
    ) -> None:
        if not isinstance(
            investigation,
            dict,
        ):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        if not investigation:
            raise ValueError(
                "Investigation cannot be empty."
            )

    @staticmethod
    def _timestamp() -> str:
        return datetime.now(
            timezone.utc
        ).isoformat()