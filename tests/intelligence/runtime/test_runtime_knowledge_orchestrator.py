"""
Runtime Knowledge Orchestrator Tests
"""

from services.intelligence.runtime.runtime_knowledge_orchestrator import (
    RuntimeKnowledgeOrchestrator,
)



def test_init():

    knowledge = RuntimeKnowledgeOrchestrator()

    assert (
        len(
            knowledge.entities
        )
        ==
        0
    )



def test_add_entity():

    knowledge = RuntimeKnowledgeOrchestrator()


    knowledge.add_entity(
        "ioc_001",
        {
            "type":
                "domain"
        },
    )


    result = knowledge.get_entity(
        "ioc_001"
    )


    assert (
        result["type"]
        ==
        "domain"
    )



def test_relationship():

    knowledge = RuntimeKnowledgeOrchestrator()


    knowledge.add_relationship(
        "ioc_001",
        "actor_001",
        "associated_with",
    )


    result = knowledge.related(
        "ioc_001"
    )


    assert (
        len(result)
        ==
        1
    )



def test_missing_entity():

    knowledge = RuntimeKnowledgeOrchestrator()


    result = knowledge.get_entity(
        "missing"
    )


    assert result is None



def test_clear():

    knowledge = RuntimeKnowledgeOrchestrator()


    knowledge.add_entity(
        "test",
        {},
    )


    knowledge.clear()


    assert (
        len(
            knowledge.entities
        )
        ==
        0
    )



def test_status():

    knowledge = RuntimeKnowledgeOrchestrator()


    result = knowledge.status()


    assert "entities" in result

    assert "relationships" in result