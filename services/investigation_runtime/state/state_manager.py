"""
Investigation state manager.

Provides lifecycle-oriented access to investigation state
without coupling the runtime to a database implementation.

A repository-backed implementation can replace the internal
storage mechanism later without changing the public state
model contract.
"""

from __future__ import annotations

from typing import Any

from .investigation_state import (
    InvestigationState,
)


class InvestigationStateManager:
    """
    Manages investigation state instances.

    The current implementation uses in-memory storage.
    Persistent repositories can be introduced behind the same
    lifecycle-oriented API in a later milestone.
    """

    def __init__(self) -> None:
        self._states: dict[
            str,
            InvestigationState,
        ] = {}

    def create(
        self,
        investigation_id: str,
        investigation: dict[str, Any],
    ) -> InvestigationState:
        """
        Create and register a new investigation state.
        """

        if not investigation_id:
            raise ValueError(
                "Investigation ID is required."
            )

        if not isinstance(
            investigation,
            dict,
        ):
            raise TypeError(
                "Investigation must be a dictionary."
            )

        if investigation_id in self._states:
            raise ValueError(
                f"Investigation '{investigation_id}' "
                "already exists."
            )

        state = InvestigationState(
            investigation_id=investigation_id,
            investigation=investigation,
        )

        self._states[investigation_id] = state

        return state

    def get(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Retrieve an investigation state.
        """

        if investigation_id not in self._states:
            raise KeyError(
                f"Investigation '{investigation_id}' "
                "was not found."
            )

        return self._states[investigation_id]

    def exists(
        self,
        investigation_id: str,
    ) -> bool:
        """
        Determine whether an investigation exists.
        """

        return investigation_id in self._states

    def start(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Start an existing investigation.
        """

        state = self.get(
            investigation_id
        )

        state.start()

        return state

    def complete(
        self,
        investigation_id: str,
        *,
        intelligence: dict[str, Any] | None = None,
        correlation: dict[str, Any] | None = None,
        confidence: dict[str, Any] | None = None,
        finding: dict[str, Any] | None = None,
    ) -> InvestigationState:
        """
        Complete an existing investigation.
        """

        state = self.get(
            investigation_id
        )

        state.complete(
            intelligence=intelligence,
            correlation=correlation,
            confidence=confidence,
            finding=finding,
        )

        return state

    def fail(
        self,
        investigation_id: str,
        error: str,
        *,
        service: str | None = None,
    ) -> InvestigationState:
        """
        Fail an existing investigation while preserving
        structured error information.
        """

        state = self.get(
            investigation_id
        )

        state.fail(
            error,
            service=service,
        )

        return state

    def cancel(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Cancel an existing investigation.
        """

        state = self.get(
            investigation_id
        )

        state.cancel()

        return state

    def update(
        self,
        investigation_id: str,
        **values: Any,
    ) -> InvestigationState:
        """
        Update investigation intelligence state.
        """

        state = self.get(
            investigation_id
        )

        state.update(
            **values
        )

        return state

    def list(
        self,
    ) -> list[InvestigationState]:
        """
        Return all known investigation states.
        """

        return list(
            self._states.values()
        )

    def remove(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Remove an investigation from the manager.

        Persistent deletion will be handled by the repository
        layer once storage is introduced.
        """

        if investigation_id not in self._states:
            raise KeyError(
                f"Investigation '{investigation_id}' "
                "was not found."
            )

        return self._states.pop(
            investigation_id
        )

    def clear(self) -> None:
        """
        Clear all in-memory investigation states.

        Primarily useful for tests and isolated runtime
        instances.
        """

        self._states.clear()