from services.intelligence.runtime.runtime_state import (
    RuntimeStateManager,
)



def test_state_init():

    manager = RuntimeStateManager()

    assert (
        manager.get_status()
        ==
        "initialized"
    )



def test_set_status():

    manager = RuntimeStateManager()

    manager.set_status(
        "running"
    )

    assert (
        manager.get_status()
        ==
        "running"
    )



def test_component():

    manager = RuntimeStateManager()

    manager.set_component(
        "worker",
        "healthy",
    )

    assert (
        manager.get_component(
            "worker"
        )
        ==
        "healthy"
    )



def test_metadata():

    manager = RuntimeStateManager()

    manager.set_metadata(
        "version",
        "1.0",
    )

    snapshot = manager.snapshot()

    assert (
        snapshot["metadata"]["version"]
        ==
        "1.0"
    )



def test_snapshot():

    manager = RuntimeStateManager()

    result = manager.snapshot()

    assert "status" in result

    assert "components" in result



def test_reset():

    manager = RuntimeStateManager()

    manager.set_status(
        "running"
    )

    manager.reset()

    assert (
        manager.get_status()
        ==
        "initialized"
    )