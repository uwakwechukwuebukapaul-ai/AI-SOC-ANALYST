"""
Runtime Intelligence Gateway Tests
"""

from services.intelligence.runtime.runtime_intelligence_gateway import (
    RuntimeIntelligenceGateway,
)



def test_init():

    gateway = RuntimeIntelligenceGateway()

    assert (
        gateway.requests
        ==
        0
    )



def test_register_agent():

    gateway = RuntimeIntelligenceGateway()


    gateway.register_agent(
        "investigator",
        [
            "investigate",
        ],
    )


    assert (
        gateway.available(
            "investigate"
        )
        is True
    )



def test_submit_request():

    gateway = RuntimeIntelligenceGateway()


    gateway.register_agent(
        "intel_agent",
        [
            "ioc_lookup",
        ],
    )


    result = gateway.submit_request(
        "ioc_lookup",
        {
            "ioc":
                "example.com"
        },
    )


    assert (
        result
        ==
        "intel_agent"
    )



def test_missing_capability():

    gateway = RuntimeIntelligenceGateway()


    result = gateway.submit_request(
        "unknown",
        {},
    )


    assert result is None



def test_clear():

    gateway = RuntimeIntelligenceGateway()


    gateway.register_agent(
        "agent",
        [],
    )


    gateway.clear()


    assert (
        gateway.orchestrator.agent_count()
        ==
        0
    )



def test_status():

    gateway = RuntimeIntelligenceGateway()


    result = gateway.status()


    assert "requests" in result

    assert "orchestrator" in result