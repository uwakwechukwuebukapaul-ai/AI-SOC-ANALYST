"""
Sentinel DNA Investigation API Routes

Enterprise investigation API boundary.

Flow:

API Request
|
v
Investigation Coordinator
|
v
Agent Pipeline
|
v
Runtime Task Executor
|
v
AI Agents
|
v
Report Service
"""

from __future__ import annotations

from typing import Any

from flask import Blueprint
from flask import jsonify
from flask import request


from services.intelligence.orchestration.investigation_coordinator import (
    InvestigationCoordinator,
)

from services.intelligence.agents.agent_registry import (
    AgentRegistry,
)

from services.intelligence.runtime.runtime_task_executor import (
    RuntimeTaskExecutor,
)

from services.intelligence.agents.bootstrap import (
    bootstrap_agents,
)

from services.intelligence.agents.runtime_adapter import (
    AgentRuntimeAdapter,
)

from services.intelligence.reporting.report_service import (
    ReportService,
)


# ============================================================
# Blueprint
# ============================================================

investigation_bp = Blueprint(
    "investigation",
    __name__,
    url_prefix="/api/investigations",
)


# ============================================================
# Sentinel DNA Intelligence Runtime
# ============================================================

agent_registry = AgentRegistry()

runtime_executor = RuntimeTaskExecutor()

runtime_adapter = AgentRuntimeAdapter(
    runtime_executor,
)


bootstrap_agents(
    agent_registry,
    runtime_adapter=runtime_adapter,
)


investigation_coordinator = InvestigationCoordinator(
    registry=agent_registry,
    runtime=runtime_executor,
)


report_service = ReportService()


# ============================================================
# Generate Investigation Report
# ============================================================

@investigation_bp.route(
    "/report",
    methods=["POST"],
)
def generate_investigation_report():

    payload: dict[str, Any] = (
        request.get_json(
            silent=True
        )
        or {}
    )


    case_id = payload.get(
        "case_id"
    )

    alert = payload.get(
        "alert"
    )


    if not case_id:

        return jsonify(
            {
                "success": False,
                "error": "case_id is required",
            }
        ), 400



    if not isinstance(
        alert,
        dict,
    ):

        return jsonify(
            {
                "success": False,
                "error": "alert must be an object",
            }
        ), 400



    try:

        orchestration_result = (
            investigation_coordinator.investigate(
                case_id=case_id,
                alert=alert,
            )
        )


        report = (
            report_service.build_response(
                case_id=case_id,
                orchestration_result=(
                    orchestration_result
                ),
            )
        )


        return jsonify(
            {
                "success": True,
                "report": report,
            }
        ), 200



    except Exception as error:

        return jsonify(
            {
                "success": False,
                "error": str(error),
            }
        ), 500



# ============================================================
# Retrieve Investigation Report
# ============================================================

@investigation_bp.route(
    "/report/<case_id>",
    methods=["GET"],
)
def get_investigation_report(
    case_id: str,
):

    try:

        report = (
            report_service.get_report(
                case_id
            )
        )


        if report is None:

            return jsonify(
                {
                    "success": False,
                    "error": "Report not found",
                    "case_id": case_id,
                }
            ), 404



        serialized_report = (
            report_service.serialize_report(
                report
            )
        )


        return jsonify(
            {
                "success": True,
                "report": serialized_report,
            }
        ), 200



    except Exception as error:

        return jsonify(
            {
                "success": False,
                "error": str(error),
            }
        ), 500