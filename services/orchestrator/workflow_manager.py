"""
Sentinel DNA
Enterprise Investigation Workflow Manager

Coordinates investigation lifecycle transitions.

Author: Sentinel DNA
"""

from __future__ import annotations

from typing import Optional

from .audit import audit_logger
from .context import InvestigationContext
from .exceptions import InvalidStateTransitionError
from .state_machine import (
    InvestigationState,
    InvestigationStateMachine,
)


class WorkflowManager:
    """
    Coordinates workflow state transitions for an investigation.
    """

    def __init__(self, context: InvestigationContext):
        self.context = context
        self.state_machine = InvestigationStateMachine()

    @property
    def current_state(self) -> InvestigationState:
        return self.state_machine.get_state()

    def transition(
        self,
        new_state: InvestigationState,
        message: Optional[str] = None,
    ) -> InvestigationState:
        """
        Transition the investigation to a new state.
        """

        current = self.current_state

        if not self.state_machine.can_transition(new_state):
            raise InvalidStateTransitionError(
                current.value,
                new_state.value,
            )

        self.state_machine.transition(new_state)

        self.context.status = new_state.value
        self.context.update_timestamp()

        event_message = (
            message
            or f"Transitioned from {current.value} to {new_state.value}"
        )

        self.context.add_timeline_event(
            stage=new_state.value,
            message=event_message,
        )

        audit_logger.log_event(
            stage=new_state.value,
            event_type="STATE_TRANSITION",
            message=event_message,
            investigation_id=self.context.investigation_id,
            case_id=self.context.case_id,
        )

        return new_state

    def fail(self, reason: str) -> None:
        """
        Mark the investigation as failed.
        """

        self.transition(
            InvestigationState.FAILED,
            message=reason,
        )

    def terminate(self, reason: str) -> None:
        """
        Terminate the investigation.
        """

        self.transition(
            InvestigationState.TERMINATED,
            message=reason,
        )

    def complete(self) -> None:
        """
        Mark the investigation as completed.
        """

        self.transition(
            InvestigationState.COMPLETED,
            message="Investigation completed successfully.",
        )

        self.context.mark_completed()