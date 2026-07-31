"""
Sentinel DNA
SOC Analyst Actions Route
"""

from flask import request, redirect, url_for

from database.repository import (
    assign_analyst,
    update_case_status,
    add_note
)

from analyst_workspace.analyst_actions import record_action



def assign_case(case_id):

    analyst = request.form.get("analyst")


    if analyst:

        assign_analyst(
            case_id,
            analyst
        )


        record_action(
            {
                "case_id": case_id
            },
            "Assigned case to analyst",
            analyst
        )


    return redirect(
        url_for(
            "case_view",
            case_id=case_id
        )
    )




def update_status(case_id):

    status = request.form.get("status")


    if status:

        update_case_status(
            case_id,
            status
        )


        record_action(
            {
                "case_id": case_id
            },
            f"Status changed to {status}",
            "SOC ANALYST"
        )


    return redirect(
        url_for(
            "case_view",
            case_id=case_id
        )
    )





def add_case_note(case_id):

    note = request.form.get("note")


    if note:

        add_note(
            case_id,
            note
        )


        record_action(
            {
                "case_id": case_id
            },
            "Added investigation note",
            "SOC ANALYST"
        )


    return redirect(
        url_for(
            "case_view",
            case_id=case_id
        )
    )