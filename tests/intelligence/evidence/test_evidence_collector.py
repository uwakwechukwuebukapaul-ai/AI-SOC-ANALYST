from services.intelligence.evidence.evidence_collector import (
    EvidenceCollector,
)


def test_collect_alert():

    collector = EvidenceCollector()


    artifacts = collector.collect_from_alert(
        {
            "indicator": "evil.xyz"
        }
    )


    assert len(artifacts) == 1

    assert artifacts[0].value == "evil.xyz"