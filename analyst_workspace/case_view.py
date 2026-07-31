"""
Sentinel DNA

SOC Analyst Case Viewer

Responsible for:
- Viewing investigation cases
- Displaying evidence
- Displaying timeline activity
- Displaying analyst actions
"""


import sys
from pathlib import Path


# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


from database.repository import get_cases
from cases.timeline import get_timeline
from database.connection import database



# =====================================
# GET CASE ACTIONS
# =====================================

def get_case_actions(case_id):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM analyst_actions
            WHERE case_id=?

            ORDER BY id ASC

            """,
            (case_id,)
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]



# =====================================
# GET CASE EVIDENCE
# =====================================

def get_case_evidence(case_id):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM evidence
            WHERE case_id=?

            ORDER BY id ASC

            """,
            (case_id,)
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]



# =====================================
# DISPLAY CASE
# =====================================

def view_case(case):

    case_id = case["case_id"]


    print("\n🧬 SENTINEL DNA CASE REPORT")

    print("=" * 50)


    print("CASE INFORMATION")

    print("-" * 50)


    for key,value in case.items():

        print(
            f"{key}: {value}"
        )



    print("\nEVIDENCE")

    print("-" * 50)


    evidence = get_case_evidence(case_id)


    if evidence:

        for item in evidence:

            print(item)

    else:

        print("No evidence found")



    print("\nTIMELINE")

    print("-" * 50)


    timeline = get_timeline(case_id)


    if timeline:

        for event in timeline:

            print(event)

    else:

        print("No timeline events")



    print("\nANALYST ACTIONS")

    print("-" * 50)


    actions = get_case_actions(case_id)


    if actions:

        for action in actions:

            print(action)

    else:

        print("No analyst actions")



# =====================================
# VIEW ALL CASES
# =====================================

def view_cases():

    cases = get_cases()


    if not cases:

        print("No cases available")

        return


    for case in cases:

        view_case(case)



# =====================================
# TEST
# =====================================

if __name__ == "__main__":


    print(
        "🧬 SENTINEL DNA SOC CASE VIEWER"
    )

    print("=" * 50)


    view_cases()