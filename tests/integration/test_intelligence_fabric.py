from services.intelligence_fabric import (
    EventNormalizer,
    EntityResolver,
    EvidencePipeline,
    InvestigationContextManager,
    IntelligenceGraph,
)



def test_event_normalization():

    engine = EventNormalizer()


    result = engine.normalize(
        {
            "event": "suspicious_login",
            "source": "endpoint",
            "severity": "high",
            "src_ip": "10.0.0.5"
        }
    )


    assert result["event_type"] == "suspicious_login"

    assert len(
        result["indicators"]
    ) == 1



def test_entity_resolution():

    resolver = EntityResolver()


    result = resolver.resolve(
        {
            "type": "ip",
            "value": "10.0.0.5"
        }
    )


    assert result["type"] == "ip"



def test_evidence_pipeline():

    pipeline = EvidencePipeline()


    result = pipeline.process(
        {
            "event": "malware_detected"
        }
    )


    assert result["status"] == "processed"



def test_investigation_context():

    manager = InvestigationContextManager()


    result = manager.create_context(
        "INC-001"
    )


    assert result["case_id"] == "INC-001"



def test_intelligence_graph():

    graph = IntelligenceGraph()


    node = graph.add_node(
        "ioc",
        "10.0.0.5"
    )


    assert node["value"] == "10.0.0.5"