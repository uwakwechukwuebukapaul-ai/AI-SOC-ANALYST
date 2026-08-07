from services.intelligence.runtime.runtime_audit import (
    RuntimeAudit,
)


def test_audit_init():

    audit = RuntimeAudit()

    assert audit.count() == 0



def test_record():

    audit = RuntimeAudit()

    entry = audit.record(
        "task_started",
        {
            "task_id": "123"
        }
    )

    assert entry.event == "task_started"
    assert audit.count() == 1



def test_latest():

    audit = RuntimeAudit()

    audit.record("event_one")
    audit.record("event_two")

    result = audit.latest()

    assert len(result) == 2
    assert result[0]["event"] == "event_one"



def test_clear():

    audit = RuntimeAudit()

    audit.record("test")

    audit.clear()

    assert audit.count() == 0



def test_to_dict():

    audit = RuntimeAudit()

    audit.record(
        "runtime_started"
    )

    result = audit.to_dict()

    assert result["count"] == 1
    assert len(result["entries"]) == 1