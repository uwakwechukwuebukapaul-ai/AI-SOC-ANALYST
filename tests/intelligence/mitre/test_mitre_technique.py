from services.intelligence.mitre.mitre_technique import (
    MitreTechnique,
)


def test_technique():

    technique = MitreTechnique(
        technique_id="T1566",
        name="Phishing",
        tactic="Initial Access",
    )


    result = technique.to_dict()


    assert result["technique_id"] == "T1566"