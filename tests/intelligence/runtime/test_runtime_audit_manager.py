"""
Runtime Audit Manager Tests
"""

from services.intelligence.runtime.runtime_audit_manager import (
    RuntimeAuditManager,
)



def test_manager_init():

    manager = RuntimeAuditManager()

    assert (
        manager.size()
        ==
        0
    )



def test_record():

    manager = RuntimeAuditManager()


    event_id = manager.record(
        "task_execute",
        "analyst",
    )


    assert (
        event_id
        is not None
    )

    assert (
        manager.size()
        ==
        1
    )



def test_get():

    manager = RuntimeAuditManager()


    event_id = manager.record(
        "login",
        "user",
    )


    event = manager.get(
        event_id
    )


    assert (
        event["action"]
        ==
        "login"
    )



def test_query():

    manager = RuntimeAuditManager()


    manager.record(
        "scan",
        "agent",
    )


    results = manager.query(
        "agent"
    )


    assert (
        len(results)
        ==
        1
    )



def test_clear():

    manager = RuntimeAuditManager()


    manager.record(
        "event",
        "system",
    )


    manager.clear()


    assert (
        manager.size()
        ==
        0
    )



def test_status():

    manager = RuntimeAuditManager()


    result = manager.status()


    assert "events" in result

    assert "latest" in result