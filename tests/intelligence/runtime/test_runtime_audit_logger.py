"""
Runtime Audit Logger Tests
"""

from services.intelligence.runtime.runtime_audit_logger import (
    RuntimeAuditLogger,
)



def test_init():

    logger = RuntimeAuditLogger()

    assert (
        logger.count()
        ==
        0
    )



def test_log():

    logger = RuntimeAuditLogger()


    logger.log(
        "runtime_start",
        "system",
    )


    assert (
        logger.count()
        ==
        1
    )



def test_latest():

    logger = RuntimeAuditLogger()


    logger.log(
        "task_execute",
        "agent",
        {
            "task":
                "analysis"
        },
    )


    result = logger.latest()


    assert (
        result["action"]
        ==
        "task_execute"
    )



def test_details():

    logger = RuntimeAuditLogger()


    logger.log(
        "config_update",
        "admin",
        {
            "mode":
                "production"
        },
    )


    result = logger.latest()


    assert (
        result["details"]["mode"]
        ==
        "production"
    )



def test_clear():

    logger = RuntimeAuditLogger()


    logger.log(
        "event",
        "system",
    )


    logger.clear()


    assert (
        logger.count()
        ==
        0
    )



def test_status():

    logger = RuntimeAuditLogger()


    result = logger.status()


    assert "events" in result