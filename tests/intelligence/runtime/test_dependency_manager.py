"""
Tests for Dependency Manager
"""

from services.intelligence.runtime.dependency_manager import (
    DependencyManager,
)



def test_dependency_init():

    manager = DependencyManager()

    assert manager.size() == 0



def test_register():

    manager = DependencyManager()

    manager.register(
        "engine",
        "runtime_engine",
    )

    assert manager.exists("engine")



def test_resolve():

    manager = DependencyManager()

    manager.register(
        "database",
        "sqlite",
    )

    assert manager.resolve("database") == "sqlite"



def test_remove():

    manager = DependencyManager()

    manager.register(
        "cache",
        "redis",
    )

    manager.remove("cache")

    assert manager.exists("cache") is False



def test_clear():

    manager = DependencyManager()

    manager.register(
        "service",
        "test",
    )

    manager.clear()

    assert manager.size() == 0



def test_to_dict():

    manager = DependencyManager()

    manager.register(
        "worker",
        "runtime_worker",
    )

    data = manager.to_dict()

    assert data["count"] == 1

    assert "worker" in data["dependencies"]