"""
Investigation state manager for Sentinel DNA.

Maintains runtime state objects for active investigations
and provides controlled lifecycle operations.
"""

from __future__ import annotations

from typing import Any

from .investigation_state import (
    InvestigationState,
)


class InvestigationStateManager:
    """
    Central registry for InvestigationState objects.
    """

    def __init__(self) -> None:
        self._states: dict[
            str,
            InvestigationState,
        ] = {}

    def create(
        self,
        investigation_id: str,
        metadata: dict[str, Any] | None = None,
    ) -> InvestigationState:
        if not investigation_id:
            raise ValueError(
                "Investigation ID is required."
            )

        if investigation_id in self._states:
            raise ValueError(
                f"Investigation '{investigation_id}' "
                "already exists."
            )

        state = InvestigationState(
            investigation_id=investigation_id,
            metadata=metadata,
        )

        self._states[
            investigation_id
        ] = state

        return state

    def get(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        try:
            return self._states[
                investigation_id
            ]
        except KeyError:
            raise KeyError(
                f"Investigation state "
                f"'{investigation_id}' not found."
            ) from None

    def exists(
        self,
        investigation_id: str,
    ) -> bool:
        return investigation_id in self._states

    def count(self) -> int:
        return len(self._states)

    def ids(self) -> list[str]:
        return list(
            self._states.keys()
        )

    def start(
        self,
        investigation_id: str,
        stage: str,
    ) -> None:
        self.get(
            investigation_id
        ).start(stage)

    def set_stage(
        self,
        investigation_id: str,
        stage: str,
    ) -> None:
        self.get(
            investigation_id
        ).set_stage(stage)

    def record_result(
        self,
        investigation_id: str,
        stage: str,
        result: dict[str, Any],
    ) -> None:
        self.get(
            investigation_id
        ).record_result(
            stage,
            result,
        )

    def complete_stage(
        self,
        investigation_id: str,
        stage: str,
        result: dict[str, Any],
    ) -> None:
        self.get(
            investigation_id
        ).complete_stage(
            stage,
            result,
        )

    def record_error(
        self,
        investigation_id: str,
        stage: str,
        error: str | Exception,
    ) -> None:
        """
        Record an investigation-stage failure.

        The manager accepts either a human-readable string
        or an Exception. Strings are normalized into
        RuntimeError instances before reaching the state
        domain object.
        """

        if isinstance(error, Exception):
            exception = error
        elif isinstance(error, str):
            exception = RuntimeError(error)
        else:
            raise TypeError(
                "Error must be a string or Exception."
            )

        self.get(
            investigation_id
        ).record_error(
            stage,
            exception,
        )

    def complete(
        self,
        investigation_id: str,
    ) -> None:
        self.get(
            investigation_id
        ).complete()

    def fail(
        self,
        investigation_id: str,
    ) -> None:
        self.get(
            investigation_id
        ).fail()

    def snapshot(
        self,
        investigation_id: str,
    ) -> dict[str, Any]:
        return self.get(
            investigation_id
        ).snapshot()

    def remove(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        try:
            return self._states.pop(
                investigation_id
            )
        except KeyError:
            raise KeyError(
                f"Investigation state "
                f"'{investigation_id}' not found."
            ) from None

    def clear(self) -> None:
        self._states.clear()