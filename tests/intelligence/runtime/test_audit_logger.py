from services.intelligence.runtime.audit_logger import (
    RuntimeAuditLogger
)


def test_logger_init():

    logger = RuntimeAuditLogger()

    assert logger.count() == 0



def test_log_event():

    logger = RuntimeAuditLogger()

    logger.log(
        "task_started"
    )

    assert logger.count() == 1



def test_log_details():

    logger = RuntimeAuditLogger()

    logger.log(
        "execution",
        actor="worker",
        details={
            "task": "analysis"
        }
    )

    entry = logger.latest()

    assert entry.actor == "worker"



def test_latest_empty():

    logger = RuntimeAuditLogger()

    assert logger.latest() is None



def test_search():

    logger = RuntimeAuditLogger()

    logger.log(
        "success"
    )

    logger.log(
        "failure"
    )

    result = logger.search(
        "success"
    )

    assert len(result) == 1



def test_clear():

    logger = RuntimeAuditLogger()

    logger.log(
        "event"
    )

    logger.clear()

    assert logger.count() == 0



def test_to_dict():

    logger = RuntimeAuditLogger()

    logger.log(
        "runtime"
    )

    data = logger.to_dict()

    assert data[0]["event"] == "runtime"