"""
Runtime Plugin Manager Tests
"""

from services.intelligence.runtime.runtime_plugin_manager import (
    RuntimePluginManager,
)



def test_init():

    manager = RuntimePluginManager()

    assert (
        manager.count()
        ==
        0
    )



def test_register():

    manager = RuntimePluginManager()


    manager.register(
        "threat_intel",
        "intelligence",
    )


    assert (
        manager.count()
        ==
        1
    )



def test_enabled():

    manager = RuntimePluginManager()


    manager.register(
        "connector",
        "integration",
    )


    assert (
        manager.enabled(
            "connector"
        )
        is True
    )



def test_disable():

    manager = RuntimePluginManager()


    manager.register(
        "scanner",
        "security",
    )


    manager.disable(
        "scanner"
    )


    assert (
        manager.enabled(
            "scanner"
        )
        is False
    )



def test_enable():

    manager = RuntimePluginManager()


    manager.register(
        "engine",
        "ai",
        False,
    )


    manager.enable(
        "engine"
    )


    assert (
        manager.enabled(
            "engine"
        )
        is True
    )



def test_remove():

    manager = RuntimePluginManager()


    manager.register(
        "test",
        "module",
    )


    manager.remove(
        "test"
    )


    assert (
        manager.get(
            "test"
        )
        is None
    )



def test_clear():

    manager = RuntimePluginManager()


    manager.register(
        "test",
        "module",
    )


    manager.clear()


    assert (
        manager.count()
        ==
        0
    )



def test_status():

    manager = RuntimePluginManager()


    result = manager.status()


    assert "plugins" in result

    assert "count" in result