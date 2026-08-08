"""
Integration tests for the Investigation Runtime state layer.
"""

from __future__ import annotations

import pytest

from services.investigation_runtime.state import (
    InvestigationState,
    InvestigationStateManager,
    InvestigationStatus,
)


def test_investigation_state_defaults() -> None:
    state = InvestigationState(
        investigation_id="INC-001"
    )

    assert state.investigation_id == "INC-001"
    assert state.status == InvestigationStatus.PENDING
    assert state.current_stage is None
    assert state.completed_stages == []
    assert state.results == {}
    assert state.errors == []


def test_investigation_state_lifecycle() -> None:
    state = InvestigationState(
        investigation_id="INC-002"
    )

    state.start("risk")

    assert state.status == InvestigationStatus.RUNNING
    assert state.current_stage == "risk"

    state.complete_stage(
        "risk",
        {
            "severity": "high",
            "score": 85,
        },
    )

    assert state.current_stage is None
    assert "risk" in state.completed_stages
    assert state.results["risk"]["score"] == 85

    state.complete()

    assert state.status == InvestigationStatus.COMPLETED
    assert state.current_stage is None


def test_state_records_errors() -> None:
    state = InvestigationState(
        investigation_id="INC-003"
    )

    error = RuntimeError(
        "Provider unavailable"
    )

    state.record_error(
        "mitre",
        error,
    )

    assert len(state.errors) == 1
    assert state.errors[0]["stage"] == "mitre"
    assert (
        state.errors[0]["type"]
        == "RuntimeError"
    )
    assert (
        state.errors[0]["message"]
        == "Provider unavailable"
    )


def test_state_snapshot_is_detached() -> None:
    state = InvestigationState(
        investigation_id="INC-004"
    )

    state.record_result(
        "risk",
        {
            "score": 90,
        },
    )

    snapshot = state.snapshot()

    snapshot["results"]["risk"]["score"] = 0

    assert (
        state.results["risk"]["score"]
        == 90
    )


def test_state_rejects_invalid_status() -> None:
    with pytest.raises(ValueError):
        InvestigationState(
            investigation_id="INC-005",
            status="invalid",
        )


def test_state_manager_creates_state() -> None:
    manager = InvestigationStateManager()

    state = manager.create(
        "INC-006",
        metadata={
            "source": "endpoint",
        },
    )

    assert state.investigation_id == "INC-006"
    assert state.metadata["source"] == "endpoint"

    assert manager.exists("INC-006")
    assert manager.count() == 1
    assert manager.ids() == ["INC-006"]


def test_state_manager_rejects_duplicate() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-007")

    with pytest.raises(ValueError):
        manager.create("INC-007")


def test_state_manager_executes_lifecycle() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-008")

    manager.start(
        "INC-008",
        "detection",
    )

    manager.complete_stage(
        "INC-008",
        "detection",
        {
            "matches": [
                "suspicious_powershell"
            ]
        },
    )

    manager.set_stage(
        "INC-008",
        "mitre",
    )

    manager.complete_stage(
        "INC-008",
        "mitre",
        {
            "techniques": [
                "T1059"
            ]
        },
    )

    manager.complete(
        "INC-008"
    )

    state = manager.get(
        "INC-008"
    )

    assert state.status == (
        InvestigationStatus.COMPLETED
    )

    assert state.completed_stages == [
        "detection",
        "mitre",
    ]

    assert (
        state.results["detection"]["matches"][0]
        == "suspicious_powershell"
    )

    assert (
        state.results["mitre"]["techniques"][0]
        == "T1059"
    )


def test_state_manager_records_failure() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-009")

    manager.start(
        "INC-009",
        "threat_hunting",
    )

    manager.record_error(
        "INC-009",
        "threat_hunting",
        "Threat hunting provider failed",
    )

    manager.fail(
        "INC-009"
    )

    state = manager.get(
        "INC-009"
    )

    assert state.status == (
        InvestigationStatus.FAILED
    )

    assert len(state.errors) == 1

    assert (
        state.errors[0]["stage"]
        == "threat_hunting"
    )

    assert (
        state.errors[0]["message"]
        == "Threat hunting provider failed"
    )


def test_state_manager_snapshot() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-010")

    manager.start(
        "INC-010",
        "risk",
    )

    snapshot = manager.snapshot(
        "INC-010"
    )

    assert snapshot[
        "investigation_id"
    ] == "INC-010"

    assert snapshot[
        "status"
    ] == InvestigationStatus.RUNNING

    assert snapshot[
        "current_stage"
    ] == "risk"


def test_state_manager_remove() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-011")

    removed = manager.remove(
        "INC-011"
    )

    assert (
        removed.investigation_id
        == "INC-011"
    )

    assert not manager.exists(
        "INC-011"
    )

    assert manager.count() == 0


def test_state_manager_missing_state() -> None:
    manager = InvestigationStateManager()

    with pytest.raises(KeyError):
        manager.get("DOES-NOT-EXIST")


def test_state_manager_clear() -> None:
    manager = InvestigationStateManager()

    manager.create("INC-012")
    manager.create("INC-013")

    assert manager.count() == 2

    manager.clear()

    assert manager.count() == 0
    assert manager.ids() == []