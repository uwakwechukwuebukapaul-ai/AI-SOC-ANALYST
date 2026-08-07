from services.intelligence.runtime.runtime_plugins import (
    RuntimePlugin,
    RuntimePluginManager,
)



def test_plugin_manager_init():

    manager = RuntimePluginManager()

    assert len(manager.plugins) == 0



def test_register_plugin():

    manager = RuntimePluginManager()


    plugin = RuntimePlugin(
        name="threat_intelligence"
    )


    manager.register(plugin)


    assert "threat_intelligence" in manager.plugins



def test_start_plugin():

    called = []


    plugin = RuntimePlugin(
        name="test",
        start_handler=lambda: called.append(True)
    )


    manager = RuntimePluginManager()

    manager.register(plugin)

    manager.start_all()


    assert called == [True]



def test_disable_plugin():

    manager = RuntimePluginManager()


    plugin = RuntimePlugin(
        name="test"
    )


    manager.register(plugin)


    manager.disable(
        "test"
    )


    assert plugin.enabled is False



def test_to_dict():

    manager = RuntimePluginManager()

    data = manager.to_dict()


    assert "plugins" in data