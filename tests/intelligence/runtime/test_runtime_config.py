from services.intelligence.runtime.runtime_config import (
    RuntimeConfig
)


def test_config_init():

    config = RuntimeConfig()

    assert config.environment == "development"



def test_set_value():

    config = RuntimeConfig()

    config.set(
        "region",
        "eu"
    )

    assert config.get(
        "region"
    ) == "eu"



def test_get_default():

    config = RuntimeConfig()

    assert config.get(
        "missing",
        "default"
    ) == "default"



def test_update():

    config = RuntimeConfig()

    config.update(
        {
            "workers": 10
        }
    )

    assert config.get(
        "workers"
    ) == 10



def test_profile():

    config = RuntimeConfig()

    config.profile(
        "production"
    )

    assert config.environment == "production"



def test_reset():

    config = RuntimeConfig()

    config.set(
        "test",
        True
    )

    config.reset()

    assert config.settings == {}



def test_to_dict():

    config = RuntimeConfig()

    data = config.to_dict()

    assert "environment" in data