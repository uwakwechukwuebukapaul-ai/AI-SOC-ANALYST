"""
Runtime Audit Manager Tests
"""

from services.intelligence.runtime.runtime_audit_manager import (
    RuntimeAuditManager,
)


def test_record():

    manager = RuntimeAuditManager()

    manager.record(
        "agent",
        "runtime",
        "started",
    )

    assert manager.count() == 1


def test_latest():

    manager = RuntimeAuditManager()

    manager.record(
        "admin",
        "engine",
        "restart",
    )

    assert (
        manager.latest()["action"]
        == "restart"
    )


def test_actor_filter():

    manager = RuntimeAuditManager()

    manager.record(
        "agent1",
        "engine",
        "run",
    )

    manager.record(
        "agent2",
        "engine",
        "run",
    )

    assert len(
        manager.by_actor("agent1")
    ) == 1


def test_component_filter():

    manager = RuntimeAuditManager()

    manager.record(
        "admin",
        "database",
        "backup",
    )

    assert len(
        manager.by_component("database")
    ) == 1


def test_clear():

    manager = RuntimeAuditManager()

    manager.record(
        "a",
        "b",
        "c",
    )

    manager.clear()

    assert manager.count() == 0


def test_status():

    manager = RuntimeAuditManager()

    result = manager.status()

    assert "count" in result

    assert "latest" in result