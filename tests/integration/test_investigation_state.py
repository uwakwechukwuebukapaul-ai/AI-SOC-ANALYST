"""
Integration tests for investigation runtime state management.
"""

from __future__ import annotations

import pytest

from services.investigation_runtime.state import (
    InvestigationState,
    InvestigationStateManager,
    InvestigationStatus,
)


def test_investigation_state_creation():
    state = InvestigationState(
        investigation_id="INV-001",
        investigation={
            "source": "endpoint",
            "indicator": "powershell",
        },
    )

    assert state.investigation_id == "INV-001"
    assert state.status == InvestigationStatus.PENDING
    assert state.investigation["indicator"] == "powershell"
    assert state.intelligence == {}
    assert state.correlation == {}
    assert state.confidence == {}
    assert state.finding == {}
    assert state.errors == []
    assert state.created_at is not None
    assert state.updated_at is not None


def test_investigation_state_lifecycle():
    state = InvestigationState(
        investigation_id="INV-002",
        investigation={
            "indicator": "powershell",
        },
    )

    state.start()

    assert state.status == InvestigationStatus.RUNNING
    assert state.started_at is not None

    state.complete(
        intelligence={
            "risk": {
                "score": 90,
            },
        },
        correlation={
            "signal_count": 1,
        },
        confidence={
            "score": 0.9,
        },
        finding={
            "risk": "critical",
        },
    )

    assert state.status == InvestigationStatus.COMPLETED
    assert state.completed_at is not None
    assert state.intelligence["risk"]["score"] == 90
    assert state.correlation["signal_count"] == 1
    assert state.confidence["score"] == 0.9
    assert state.finding["risk"] == "critical"


def test_investigation_state_failure():
    state = InvestigationState(
        investigation_id="INV-003",
        investigation={
            "indicator": "malicious.exe",
        },
    )

    state.start()

    state.fail(
        "Risk provider unavailable",
        service="risk_intelligence",
    )

    assert state.status == InvestigationStatus.FAILED
    assert state.completed_at is not None
    assert len(state.errors) == 1

    error = state.errors[0]

    assert error["error"] == (
        "Risk provider unavailable"
    )
    assert error["service"] == "risk_intelligence"
    assert "timestamp" in error


def test_investigation_state_manager():
    manager = InvestigationStateManager()

    state = manager.create(
        "INV-004",
        {
            "source": "endpoint",
            "indicator": "powershell",
        },
    )

    assert state.investigation_id == "INV-004"
    assert manager.exists("INV-004")
    assert manager.get("INV-004") is state

    manager.start("INV-004")

    assert (
        manager.get("INV-004").status
        == InvestigationStatus.RUNNING
    )

    manager.update(
        "INV-004",
        intelligence={
            "risk": {
                "score": 95,
            },
        },
    )

    assert (
        manager.get("INV-004")
        .intelligence["risk"]["score"]
        == 95
    )

    manager.complete(
        "INV-004",
        confidence={
            "score": 0.95,
        },
        finding={
            "risk": "critical",
        },
    )

    assert (
        manager.get("INV-004").status
        == InvestigationStatus.COMPLETED
    )


def test_state_serialization():
    state = InvestigationState(
        investigation_id="INV-005",
        investigation={
            "source": "email",
        },
    )

    state.start()

    state.complete(
        finding={
            "risk": "high",
        },
    )

    payload = state.to_dict()

    assert payload["investigation_id"] == "INV-005"
    assert payload["status"] == "completed"
    assert payload["investigation"]["source"] == "email"
    assert payload["finding"]["risk"] == "high"
    assert isinstance(
        payload["created_at"],
        str,
    )
    assert isinstance(
        payload["updated_at"],
        str,
    )


def test_state_rejects_invalid_transitions():
    state = InvestigationState(
        investigation_id="INV-006",
        investigation={},
    )

    with pytest.raises(ValueError):
        state.complete()

    state.start()

    with pytest.raises(ValueError):
        state.start()

    state.complete()

    with pytest.raises(ValueError):
        state.fail("too late")


def test_state_validation():
    with pytest.raises(ValueError):
        InvestigationState(
            investigation_id="",
            investigation={},
        )

    with pytest.raises(TypeError):
        InvestigationState(
            investigation_id="INV-007",
            investigation=[],
        )

    manager = InvestigationStateManager()

    manager.create(
        "INV-008",
        {},
    )

    with pytest.raises(ValueError):
        manager.create(
            "INV-008",
            {},
        )

    with pytest.raises(KeyError):
        manager.get("DOES-NOT-EXIST")


def test_state_manager_collection_operations():
    manager = InvestigationStateManager()

    manager.create("INV-009", {})
    manager.create("INV-010", {})

    states = manager.list()

    assert len(states) == 2
    assert {
        state.investigation_id
        for state in states
    } == {
        "INV-009",
        "INV-010",
    }

    removed = manager.remove("INV-009")

    assert removed.investigation_id == "INV-009"
    assert not manager.exists("INV-009")
    assert manager.exists("INV-010")

    manager.clear()

    assert manager.list() == []