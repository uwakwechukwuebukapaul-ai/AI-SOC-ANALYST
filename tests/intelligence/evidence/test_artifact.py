from services.intelligence.evidence.artifact import (
    Artifact,
)


def test_artifact_creation():

    artifact = Artifact(
        artifact_id="ioc-1",
        artifact_type="domain",
        value="evil.xyz",
        source="email",
    )


    result = artifact.to_dict()


    assert result["value"] == "evil.xyz"