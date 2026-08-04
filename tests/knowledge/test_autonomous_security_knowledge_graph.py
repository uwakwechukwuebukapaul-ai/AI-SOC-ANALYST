from services.knowledge.autonomous_security_knowledge_graph import (
    AutonomousSecurityKnowledgeGraph
)


def test_add_entity():

    graph = AutonomousSecurityKnowledgeGraph()

    entity = graph.add_entity(
        "user01",
        "user",
        {"department": "finance"}
    )

    assert entity["id"] == "user01"
    assert entity["type"] == "user"


def test_get_entity():

    graph = AutonomousSecurityKnowledgeGraph()

    graph.add_entity(
        "malware01",
        "malware"
    )

    result = graph.get_entity("malware01")

    assert result["type"] == "malware"


def test_add_relationship():

    graph = AutonomousSecurityKnowledgeGraph()

    graph.add_entity("attacker", "threat_actor")
    graph.add_entity("technique", "mitre_attack")

    relationship = graph.add_relationship(
        "attacker",
        "uses",
        "technique"
    )

    assert relationship["relation"] == "uses"


def test_attack_path_generation():

    graph = AutonomousSecurityKnowledgeGraph()

    graph.add_relationship(
        "attacker",
        "targets",
        "endpoint"
    )

    graph.add_relationship(
        "endpoint",
        "creates",
        "incident"
    )

    path = graph.find_attack_path(
        "attacker",
        "incident"
    )

    assert path == [
        "attacker",
        "endpoint",
        "incident"
    ]


def test_learning_pattern():

    graph = AutonomousSecurityKnowledgeGraph()

    graph.add_entity(
        "ip01",
        "ip_address"
    )

    graph.add_entity(
        "ip02",
        "ip_address"
    )

    result = graph.learn_pattern(
        "ip_address"
    )

    assert result["count"] == 2


def test_clear_graph():

    graph = AutonomousSecurityKnowledgeGraph()

    graph.add_entity(
        "incident01",
        "incident"
    )

    graph.clear_graph()

    assert len(graph.entities) == 0
    assert len(graph.relationships) == 0