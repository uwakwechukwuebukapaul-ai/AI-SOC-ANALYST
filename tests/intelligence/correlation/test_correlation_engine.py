from services.intelligence.correlation.correlation_engine import (
    CorrelationEngine,
)



def test_correlation_engine():

    engine = CorrelationEngine()


    artifacts = [

        {
            "type": "ioc",
            "value": "evil.xyz",
        },

        {
            "type": "ioc",
            "value": "evil.xyz",
        },

        {
            "type": "threat",
            "value": "malware",
        },

    ]


    result = engine.correlate(
        artifacts
    )


    assert result[
        "status"
    ] == "completed"


    assert result[
        "correlated_findings"
    ] == 2