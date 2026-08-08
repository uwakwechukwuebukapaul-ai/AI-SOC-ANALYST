from services.intelligence.reporting.artifact_normalizer import (
    ArtifactNormalizer,
)



def test_artifact_normalizer():

    normalizer = ArtifactNormalizer()


    artifacts = normalizer.normalize(
        {
            "source": "email",
            "indicator": "evil-domain.xyz",
            "severity": "high",
            "metadata": {
                "nested": "data"
            }
        }
    )


    assert len(
        artifacts
    ) == 3


    assert {
        "type": "ioc",
        "value": "evil-domain.xyz",
    } in artifacts


    assert {
        "type": "severity",
        "value": "high",
    } in artifacts