"""
Runtime Health Monitor Tests
"""

from services.intelligence.runtime.runtime_health_monitor import (
    RuntimeHealthMonitor,
)



def test_init():

    monitor = RuntimeHealthMonitor()

    assert (
        monitor.checks
        ==
        0
    )



def test_health_before_start():

    monitor = RuntimeHealthMonitor()


    assert (
        monitor.healthy()
        is False
    )



def test_health_after_start():

    monitor = RuntimeHealthMonitor()


    monitor.runtime.start()


    assert (
        monitor.healthy()
        is True
    )



def test_check():

    monitor = RuntimeHealthMonitor()


    result = monitor.check()


    assert "healthy" in result

    assert "runtime" in result



def test_metrics():

    monitor = RuntimeHealthMonitor()


    result = monitor.metrics()


    assert "health_checks" in result

    assert "running" in result



def test_reset():

    monitor = RuntimeHealthMonitor()


    monitor.check()


    monitor.reset()


    assert (
        monitor.checks
        ==
        0
    )