"""
Runtime Dependency Manager Tests
"""

from services.intelligence.runtime.runtime_dependency_manager import (
    RuntimeDependencyManager,
)



def test_init():

    manager = RuntimeDependencyManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimeDependencyManager()


    manager.register(
        "threat_intelligence",
    )


    assert (
        manager.available(
            "threat_intelligence"
        )
        is True
    )



def test_metadata():

    manager = RuntimeDependencyManager()


    manager.register(
        "engine",
        {
            "version":
                "1.0"
        },
    )


    assert (
        manager.dependencies["engine"]["metadata"]["version"]
        ==
        "1.0"
    )



def test_disable():

    manager = RuntimeDependencyManager()


    manager.register(
        "database",
    )


    manager.disable(
        "database"
    )


    assert (
        manager.available(
            "database"
        )
        is False
    )



def test_enable():

    manager = RuntimeDependencyManager()


    manager.register(
        "database",
    )


    manager.disable(
        "database"
    )

    manager.enable(
        "database"
    )


    assert (
        manager.available(
            "database"
        )
        is True
    )



def test_remove():

    manager = RuntimeDependencyManager()


    manager.register(
        "test",
    )


    manager.remove(
        "test"
    )


    assert (
        manager.available(
            "test"
        )
        is False
    )



def test_clear():

    manager = RuntimeDependencyManager()


    manager.register(
        "test",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimeDependencyManager()


    result = manager.status()


    assert "dependencies" in result

    assert "count" in result