from services.intelligence.storage.artifact_repository import (
    ArtifactRepository,
)


def test_create_artifact():

    repository = ArtifactRepository()

    artifact = {
        "type": "ioc",
        "value": "malicious-domain.xyz",
    }


    result = repository.create(
        "CASE-001",
        artifact,
    )


    assert result == artifact



def test_get_artifacts():

    repository = ArtifactRepository()


    repository.create(
        "CASE-001",
        {
            "type": "threat_intel",
            "score": 90,
        },
    )


    artifacts = repository.get(
        "CASE-001"
    )


    assert len(artifacts) == 1



def test_count_artifacts():

    repository = ArtifactRepository()


    repository.create(
        "CASE-001",
        {
            "type": "finding",
        },
    )


    assert repository.count(
        "CASE-001"
    ) == 1