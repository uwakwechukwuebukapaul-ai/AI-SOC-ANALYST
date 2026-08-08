from services.intelligence.evidence.artifact import (
    Artifact,
)

from services.intelligence.evidence.evidence_classifier import (
    EvidenceClassifier,
)


def test_classifier():

    artifact = Artifact(
        artifact_id="1",
        artifact_type="ioc",
        value="malicious.xyz",
        source="test",
    )


    classifier = EvidenceClassifier()


    result = classifier.classify(
        artifact
    )


    assert result == "domain"