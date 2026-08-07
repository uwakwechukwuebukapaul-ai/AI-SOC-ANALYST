"""
Runtime Incident Orchestrator Tests
"""

from services.intelligence.runtime.runtime_incident_orchestrator import (
    RuntimeIncidentOrchestrator,
)



def test_init():

    orchestrator = RuntimeIncidentOrchestrator()

    assert (
        orchestrator.count()
        ==
        0
    )



def test_create_incident():

    orchestrator = RuntimeIncidentOrchestrator()


    incident_id = orchestrator.create_incident(
        "Suspicious Login",
        "high",
    )


    assert (
        incident_id.startswith(
            "INC-"
        )
    )



def test_get_incident():

    orchestrator = RuntimeIncidentOrchestrator()


    incident_id = orchestrator.create_incident(
        "Malware Detection"
    )


    result = orchestrator.get(
        incident_id
    )


    assert (
        result["title"]
        ==
        "Malware Detection"
    )



def test_update_status():

    orchestrator = RuntimeIncidentOrchestrator()


    incident_id = orchestrator.create_incident(
        "Threat Alert"
    )


    orchestrator.update_status(
        incident_id,
        "investigating",
    )


    result = orchestrator.get(
        incident_id
    )


    assert (
        result["status"]
        ==
        "investigating"
    )



def test_update_severity():

    orchestrator = RuntimeIncidentOrchestrator()


    incident_id = orchestrator.create_incident(
        "Critical Threat",
        "medium",
    )


    orchestrator.update_severity(
        incident_id,
        "critical",
    )


    result = orchestrator.get(
        incident_id
    )


    assert (
        result["severity"]
        ==
        "critical"
    )



def test_clear():

    orchestrator = RuntimeIncidentOrchestrator()


    orchestrator.create_incident(
        "Test Incident"
    )


    orchestrator.clear()


    assert (
        orchestrator.count()
        ==
        0
    )



def test_status():

    orchestrator = RuntimeIncidentOrchestrator()


    result = orchestrator.status()


    assert "incidents" in result