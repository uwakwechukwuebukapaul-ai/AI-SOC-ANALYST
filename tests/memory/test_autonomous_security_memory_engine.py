from services.memory.autonomous_security_memory_engine import (
    AutonomousSecurityMemoryEngine
)


def test_store_memory():

    engine = AutonomousSecurityMemoryEngine()

    result = engine.store_memory(
        "incident",
        "phishing attack detected"
    )

    assert result["category"] == "incident"


def test_retrieve_memory():

    engine = AutonomousSecurityMemoryEngine()

    engine.store_memory(
        "incident",
        "ransomware detected"
    )

    result = engine.retrieve_memory(
        "ransomware"
    )

    assert len(result) == 1


def test_security_pattern_learning():

    engine = AutonomousSecurityMemoryEngine()

    result = engine.learn_security_pattern(
        "credential dumping",
        "LSASS memory access"
    )

    assert result["category"] == "threat_pattern"
    assert result["confidence"] == 0.9


def test_incident_recall():

    engine = AutonomousSecurityMemoryEngine()

    result = engine.remember_incident(
        "malware",
        "isolated endpoint"
    )

    assert result["category"] == "incident"


def test_memory_confidence():

    engine = AutonomousSecurityMemoryEngine()

    memory = engine.learn_security_pattern(
        "phishing",
        "email campaign"
    )

    result = engine.calculate_memory_confidence(
        memory["id"]
    )

    assert result["level"] == "high"


def test_memory_history():

    engine = AutonomousSecurityMemoryEngine()

    engine.store_memory(
        "test",
        "security event"
    )

    assert len(engine.get_history()) == 1