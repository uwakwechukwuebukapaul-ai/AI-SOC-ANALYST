"""
Investigation persistence repository contract.

Defines the storage boundary used by the investigation
runtime without coupling the runtime to SQLite or any
other database technology.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..state import InvestigationState


class InvestigationRepository(ABC):
    """
    Abstract persistence contract for investigation state.
    """

    @abstractmethod
    def create(
        self,
        state: InvestigationState,
    ) -> InvestigationState:
        """
        Persist a new investigation state.
        """
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Retrieve an investigation state.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        investigation_id: str,
    ) -> bool:
        """
        Determine whether an investigation exists.
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        state: InvestigationState,
    ) -> InvestigationState:
        """
        Persist changes to an existing investigation.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        investigation_id: str,
    ) -> InvestigationState:
        """
        Delete and return an investigation state.
        """
        raise NotImplementedError

    @abstractmethod
    def list(
        self,
    ) -> list[InvestigationState]:
        """
        Return all persisted investigations.
        """
        raise NotImplementedError