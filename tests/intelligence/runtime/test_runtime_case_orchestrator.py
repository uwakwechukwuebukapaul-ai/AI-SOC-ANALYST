"""
Runtime Case Orchestrator Tests
"""

from services.intelligence.runtime.runtime_case_orchestrator import (
    RuntimeCaseOrchestrator,
)



def test_init():

    orchestrator = RuntimeCaseOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_create_case():

    orchestrator = RuntimeCaseOrchestrator()


    case_id = orchestrator.create_case(
        "Phishing Investigation"
    )


    assert (
        case_id.startswith(
            "CASE-"
        )
    )



def test_get_case():

    orchestrator = RuntimeCaseOrchestrator()


    case_id = orchestrator.create_case(
        "Threat Investigation"
    )


    result = orchestrator.get(
        case_id
    )


    assert (
        result["title"]
        ==
        "Threat Investigation"
    )



def test_add_result():

    orchestrator = RuntimeCaseOrchestrator()


    case_id = orchestrator.create_case(
        "IOC Analysis"
    )


    orchestrator.add_result(
        case_id,
        {
            "risk":
                "high"
        },
    )


    result = orchestrator.get(
        case_id
    )


    assert (
        len(
            result["results"]
        )
        ==
        1
    )



def test_close_case():

    orchestrator = RuntimeCaseOrchestrator()


    case_id = orchestrator.create_case(
        "Malware Analysis"
    )


    orchestrator.close_case(
        case_id
    )


    result = orchestrator.get(
        case_id
    )


    assert (
        result["status"]
        ==
        "closed"
    )



def test_clear():

    orchestrator = RuntimeCaseOrchestrator()


    orchestrator.create_case(
        "Test"
    )


    orchestrator.clear()


    assert (
        orchestrator.count()
        ==
        0
    )



def test_status():

    orchestrator = RuntimeCaseOrchestrator()


    result = orchestrator.status()


    assert "cases" in result