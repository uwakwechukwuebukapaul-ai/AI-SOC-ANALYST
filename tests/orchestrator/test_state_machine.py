"""
Sentinel DNA
Investigation State Machine Tests

Validates investigation lifecycle transitions.
"""

import pytest

from services.orchestrator.state_machine import (
    InvestigationState,
    InvestigationStateMachine,
)


def test_initial_state_is_new():
    machine = InvestigationStateMachine()

    assert machine.get_state() == InvestigationState.NEW


def test_valid_investigation_transition_flow():
    machine = InvestigationStateMachine()

    machine.transition(InvestigationState.INGESTING)
    machine.transition(InvestigationState.IOC_EXTRACTION)
    machine.transition(InvestigationState.THREAT_INTEL)
    machine.transition(InvestigationState.EVIDENCE_COLLECTION)

    assert (
        machine.get_state()
        == InvestigationState.EVIDENCE_COLLECTION
    )


def test_invalid_transition_is_blocked():
    machine = InvestigationStateMachine()

    with pytest.raises(ValueError):
        machine.transition(
            InvestigationState.COMPLETED
        )


def test_completed_state():
    machine = InvestigationStateMachine()

    machine.transition(InvestigationState.INGESTING)
    machine.transition(InvestigationState.IOC_EXTRACTION)
    machine.transition(InvestigationState.THREAT_INTEL)
    machine.transition(InvestigationState.EVIDENCE_COLLECTION)
    machine.transition(InvestigationState.MITRE_MAPPING)
    machine.transition(InvestigationState.AI_ANALYSIS)
    machine.transition(InvestigationState.RECOMMENDATIONS)
    machine.transition(InvestigationState.RESPONSE)
    machine.transition(InvestigationState.COMPLETED)

    assert machine.is_complete()