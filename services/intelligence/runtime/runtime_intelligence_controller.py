"""
Sentinel DNA Runtime Intelligence Controller

Application controller layer.

Responsibilities:

- handle intelligence requests
- validate input
- call runtime API
- format responses
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .runtime_intelligence_api import (
    RuntimeIntelligenceAPI,
)


@dataclass
class RuntimeIntelligenceController:
    """
    Runtime intelligence controller.
    """

    api: RuntimeIntelligenceAPI = field(
        default_factory=RuntimeIntelligenceAPI
    )


    def register(
        self,
        capability: str,
        handler,
    ) -> None:
        """
        Register capability.
        """

        self.api.register(
            capability,
            handler,
        )



    def investigate(
        self,
        request: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Process intelligence request.
        """

        capability = request.get(
            "capability"
        )

        investigation_id = request.get(
            "investigation_id"
        )


        if not capability or not investigation_id:
            return {
                "success": False,
                "error": "invalid_request",
            }


        result = self.api.execute(
            capability,
            investigation_id,
            request.get(
                "metadata"
            ),
        )


        return {
            "success": result is not None,
            "result": result,
        }



    def status(self) -> dict[str, Any]:
        """
        Controller status.
        """

        return self.api.status()