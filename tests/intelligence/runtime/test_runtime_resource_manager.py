"""
Runtime Resource Manager Tests
"""

from services.intelligence.runtime.runtime_resource_manager import (
    RuntimeResourceManager,
)



def test_init():

    manager = RuntimeResourceManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimeResourceManager()


    manager.register(
        "workers",
        10,
    )


    assert (
        manager.count()
        ==
        1
    )



def test_allocate():

    manager = RuntimeResourceManager()


    manager.register(
        "workers",
        5,
    )


    result = manager.allocate(
        "workers",
        2,
    )


    assert result is True

    assert (
        manager.resources["workers"]["allocated"]
        ==
        2
    )



def test_capacity_limit():

    manager = RuntimeResourceManager()


    manager.register(
        "workers",
        2,
    )


    result = manager.allocate(
        "workers",
        5,
    )


    assert result is False



def test_release():

    manager = RuntimeResourceManager()


    manager.register(
        "workers",
        5,
    )


    manager.allocate(
        "workers",
        3,
    )


    manager.release(
        "workers",
        2,
    )


    assert (
        manager.resources["workers"]["allocated"]
        ==
        1
    )



def test_utilization():

    manager = RuntimeResourceManager()


    manager.register(
        "workers",
        10,
    )


    manager.allocate(
        "workers",
        5,
    )


    assert (
        manager.utilization(
            "workers"
        )
        ==
        0.5
    )



def test_clear():

    manager = RuntimeResourceManager()


    manager.register(
        "test",
        1,
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeResourceManager()


    result = manager.status()


    assert "resources" in result

    assert "count" in result