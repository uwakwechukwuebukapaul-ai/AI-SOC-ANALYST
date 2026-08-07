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



def test_record():

    logger = RuntimeAuditLogger()


    logger.record(
        "ai_agent",
        "investigate_case",
    )


    assert (
        logger.count()
        ==
        1
    )



def test_latest():

    logger = RuntimeAuditLogger()


    logger.record(
        "analyst",
        "approve",
        {
            "case":
                "INC001"
        },
    )


    result = logger.latest()


    assert (
        result["actor"]
        ==
        "analyst"
    )



def test_details():

    logger = RuntimeAuditLogger()


    logger.record(
        "system",
        "scan",
        {
            "target":
                "email"
        },
    )


    result = logger.latest()


    assert (
        result["details"]["target"]
        ==
        "email"
    )



def test_empty_latest():

    logger = RuntimeAuditLogger()


    assert (
        logger.latest()
        is None
    )



def test_clear():

    logger = RuntimeAuditLogger()


    logger.record(
        "test",
        "action",
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


    assert "records" in result