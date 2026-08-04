from services.memory.autonomous_security_memory_engine import (
    AutonomousSecurityMemoryEngine
)



def test_store_memory():

    engine = AutonomousSecurityMemoryEngine()


    result = engine.store_memory(
        "IOC",
        "Malicious phishing domain detected",
        "HIGH"
    )


    assert result["type"] == "IOC"

    assert engine.get_memory_count() == 1




def test_recall_memory():

    engine = AutonomousSecurityMemoryEngine()


    engine.store_memory(
        "INCIDENT",
        "Ransomware attack detected"
    )


    results = engine.recall_memory(
        "Ransomware"
    )


    assert len(results) == 1




def test_learn_pattern():

    engine = AutonomousSecurityMemoryEngine()


    result = engine.learn_pattern(
        "Credential dumping behavior",
        0.95
    )


    assert result["type"] == "THREAT_PATTERN"

    assert result["confidence"] == 0.95




def test_memory_history():

    engine = AutonomousSecurityMemoryEngine()


    engine.store_memory(
        "ALERT",
        "Suspicious login"
    )


    history = engine.get_history()


    assert len(history) == 1




def test_multiple_memories():

    engine = AutonomousSecurityMemoryEngine()


    engine.store_memory(
        "IOC",
        "Malware hash"
    )


    engine.store_memory(
        "IOC",
        "Phishing URL"
    )


    assert engine.get_memory_count() == 2




def test_clear_memory():

    engine = AutonomousSecurityMemoryEngine()


    engine.store_memory(
        "TEST",
        "Temporary memory"
    )


    result = engine.clear_memory()


    assert result is True

    assert engine.get_memory_count() == 0