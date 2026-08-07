"""
Runtime Health Monitor Tests
"""

from services.intelligence.runtime.runtime_health_monitor import (
    RuntimeHealthMonitor,
)


def test_init():

    monitor = RuntimeHealthMonitor()

    assert monitor.count() == 0


def test_register():

    monitor = RuntimeHealthMonitor()

    monitor.register("database")

    assert monitor.count() == 1


def test_update():

    monitor = RuntimeHealthMonitor()

    monitor.register("database")

    monitor.update(
        "database",
        "degraded",
    )

    assert (
        monitor.get("database")["status"]
        == "degraded"
    )


def test_get():

    monitor = RuntimeHealthMonitor()

    monitor.register("engine")

    assert (
        monitor.get("engine")["status"]
        == "healthy"
    )


def test_overall_health():

    monitor = RuntimeHealthMonitor()

    monitor.register("engine")

    monitor.register("database")

    assert monitor.healthy() is True

    monitor.update(
        "database",
        "failed",
    )

    assert monitor.healthy() is False


def test_clear():

    monitor = RuntimeHealthMonitor()

    monitor.register("test")

    monitor.clear()

    assert monitor.count() == 0


def test_status():

    monitor = RuntimeHealthMonitor()

    result = monitor.status()

    assert "healthy" in result

    assert "components" in result

    assert "count" in result