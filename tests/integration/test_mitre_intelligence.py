from services.mitre_intelligence import (
    MitreIntelligenceEngine
)



def test_mitre_mapping():

    engine = MitreIntelligenceEngine()


    result = engine.analyze(
        {
            "event": "authentication_attack",
            "technique_signal":
                "password_spray"
        }
    )


    assert (
        result["techniques"][0]["id"]
        ==
        "T1110.003"
    )


    assert (
        "Credential Access"
        in result["tactics"]
    )



def test_attack_path():

    engine = MitreIntelligenceEngine()


    result = engine.analyze(
        {
            "technique_signal":
                "phishing"
        }
    )


    assert (
        len(result["attack_path"])
        ==
        1
    )



def test_detection_coverage():

    engine = MitreIntelligenceEngine()


    result = engine.analyze(
        {
            "technique_signal":
                "malware_execution"
        }
    )


    assert (
        result["coverage"]["covered"]
        is True
    )