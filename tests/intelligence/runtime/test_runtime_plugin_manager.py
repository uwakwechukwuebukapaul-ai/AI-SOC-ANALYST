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
        "virustotal",
        {
            "type":
                "threat_intel"
        },
    )


    assert (
        manager.active(
            "virustotal"
        )
        is True
    )



def test_disable():

    manager = RuntimePluginManager()


    manager.register(
        "connector",
        {},
    )


    manager.disable(
        "connector"
    )


    assert (
        manager.active(
            "connector"
        )
        is False
    )



def test_enable():

    manager = RuntimePluginManager()


    manager.register(
        "connector",
        {},
    )


    manager.disable(
        "connector"
    )

    manager.enable(
        "connector"
    )


    assert (
        manager.active(
            "connector"
        )
        is True
    )



def test_remove():

    manager = RuntimePluginManager()


    manager.register(
        "test",
        {},
    )


    manager.remove(
        "test"
    )


    assert (
        manager.active(
            "test"
        )
        is False
    )



def test_clear():

    manager = RuntimePluginManager()


    manager.register(
        "test",
        {},
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