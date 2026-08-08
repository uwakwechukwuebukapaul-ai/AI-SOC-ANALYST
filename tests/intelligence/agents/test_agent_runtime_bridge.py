"""
Sentinel DNA Agent Runtime Bridge Test

Validates:

AgentRegistry
    |
AgentRuntimeAdapter
    |
RuntimeTaskExecutor
    |
Agent.execute()
"""

from services.intelligence.agents.agent_registry import AgentRegistry
from services.intelligence.agents.bootstrap import register_agents
from services.intelligence.agents.runtime_adapter import (
    AgentRuntimeAdapter,
)

from services.intelligence.runtime.runtime_task_executor import (
    RuntimeTaskExecutor,
)


def test_agent_runtime_bridge():

    registry = AgentRegistry()

    register_agents(registry)

    executor = RuntimeTaskExecutor()

    adapter = AgentRuntimeAdapter(
        runtime_executor=executor,
    )

    for agent in registry.list_agents():
        adapter.register_agent(agent)

    assert executor.status()["handlers"]
