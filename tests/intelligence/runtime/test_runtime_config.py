from services.intelligence.runtime.runtime_config import (
    RuntimeConfig,
)


def test_config_init():

    config = RuntimeConfig()

    assert config.max_workers == 4



def test_update():

    config = RuntimeConfig()

    config.update(
        "max_workers",
        10,
    )

    assert config.max_workers == 10



def test_metadata_update():

    config = RuntimeConfig()

    config.update(
        "region",
        "eu-west",
    )

    assert config.metadata["region"] == "eu-west"



def test_get():

    config = RuntimeConfig()

    assert config.get(
        "max_retries"
    ) == 3



def test_to_dict():

    config = RuntimeConfig()

    data = config.to_dict()

    assert "max_workers" in data