"""
Runtime Scheduler Tests
"""

from services.intelligence.runtime.runtime_scheduler import (
    RuntimeScheduler,
)


def test_register():

    scheduler = RuntimeScheduler()

    scheduler.register(
        "job",
        lambda: None,
    )

    assert scheduler.count() == 1


def test_execute():

    scheduler = RuntimeScheduler()

    executed = []

    def job():
        executed.append(True)

    scheduler.register(
        "job",
        job,
    )

    assert scheduler.run("job") is True

    assert executed == [True]


def test_disabled():

    scheduler = RuntimeScheduler()

    scheduler.register(
        "job",
        lambda: None,
        enabled=False,
    )

    assert scheduler.run("job") is False


def test_enable():

    scheduler = RuntimeScheduler()

    scheduler.register(
        "job",
        lambda: None,
        enabled=False,
    )

    scheduler.enable("job")

    assert scheduler.run("job") is True


def test_remove():

    scheduler = RuntimeScheduler()

    scheduler.register(
        "job",
        lambda: None,
    )

    scheduler.remove("job")

    assert scheduler.exists("job") is False


def test_clear():

    scheduler = RuntimeScheduler()

    scheduler.register(
        "job",
        lambda: None,
    )

    scheduler.clear()

    assert scheduler.count() == 0


def test_status():

    scheduler = RuntimeScheduler()

    result = scheduler.status()

    assert "count" in result

    assert "tasks" in result