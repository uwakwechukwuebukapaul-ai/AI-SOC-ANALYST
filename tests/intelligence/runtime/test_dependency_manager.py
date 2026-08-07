from services.intelligence.runtime.dependency_manager import (
    DependencyManager
)


def test_manager_init():

    manager = DependencyManager()

    assert manager.dependencies == {}



def test_register():

    manager = DependencyManager()

    manager.register(
        "database"
    )

    assert "database" in manager.dependencies



def test_check_without_checker():

    manager = DependencyManager()

    manager.register(
        "cache"
    )

    assert manager.check(
        "cache"
    ) is True



def test_check_with_checker():

    manager = DependencyManager()

    manager.register(
        "api",
        checker=lambda: True
    )

    assert manager.check(
        "api"
    ) is True



def test_check_failure():

    manager = DependencyManager()

    manager.register(
        "service",
        checker=lambda: False
    )

    assert manager.check(
        "service"
    ) is False



def test_remove():

    manager = DependencyManager()

    manager.register(
        "queue"
    )

    manager.remove(
        "queue"
    )

    assert "queue" not in manager.dependencies



def test_clear():

    manager = DependencyManager()

    manager.register(
        "worker"
    )

    manager.clear()

    assert manager.dependencies == {}



def test_status():

    manager = DependencyManager()

    manager.register(
        "engine"
    )

    data = manager.to_dict()

    assert "engine" in data