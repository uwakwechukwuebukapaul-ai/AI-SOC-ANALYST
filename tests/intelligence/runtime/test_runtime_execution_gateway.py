"""
Runtime Execution Gateway Tests
"""

from services.intelligence.runtime.runtime_execution_gateway import (
    RuntimeExecutionGateway,
)

from services.intelligence.runtime.task import (
    Task,
)



def create_task():

    return Task(
        capability="analysis",
        payload={
            "test":
                True
        },
    )



def test_init():

    gateway = RuntimeExecutionGateway()

    assert gateway is not None



def test_execute_allowed():

    gateway = RuntimeExecutionGateway()


    gateway.start()


    gateway.access.grant(
        "agent",
        "execute",
    )


    gateway.execution.workers.executor.register(
        "analysis",
        lambda data: {
            "ok":
                True
        },
    )


    result = gateway.execute(
        "agent",
        "execute",
        create_task(),
    )


    assert (
        result["ok"]
        is True
    )



def test_execute_denied():

    gateway = RuntimeExecutionGateway()


    gateway.start()


    result = gateway.execute(
        "unknown",
        "execute",
        create_task(),
    )


    assert result is None



def test_audit_created():

    gateway = RuntimeExecutionGateway()


    gateway.execute(
        "unknown",
        "execute",
        create_task(),
    )


    assert (
        gateway.audit.count()
        ==
        1
    )



def test_status():

    gateway = RuntimeExecutionGateway()


    result = gateway.status()


    assert "access" in result

    assert "execution" in result

    assert "audit" in result