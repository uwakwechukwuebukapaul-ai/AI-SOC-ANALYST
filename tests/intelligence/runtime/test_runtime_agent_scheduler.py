"""
Runtime Agent Scheduler Tests
"""

from services.intelligence.runtime.runtime_agent_scheduler import (
    RuntimeAgentScheduler,
)



def test_init():

    scheduler = RuntimeAgentScheduler()

    assert (
        len(
            scheduler.agents
        )
        ==
        0
    )



def test_register_agent():

    scheduler = RuntimeAgentScheduler()


    scheduler.register_agent(
        "investigator",
        [
            "investigate",
        ],
    )


    assert (
        "investigator"
        in
        scheduler.agents
    )



def test_schedule():

    scheduler = RuntimeAgentScheduler()


    scheduler.register_agent(
        "intel_agent",
        [
            "ioc_lookup",
        ],
    )


    result = scheduler.schedule(
        "ioc_lookup",
        {
            "ioc": "test"
        },
    )


    assert (
        result
        ==
        "intel_agent"
    )



def test_missing_capability():

    scheduler = RuntimeAgentScheduler()


    scheduler.register_agent(
        "agent",
        [
            "scan",
        ],
    )


    result = scheduler.schedule(
        "investigate",
        {},
    )


    assert result is None



def test_workload():

    scheduler = RuntimeAgentScheduler()


    scheduler.register_agent(
        "agent",
        [
            "analysis",
        ],
    )


    scheduler.schedule(
        "analysis",
        {},
    )


    assert (
        scheduler.workload(
            "agent"
        )
        ==
        1
    )



def test_status():

    scheduler = RuntimeAgentScheduler()


    result = scheduler.status()


    assert "agents" in result

    assert "assignments" in result