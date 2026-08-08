"""
Sentinel DNA Investigation Runtime E2E Test

Validates:

Agent Bootstrap
        |
        v
Agent Registry
        |
        v
Runtime Adapter
        |
        v
Runtime Task Executor
        |
        v
Investigation Coordinator
        |
        v
Agent Pipeline Execution
"""

from services.intelligence.agents.agent_registry import (
    AgentRegistry,
)

from services.intelligence.agents.bootstrap import (
    bootstrap_agents,
)

from services.intelligence.agents.runtime_adapter import (
    AgentRuntimeAdapter,
)

from services.intelligence.runtime.runtime_task_executor import (
    RuntimeTaskExecutor,
)

from services.intelligence.orchestration.investigation_coordinator import (
    InvestigationCoordinator,
)


def test_investigation_runtime_e2e():

    # --------------------------------------------------
    # Agent registry
    # --------------------------------------------------

    registry = AgentRegistry()


    # --------------------------------------------------
    # Runtime executor
    # --------------------------------------------------

    executor = RuntimeTaskExecutor()


    # --------------------------------------------------
    # Runtime bridge
    # --------------------------------------------------

    runtime_adapter = AgentRuntimeAdapter(
        executor,
    )


    # --------------------------------------------------
    # Bootstrap agents
    #
    # Registers:
    # - Agent Registry
    # - Runtime capabilities
    # --------------------------------------------------

    bootstrap_agents(
        registry,
        runtime_adapter=runtime_adapter,
    )


    # Verify runtime wiring

    status = executor.status()

    assert len(
        status["handlers"]
    ) > 0


    # --------------------------------------------------
    # Investigation Coordinator
    # --------------------------------------------------

    coordinator = InvestigationCoordinator(
        registry=registry,
        runtime=executor,
    )


    alert = {
        "source": "email",
        "indicator": "malicious-domain.xyz",
        "severity": "high",
    }


    # --------------------------------------------------
    # Execute investigation
    # --------------------------------------------------

    result = coordinator.investigate(
        case_id="CASE-001",
        alert=alert,
    )


    # --------------------------------------------------
    # Assertions
    # --------------------------------------------------

    assert result is not None


    assert result.plan_name == (
        "Standard Security Investigation"
    )


    assert len(
        result.results
    ) > 0


    assert len(
        result.errors
    ) == 0