"""
Runtime Configuration Manager Tests
"""

from services.intelligence.runtime.runtime_configuration_manager import (
    RuntimeConfigurationManager,
)



def test_init():

    config = RuntimeConfigurationManager()

    assert (
        config.settings
        ==
        {}
    )



def test_set_get():

    config = RuntimeConfigurationManager()


    config.set(
        "environment",
        "production",
    )


    assert (
        config.get(
            "environment"
        )
        ==
        "production"
    )



def test_default():

    config = RuntimeConfigurationManager()


    assert (
        config.get(
            "missing"
        )
        is None
    )



def test_enable_feature():

    config = RuntimeConfigurationManager()


    config.enable_feature(
        "ai_investigation"
    )


    assert (
        config.feature_enabled(
            "ai_investigation"
        )
        is True
    )



def test_disable_feature():

    config = RuntimeConfigurationManager()


    config.enable_feature(
        "automation"
    )


    config.disable_feature(
        "automation"
    )


    assert (
        config.feature_enabled(
            "automation"
        )
        is False
    )



def test_clear():

    config = RuntimeConfigurationManager()


    config.set(
        "mode",
        "test",
    )


    config.clear()


    assert (
        config.settings
        ==
        {}
    )



def test_status():

    config = RuntimeConfigurationManager()


    result = config.status()


    assert "settings" in result

    assert "features" in result