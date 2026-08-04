from services.incident.autonomous_incident_response_engine import (
    AutonomousIncidentResponseEngine
)


def test_create_incident():

    engine = AutonomousIncidentResponseEngine()

    incident = engine.create_incident(
        {
            "title": "Malware Infection",
            "category": "malware",
            "risk_score": 95
        }
    )

    assert incident["severity"] == "critical"
    assert incident["status"] == "open"



def test_severity_calculation():

    engine = AutonomousIncidentResponseEngine()

    assert engine.calculate_severity(
        {"risk_score": 80}
    ) == "high"



def test_generate_response_plan():

    engine = AutonomousIncidentResponseEngine()

    incident = engine.create_incident(
        {
            "title": "Account Breach",
            "category": "credential_compromise",
            "risk_score": 90
        }
    )

    plan = engine.generate_response_plan(incident)

    assert len(plan["actions"]) > 0



def test_containment_recommendation():

    engine = AutonomousIncidentResponseEngine()

    incident = {
        "category": "malware"
    }

    actions = engine.recommend_containment(incident)

    assert "isolate endpoint" in actions



def test_incident_status_update():

    engine = AutonomousIncidentResponseEngine()

    incident = engine.create_incident(
        {
            "title": "Suspicious Login",
            "risk_score": 50
        }
    )

    updated = engine.update_status(
        incident["id"],
        "resolved"
    )

    assert updated["status"] == "resolved"



def test_clear_history():

    engine = AutonomousIncidentResponseEngine()

    engine.create_incident(
        {
            "title": "Test",
            "risk_score": 20
        }
    )

    engine.clear_history()

    assert engine.get_incident_history() == []