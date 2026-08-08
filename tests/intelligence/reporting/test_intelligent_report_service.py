from services.intelligence.reporting.intelligent_report_service import (
    IntelligentReportService,
)



class FakeReportService:

    def build_response(
        self,
        case_id,
        orchestration_result,
    ):

        return {
            "case_id": case_id,
            "findings": [],
        }



def test_intelligent_report_generation():


    service = IntelligentReportService(
        report_service=FakeReportService()
    )


    result = service.generate(

        case_id="CASE-001",

        orchestration_result={
            "status": "completed"
        },

        artifacts=[

            {
                "type": "ioc",
                "value": "evil-domain.xyz",
            }

        ],
    )



    assert (
        result["case_id"]
        ==
        "CASE-001"
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