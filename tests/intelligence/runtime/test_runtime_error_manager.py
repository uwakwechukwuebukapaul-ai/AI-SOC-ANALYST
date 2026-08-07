"""
Runtime Error Manager Tests
"""

from services.intelligence.runtime.runtime_error_manager import (
    RuntimeErrorManager,
)



def test_init():

    manager = RuntimeErrorManager()

    assert (
        manager.count()
        ==
        0
    )



def test_record():

    manager = RuntimeErrorManager()


    manager.record(
        "ai_engine",
        "timeout",
    )


    assert (
        manager.count()
        ==
        1
    )



def test_latest():

    manager = RuntimeErrorManager()


    manager.record(
        "database",
        "connection_failed",
    )


    result = manager.latest()


    assert (
        result["component"]
        ==
        "database"
    )



def test_severity():

    manager = RuntimeErrorManager()


    manager.record(
        "agent",
        "blocked",
        "critical",
    )


    result = manager.latest()


    assert (
        result["severity"]
        ==
        "critical"
    )



def test_by_component():

    manager = RuntimeErrorManager()


    manager.record(
        "api",
        "failure",
    )


    manager.record(
        "database",
        "failure",
    )


    result = manager.by_component(
        "api"
    )


    assert (
        len(result)
        ==
        1
    )



def test_clear():

    manager = RuntimeErrorManager()


    manager.record(
        "test",
        "error",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeErrorManager()


    result = manager.status()


    assert "errors" in result

    assert "count" in result