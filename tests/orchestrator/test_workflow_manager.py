"""
Sentinel DNA
Investigation Workflow Manager Tests

Validates workflow orchestration,
state transitions, timeline updates,
and failure handling.
"""

import pytest

from services.orchestrator.context import InvestigationContext
from services.orchestrator.exceptions import (
    InvalidStateTransitionError,
)
from services.orchestrator.state_machine import (
    InvestigationState,
)
from services.orchestrator.workflow_manager import (
    WorkflowManager,
)


def create_context():
    return InvestigationContext(
        investigation_id="INV-TEST-001",
        case_id="CASE-TEST-001",
    )


def create_manager():
    context = create_context()
    return WorkflowManager(context)


def test_workflow_starts_in_new_state():
    manager = create_manager()

    assert (
        manager.current_state
        == InvestigationState.NEW
    )


def test_valid_transition_updates_context_status():
    manager = create_manager()

    manager.transition(
        InvestigationState.INGESTING
    )

    assert (
        manager.current_state
        == InvestigationState.INGESTING
    )

    assert (
        manager.context.status
        == InvestigationState.INGESTING.value
    )


def test_transition_creates_timeline_event():
    manager = create_manager()

    manager.transition(
        InvestigationState.INGESTING,
        message="Evidence ingestion started",
    )

    assert len(
        manager.context.timeline
    ) == 1

    assert (
        manager.context.timeline[0]["stage"]
        == "INGESTING"
    )


def test_invalid_transition_raises_error():
    manager = create_manager()

    with pytest.raises(
        InvalidStateTransitionError
    ):
        manager.transition(
            InvestigationState.COMPLETED
        )


def test_fail_marks_investigation_failed():
    manager = create_manager()

    manager.transition(
        InvestigationState.INGESTING
    )

    manager.fail(
        "IOC extraction service unavailable"
    )

    assert (
        manager.current_state
        == InvestigationState.FAILED
    )

    assert (
        manager.context.status
        == InvestigationState.FAILED.value
    )