from services.intelligence.reporting.intelligence.report_enrichment import (
    ReportEnrichment,
)



def test_report_enrichment():


    engine = ReportEnrichment()


    report = {
        "case_id": "CASE-001",
    }


    intelligence = {

        "correlation": {
            "correlated_findings": 2,
        },

        "reasoning": {

            "confidence": 80,

            "hypotheses": [

                {
                    "hypothesis":
                    "Possible phishing activity"
                }

            ],
        },
    }



    result = engine.enrich(
        report,
        intelligence,
    )


    assert (
        result["intelligence_status"]
        ==
        "completed"
    )


    assert (
        "attack_story"
        in result
    )


    assert (
        "analyst_summary"
        in result
    )