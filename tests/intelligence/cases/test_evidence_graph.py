from services.intelligence.cases.evidence_graph import (
    EvidenceGraph,
)


def test_evidence_graph():

    graph = EvidenceGraph()


    graph.add_entity(
        "ioc-1",
        "domain",
        {
            "value": "evil.xyz"
        },
    )


    graph.add_entity(
        "case-1",
        "case",
        {},
    )


    graph.add_relationship(
        "case-1",
        "ioc-1",
        "contains",
    )


    result = graph.get_graph()


    assert len(
        result["nodes"]
    ) == 2


    assert len(
        result["edges"]
    ) == 1