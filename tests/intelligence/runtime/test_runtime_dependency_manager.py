"""
Runtime Dependency Manager Tests
"""

from services.intelligence.runtime.runtime_dependency_manager import (
    RuntimeDependencyManager,
)



def test_manager_init():

    manager = RuntimeDependencyManager()

    assert (
        manager.size()
        ==
        0
    )



def test_register():

    manager = RuntimeDependencyManager()

    component = object()


    manager.register(
        "database",
        component,
    )


    assert (
        manager.exists(
            "database"
        )
        is True
    )



def test_resolve():

    manager = RuntimeDependencyManager()

    component = object()


    manager.register(
        "engine",
        component,
    )


    result = manager.resolve(
        "engine"
    )


    assert result == component



def test_remove():

    manager = RuntimeDependencyManager()


    manager.register(
        "cache",
        object(),
    )


    manager.remove(
        "cache"
    )


    assert (
        manager.exists(
            "cache"
        )
        is False
    )



def test_clear():

    manager = RuntimeDependencyManager()


    manager.register(
        "service",
        object(),
    )


    manager.clear()


    assert (
        manager.size()
        ==
        0
    )



def test_status():

    manager = RuntimeDependencyManager()


    result = manager.status()


    assert "count" in result

    assert "dependencies" in result