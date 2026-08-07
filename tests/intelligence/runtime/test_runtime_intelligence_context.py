"""
Runtime Intelligence Context Tests
"""

from services.intelligence.runtime.runtime_intelligence_context import (
    RuntimeIntelligenceContext,
)



def test_init():

    context = RuntimeIntelligenceContext(
        investigation_id="INC-001"
    )

    assert (
        context.investigation_id
        ==
        "INC-001"
    )



def test_add_evidence():

    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    context.add_evidence(
        {
            "type":
                "email"
        }
    )


    assert (
        len(context.evidence)
        ==
        1
    )



def test_add_ioc():

    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    context.add_ioc(
        {
            "value":
                "example.com"
        }
    )


    assert (
        len(context.iocs)
        ==
        1
    )



def test_add_mitre():

    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    context.add_mitre(
        {
            "technique":
                "T1566"
        }
    )


    assert (
        len(context.mitre)
        ==
        1
    )



def test_metadata():

    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    context.update_metadata(
        "priority",
        "critical",
    )


    assert (
        context.metadata["priority"]
        ==
        "critical"
    )



def test_status():

    context = RuntimeIntelligenceContext(
        "INC-001"
    )


    result = context.status()


    assert "investigation_id" in result

    assert "evidence_count" in result