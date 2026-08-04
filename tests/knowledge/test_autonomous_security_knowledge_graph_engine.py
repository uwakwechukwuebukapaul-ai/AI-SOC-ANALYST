from services.knowledge.autonomous_security_knowledge_graph_engine import (
    AutonomousSecurityKnowledgeGraphEngine
)


def test_create_entity():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    entity = engine.create_entity(
        "ip_address",
        "192.168.1.10"
    )

    assert entity["type"] == "ip_address"


def test_create_relationship():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    attacker = engine.create_entity(
        "threat_actor",
        "APT-Test"
    )

    malware = engine.create_entity(
        "malware",
        "Example Malware"
    )

    relation = engine.create_relationship(
        attacker["id"],
        malware["id"],
        "uses"
    )

    assert relation["type"] == "uses"


def test_find_related_entities():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    actor = engine.create_entity(
        "actor",
        "APT"
    )

    tool = engine.create_entity(
        "tool",
        "Malware"
    )

    engine.create_relationship(
        actor["id"],
        tool["id"],
        "uses"
    )

    result = engine.find_related_entities(
        actor["id"]
    )

    assert len(result) == 1


def test_attack_path_mapping():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    first = engine.create_entity(
        "incident",
        "Phishing"
    )

    second = engine.create_entity(
        "ioc",
        "evil.com"
    )

    engine.create_relationship(
        first["id"],
        second["id"],
        "contains"
    )

    path = engine.map_attack_path(
        first["id"]
    )

    assert len(path) >= 1


def test_threat_cluster_analysis():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    actor = engine.create_entity(
        "threat_actor",
        "APT Group"
    )

    for item in range(3):

        entity = engine.create_entity(
            "ioc",
            f"IOC-{item}"
        )

        engine.create_relationship(
            actor["id"],
            entity["id"],
            "linked_to"
        )

    result = engine.analyze_threat_cluster(
        actor["id"]
    )

    assert result["risk_level"] == "high"


def test_graph_history():

    engine = AutonomousSecurityKnowledgeGraphEngine()

    engine.create_entity(
        "malware",
        "Test Malware"
    )

    history = engine.get_history()

    assert len(history) == 1