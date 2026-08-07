"""
Runtime Resource Manager Tests
"""

from services.intelligence.runtime.runtime_resource_manager import (
    RuntimeResourceManager,
)


def test_register():

    manager = RuntimeResourceManager()

    manager.register(
        "workers",
        5,
    )

    assert manager.count() == 1


def test_allocate():

    manager = RuntimeResourceManager()

    manager.register(
        "workers",
        5,
    )

    assert manager.allocate(
        "workers",
        2,
    ) is True

    assert manager.available(
        "workers"
    ) == 3


def test_allocate_failure():

    manager = RuntimeResourceManager()

    manager.register(
        "workers",
        2,
    )

    assert manager.allocate(
        "workers",
        3,
    ) is False


def test_release():

    manager = RuntimeResourceManager()

    manager.register(
        "workers",
        4,
    )

    manager.allocate(
        "workers",
        3,
    )

    manager.release(
        "workers",
        2,
    )

    assert manager.available(
        "workers"
    ) == 3


def test_available_missing():

    manager = RuntimeResourceManager()

    assert manager.available(
        "missing"
    ) == 0


def test_clear():

    manager = RuntimeResourceManager()

    manager.register(
        "workers",
        1,
    )

    manager.clear()

    assert manager.count() == 0


def test_status():

    manager = RuntimeResourceManager()

    result = manager.status()

    assert "count" in result

    assert "resources" in result