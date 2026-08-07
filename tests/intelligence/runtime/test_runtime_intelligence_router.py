"""
Runtime Intelligence Router Tests
"""

from services.intelligence.runtime.runtime_intelligence_router import (
    RuntimeIntelligenceRouter,
)

from services.intelligence.runtime.runtime_agent_runtime import (
    RuntimeAgentRuntime,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_agent():

    agent = RuntimeAgentRuntime(
        "intel_agent"
    )

    agent.add_capability(
        "threat_analysis"
    )

    agent.gateway.access.grant(
        "intel_agent",
        "execute",
    )

    agent.gateway.execution.start()


    agent.gateway.execution.workers.executor.register(
        "threat_analysis",
        lambda data: {
            "analysis":
                "complete"
        },
    )


    return agent



def create_task():

    return Task(
        capability="threat_analysis",
        payload={
            "ioc":
                "example.com"
        },
    )



def test_init():

    router = RuntimeIntelligenceRouter()

    assert (
        router.routes
        ==
        0
    )



def test_register_agent():

    router = RuntimeIntelligenceRouter()


    router.register_agent(
        create_agent()
    )


    assert (
        router.orchestrator.agent_count()
        ==
        1
    )



def test_available():

    router = RuntimeIntelligenceRouter()


    router.register_agent(
        create_agent()
    )


    assert (
        router.available(
            "threat_analysis"
        )
        is True
    )



def test_route():

    router = RuntimeIntelligenceRouter()


    router.register_agent(
        create_agent()
    )


    result = router.route(
        create_task()
    )


    assert (
        result["analysis"]
        ==
        "complete"
    )



def test_clear():

    router = RuntimeIntelligenceRouter()


    router.register_agent(
        create_agent()
    )


    router.clear()


    assert (
        router.routes
        ==
        0
    )



def test_status():

    router = RuntimeIntelligenceRouter()


    result = router.status()


    assert "routes" in result

    assert "agents" in result