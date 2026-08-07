from services.detection_engineering import (
    DetectionEngine,
    SigmaMapper,
    RuleValidator,
    CoverageAnalyzer
)



def test_detection_analysis():

    engine = DetectionEngine()


    result = engine.analyze_event(

        {
            "event":
                "failed_login",

            "indicator":
                "192.168.1.10",

            "severity":
                "high"

        }

    )


    assert (
        "IOC indicator detected"
        in result["matches"]
    )



def test_sigma_mapping():

    mapper = SigmaMapper()


    result = mapper.map_detection(

        {
            "severity":
                "high"
        }

    )


    assert (
        result["format"]
        ==
        "sigma"
    )



def test_rule_validation():

    validator = RuleValidator()


    result = validator.validate(

        {
            "title":
                "test",

            "description":
                "rule",

            "level":
                "high"

        }

    )


    assert result["valid"]



def test_detection_coverage():

    analyzer = CoverageAnalyzer()


    result = analyzer.analyze(

        [
            "rule1",
            "rule2"
        ]

    )


    assert (
        result["total_rules"]
        ==
        2
    )