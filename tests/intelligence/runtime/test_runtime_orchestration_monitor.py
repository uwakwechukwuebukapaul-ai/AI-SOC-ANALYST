"""
Runtime Orchestration Monitor Tests
"""

from services.intelligence.runtime.runtime_orchestration_monitor import (
    RuntimeOrchestrationMonitor,
)



def test_init():

    monitor = RuntimeOrchestrationMonitor()

    assert (
        monitor.count()
        ==
        0
    )



def test_register():

    monitor = RuntimeOrchestrationMonitor()


    monitor.register(
        "workflow01",
        "investigation",
    )


    assert (
        monitor.count()
        ==
        1
    )



def test_update():

    monitor = RuntimeOrchestrationMonitor()


    monitor.register(
        "workflow01",
        "analysis",
    )


    monitor.update(
        "workflow01",
        "running",
    )


    assert (
        monitor.get(
            "workflow01"
        )["status"]
        ==
        "running"
    )



def test_get_missing():

    monitor = RuntimeOrchestrationMonitor()


    assert (
        monitor.get(
            "missing"
        )
        is None
    )



def test_active():

    monitor = RuntimeOrchestrationMonitor()


    monitor.register(
        "workflow01",
        "incident",
    )


    assert (
        len(
            monitor.active()
        )
        ==
        1
    )



def test_clear():

    monitor = RuntimeOrchestrationMonitor()


    monitor.register(
        "test",
        "workflow",
    )


    monitor.clear()


    assert (
        monitor.count()
        ==
        0
    )



def test_status():

    monitor = RuntimeOrchestrationMonitor()


    result = monitor.status()


    assert "workflows" in result

    assert "active" in result