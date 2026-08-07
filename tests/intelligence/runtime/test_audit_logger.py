"""
Tests for Runtime Audit Logger
"""

from services.intelligence.runtime.audit_logger import (
    AuditLogger,
)



def test_logger_init():

    logger = AuditLogger()

    assert logger.count() == 0



def test_log_event():

    logger = AuditLogger()

    event = logger.log(
        "task_started",
        {
            "task_id": "123"
        }
    )

    assert event["action"] == "task_started"

    assert logger.count() == 1



def test_get_events():

    logger = AuditLogger()

    logger.log(
        "runtime_start"
    )

    events = logger.get_events()

    assert len(events) == 1



def test_latest():

    logger = AuditLogger()

    logger.log(
        "first"
    )

    logger.log(
        "second"
    )

    assert logger.latest()["action"] == "second"



def test_clear():

    logger = AuditLogger()

    logger.log(
        "event"
    )

    logger.clear()

    assert logger.count() == 0



def test_to_dict():

    logger = AuditLogger()

    logger.log(
        "audit_test"
    )

    data = logger.to_dict()

    assert data["total_events"] == 1