from services.investigation.autonomous_investigator import AutonomousInvestigator


def test_create_investigation():
    investigator = AutonomousInvestigator()

    investigation = investigator.create_investigation(
        "Investigate phishing email"
    )

    assert investigation["objective"] == "Investigate phishing email"
    assert investigation["status"] == "started"


def test_collect_evidence():
    investigator = AutonomousInvestigator()

    evidence = investigator.collect_evidence(
        {
            "email": "sample@example.com",
            "url": "http://malicious-site.com"
        }
    )

    assert len(evidence) > 0


def test_analyze_indicators():
    investigator = AutonomousInvestigator()

    result = investigator.analyze_indicators(
        [
            "malicious-site.com"
        ]
    )

    assert result["risk"] in [
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    ]


def test_map_attack_techniques():
    investigator = AutonomousInvestigator()

    mapping = investigator.map_attack_techniques(
        "credential phishing"
    )

    assert len(mapping) > 0


def test_generate_investigation_report():
    investigator = AutonomousInvestigator()

    report = investigator.generate_report(
        {
            "risk": "HIGH"
        }
    )

    assert report["generated"] is True


def test_investigation_history():
    investigator = AutonomousInvestigator()

    investigator.create_investigation(
        "Malware investigation"
    )

    history = investigator.get_history()

    assert len(history) == 1