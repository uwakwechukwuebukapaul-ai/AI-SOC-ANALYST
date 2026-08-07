"""
Runtime Configuration Manager Tests
"""

from services.intelligence.runtime.runtime_configuration_manager import (
    RuntimeConfigurationManager,
)



def test_manager_init():

    manager = RuntimeConfigurationManager()

    assert (
        manager.configuration
        ==
        {}
    )



def test_set():

    manager = RuntimeConfigurationManager()


    manager.set(
        "environment",
        "production",
    )


    assert (
        manager.get(
            "environment"
        )
        ==
        "production"
    )



def test_exists():

    manager = RuntimeConfigurationManager()


    manager.set(
        "mode",
        "secure",
    )


    assert (
        manager.exists(
            "mode"
        )
        is True
    )



def test_remove():

    manager = RuntimeConfigurationManager()


    manager.set(
        "debug",
        True,
    )


    manager.remove(
        "debug"
    )


    assert (
        manager.exists(
            "debug"
        )
        is False
    )



def test_update():

    manager = RuntimeConfigurationManager()


    manager.update(
        {
            "workers": 5,
            "timeout": 30,
        }
    )


    assert (
        manager.get(
            "workers"
        )
        ==
        5
    )



def test_clear():

    manager = RuntimeConfigurationManager()


    manager.set(
        "key",
        "value",
    )


    manager.clear()


    assert (
        manager.configuration
        ==
        {}
    )



def test_status():

    manager = RuntimeConfigurationManager()


    result = manager.status()


    assert "count" in result

    assert "configuration" in result