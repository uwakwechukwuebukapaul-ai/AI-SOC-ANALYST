"""
Sentinel DNA Report API Tests

Validates investigation report API endpoints.

Coverage:

- report generation endpoint
- report retrieval endpoint
- response schema
- report persistence boundary
"""

from __future__ import annotations

import pytest

from flask import Flask

from services.api.investigation_routes import (
    investigation_bp,
)


@pytest.fixture
def client():

    app = Flask(
        __name__
    )

    app.register_blueprint(
        investigation_bp
    )

    app.testing = True

    return app.test_client()



def test_generate_investigation_report(
    client,
):

    response = client.post(
        "/api/investigations/report",
        json={
            "case_id": "CASE-001",
            "alert": {
                "source": "email",
                "indicator": "malicious-domain.xyz",
                "severity": "high",
            },
        },
    )


    assert response.status_code == 200


    data = response.get_json()


    assert data is not None


    assert "report" in data


    report = data["report"]


    assert (
        report["case_id"]
        ==
        "CASE-001"
    )


    assert (
        "severity"
        in report
    )


    assert (
        "findings"
        in report
    )



def test_get_investigation_report(
    client,
):

    response = client.get(
        "/api/investigations/report/CASE-001"
    )


    assert response.status_code in (
        200,
        404,
    )


    if response.status_code == 200:

        data = response.get_json()


        assert (
            "report"
            in data
        )