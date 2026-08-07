"""
Runtime Lifecycle Manager Tests
"""

from services.intelligence.runtime.runtime_lifecycle_manager import (
    RuntimeLifecycleManager,
)


def test_register():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    assert manager.count() == 1


def test_start():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    assert manager.start("engine") is True

    assert manager.state("engine") == "running"


def test_stop():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    manager.stop("engine")

    assert manager.state("engine") == "stopped"


def test_restart():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    manager.restart("engine")

    assert manager.state("engine") == "running"


def test_terminate():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    manager.terminate("engine")

    assert manager.state("engine") == "terminated"


def test_missing_component():

    manager = RuntimeLifecycleManager()

    assert manager.start("missing") is False

    assert manager.state("missing") is None


def test_clear():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    manager.clear()

    assert manager.count() == 0


def test_status():

    manager = RuntimeLifecycleManager()

    manager.register("engine")

    result = manager.status()

    assert "components" in result

    assert "count" in result