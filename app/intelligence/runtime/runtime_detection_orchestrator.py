"""
Sentinel DNA Runtime Detection Orchestrator

Canonical enterprise detection runtime.

Responsibilities:

- register detection rules
- evaluate security events
- normalize detection results
- track detection operations
- expose runtime status
- preserve legacy detect() compatibility
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


DetectionHandler = Callable[
    [dict[str, Any]],
    Any,
]


@dataclass
class RuntimeDetectionOrchestrator:
    """
    Canonical runtime detection coordinator.

    Detection business logic remains inside registered handlers.

    This class owns:

    - rule registration
    - routing
    - lifecycle
    - metrics
    - result normalization
    """

    rules: dict[str, DetectionHandler] = field(
        default_factory=dict
    )

    operations: int = 0

    detections: int = 0

    failures: int = 0

    # ------------------------------------------------------------------
    # Rule Registration
    # ------------------------------------------------------------------

    def register_rule(
        self,
        name: str,
        handler: DetectionHandler,
    ) -> None:
        """
        Register a detection rule.
        """

        normalized_name = str(
            name
        ).strip()

        if not normalized_name:
            raise ValueError(
                "Detection rule name is required."
            )

        if not callable(handler):
            raise TypeError(
                "Detection rule handler must be callable."
            )

        self.rules[normalized_name] = handler

    def unregister_rule(
        self,
        name: str,
    ) -> DetectionHandler | None:
        """
        Remove a detection rule.
        """

        return self.rules.pop(
            str(name).strip(),
            None,
        )

    def has_rule(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a detection rule exists.
        """

        return (
            str(name).strip()
            in self.rules
        )

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def evaluate(
        self,
        event_type: str,
        event: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Evaluate an event against a registered detection rule.

        Always returns a normalized dictionary containing
        a ``success`` field.
        """

        self.operations += 1

        normalized_event = dict(
            event or {}
        )

        normalized_event_type = str(
            event_type
        ).strip()

        try:
            handler = self.rules.get(
                normalized_event_type
            )

            if handler is None:
                return {
                    "success": True,
                    "detected": False,
                    "event_type": normalized_event_type,
                    "rule": None,
                    "message": (
                        "No detection rule registered "
                        f"for event type "
                        f"'{normalized_event_type}'."
                    ),
                    "event": normalized_event,
                }

            raw_result = handler(
                normalized_event
            )

            result = self._normalize_result(
                raw_result
            )

            result.setdefault(
                "event_type",
                normalized_event_type,
            )

            result.setdefault(
                "rule",
                normalized_event_type,
            )

            if result.get(
                "detected"
            ) is True:
                self.detections += 1

            return result

        except Exception as exc:
            self.failures += 1

            return {
                "success": False,
                "detected": False,
                "event_type": normalized_event_type,
                "rule": normalized_event_type,
                "error": str(exc),
                "event": normalized_event,
            }

    # ------------------------------------------------------------------
    # Compatibility
    # ------------------------------------------------------------------

    def detect(
        self,
        event_type: str,
        event: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Backward-compatible alias for evaluate().
        """

        return self.evaluate(
            event_type,
            event,
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Clear rules and runtime counters.
        """

        self.rules.clear()

        self.operations = 0
        self.detections = 0
        self.failures = 0

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        """
        Return detection runtime status.
        """

        return {
            "operations": self.operations,
            "detections": self.detections,
            "failures": self.failures,
            "rules": list(
                self.rules.keys()
            ),
            "count": len(
                self.rules
            ),
        }

    # ------------------------------------------------------------------
    # Result Normalization
    # ------------------------------------------------------------------

    @staticmethod
    def _normalize_result(
        result: Any,
    ) -> dict[str, Any]:
        """
        Normalize arbitrary detection handler output.
        """

        if isinstance(
            result,
            dict,
        ):
            normalized = dict(
                result
            )

            normalized.setdefault(
                "success",
                True,
            )

            return normalized

        if isinstance(
            result,
            bool,
        ):
            return {
                "success": True,
                "detected": result,
            }

        if result is None:
            return {
                "success": True,
                "detected": False,
            }

        return {
            "success": True,
            "detected": bool(
                result
            ),
            "result": result,
        }