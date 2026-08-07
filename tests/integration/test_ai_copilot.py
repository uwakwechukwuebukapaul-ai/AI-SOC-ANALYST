from services.ai_copilot import (
    AICopilotEngine,
    ReportGenerator,
    AnalystAssistant
)



def test_copilot_analysis():

    engine = AICopilotEngine()


    result = engine.analyze_case(

        {
            "id": "INC-001"
        },

        {
            "threat_level": "high",
            "confidence": 90,
            "recommendation":
                "Investigate immediately"
        }

    )


    assert result["type"] == (
        "copilot_analysis"
    )



def test_report_generation():

    generator = ReportGenerator()


    report = generator.generate(

        {
            "summary":
                "Threat detected",

            "reasoning":
                [],

            "recommendations":
                []

        }

    )


    assert (
        "Sentinel DNA"
        in report["title"]
    )



def test_analyst_assistant():

    assistant = AnalystAssistant()


    result = assistant.explain(

        {
            "summary":
                "Credential attack detected"
        }

    )


    assert (
        "Credential"
        in result["answer"]
    )