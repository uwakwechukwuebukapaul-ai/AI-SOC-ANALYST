"""
Sentinel DNA Runtime Health Monitor Tests
"""

from services.intelligence.runtime.health_monitor import (
    RuntimeHealthMonitor
)



def test_health_init():

    monitor = RuntimeHealthMonitor()

    assert monitor.healthy is True
    assert monitor.failures == 0



def test_heartbeat():

    monitor = RuntimeHealthMonitor()

    before = monitor.last_heartbeat

    monitor.heartbeat()

    assert monitor.last_heartbeat >= before



def test_check():

    monitor = RuntimeHealthMonitor()

    result = monitor.check()

    assert result is True
    assert monitor.checks == 1



def test_failure():

    monitor = RuntimeHealthMonitor()

    monitor.mark_failure()

    assert monitor.healthy is False
    assert monitor.failures == 1



def test_recovery():

    monitor = RuntimeHealthMonitor()

    monitor.mark_failure()

    monitor.recover()

    assert monitor.healthy is True



def test_status():

    monitor = RuntimeHealthMonitor()

    status = monitor.status()

    assert "healthy" in status
    assert "failures" in status
    assert "checks" in status