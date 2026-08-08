from services.intelligence.risk.risk_factors import (
    RiskFactor,
)


def test_risk_factor():

    factor = RiskFactor(
        name="malicious_indicator",
        weight=40,
        description="Malicious IOC",
    )


    result = factor.to_dict()


    assert result["name"] == (
        "malicious_indicator"
    )

    assert result["weight"] == 40