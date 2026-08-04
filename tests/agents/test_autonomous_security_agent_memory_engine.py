from services.agents.autonomous_security_agent_memory_engine import (
    AutonomousSecurityAgentMemoryEngine,
)


def test_store_memory():
    engine = AutonomousSecurityAgentMemoryEngine()

    memory = engine.store_memory(
        agent_id="agent-001",
        memory_type="investigation",
        event="Detected phishing campaign",
        outcome="success",
        confidence=0.95,
    )

    assert memory["agent_id"] == "agent-001"
    assert memory["outcome"] == "success"


def test_retrieve_memory():
    engine = AutonomousSecurityAgentMemoryEngine()

    engine.store_memory(
        agent_id="agent-001",
        memory_type="response",
        event="Blocked malicious domain",
        outcome="success",
    )

    memories = engine.retrieve_memory("agent-001")

    assert len(memories) == 1
    assert memories[0]["event"] == "Blocked malicious domain"


def test_search_memory():
    engine = AutonomousSecurityAgentMemoryEngine()

    engine.store_memory(
        agent_id="agent-001",
        memory_type="threat",
        event="Ransomware detection",
        outcome="success",
    )

    results = engine.search_memory("ransomware")

    assert len(results) == 1


def test_analyze_memory_pattern():
    engine = AutonomousSecurityAgentMemoryEngine()

    engine.store_memory(
        agent_id="agent-001",
        memory_type="investigation",
        event="Investigation completed",
        outcome="success",
    )

    analysis = engine.analyze_memory_pattern("agent-001")

    assert analysis["memory_count"] == 1
    assert analysis["successful_actions"] == 1
    assert analysis["status"] == "analyzed"


def test_generate_learning_recommendation():
    engine = AutonomousSecurityAgentMemoryEngine()

    engine.store_memory(
        agent_id="agent-001",
        memory_type="response",
        event="Incident response",
        outcome="failure",
    )

    result = engine.generate_learning_recommendation(
        "agent-001"
    )

    assert "optimize" in result["recommendation"]


def test_memory_history():
    engine = AutonomousSecurityAgentMemoryEngine()

    engine.store_memory(
        agent_id="agent-001",
        memory_type="learning",
        event="New threat pattern learned",
        outcome="success",
    )

    history = engine.memory_history()

    assert len(history) == 1