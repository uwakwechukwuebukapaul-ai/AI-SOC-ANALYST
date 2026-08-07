"""
Runtime Plugin Manager Tests
"""

from services.intelligence.runtime.runtime_plugin_manager import (
    RuntimePluginManager,
)



def test_manager_init():

    manager = RuntimePluginManager()

    assert (
        len(manager.plugins)
        ==
        0
    )



def test_register():

    manager = RuntimePluginManager()


    plugin = object()


    manager.register(
        "threat_plugin",
        plugin,
    )


    assert (
        manager.get(
            "threat_plugin"
        )
        == plugin
    )



def test_enable():

    manager = RuntimePluginManager()


    manager.register(
        "ai_plugin",
        object(),
    )


    result = manager.enable(
        "ai_plugin"
    )


    assert result is True



def test_disable():

    manager = RuntimePluginManager()


    manager.register(
        "agent_plugin",
        object(),
    )


    manager.enable(
        "agent_plugin"
    )


    manager.disable(
        "agent_plugin"
    )


    assert (
        "agent_plugin"
        not in
        manager.enabled
    )



def test_remove():

    manager = RuntimePluginManager()


    manager.register(
        "plugin",
        object(),
    )


    manager.remove(
        "plugin"
    )


    assert (
        manager.get(
            "plugin"
        )
        is None
    )



def test_status():

    manager = RuntimePluginManager()


    result = manager.status()


    assert "plugins" in result

    assert "enabled" in result

    assert "count" in result