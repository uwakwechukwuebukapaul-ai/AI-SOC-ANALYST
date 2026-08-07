from services.intelligence.runtime.runtime_registry import RuntimeRegistry



def test_default_registry():

    registry = RuntimeRegistry()

    assert registry.agents == {}

    assert registry.handlers == {}



def test_register_agent():

    registry = RuntimeRegistry()

    agent = object()

    registry.register_agent(
        "analyst",
        agent
    )

    assert registry.get_agent(
        "analyst"
    ) == agent



def test_register_handler():

    registry = RuntimeRegistry()

    handler = object()

    registry.register_handler(
        "email",
        handler
    )

    assert registry.get_handler(
        "email"
    ) == handler



def test_register_capability():

    registry = RuntimeRegistry()

    registry.register_capability(
        "investigation",
        True
    )

    assert registry.get_capability(
        "investigation"
    ) is True



def test_clear():

    registry = RuntimeRegistry()

    registry.register_agent(
        "test",
        object()
    )

    registry.clear()

    assert registry.agents == {}



def test_to_dict():

    registry = RuntimeRegistry()

    data = registry.to_dict()

    assert "agents" in data
    assert "handlers" in data
    assert "capabilities" in data