from services.intelligence.mitre.mitre_mapper import (
    MitreMapper,
)


def test_email_mapping():

    mapper = MitreMapper()


    result = mapper.map_artifact(
        {
            "type": "email"
        }
    )


    assert result[0]["technique_id"] == "T1566"