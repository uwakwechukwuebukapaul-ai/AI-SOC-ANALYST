"""
Sentinel DNA
Web Application

Main Flask application
"""


from pathlib import Path
import sys

from flask import Flask



# =====================================
# PROJECT PATH
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))





# =====================================
# FLASK APP
# =====================================

app = Flask(

    __name__,

    template_folder="templates",

    static_folder="static"

)





# =====================================
# ROUTES
# =====================================

from routes.dashboard import dashboard

from routes.cases import case_view

from routes.actions import (

    assign_case,

    update_status,

    add_case_note

)






# =====================================
# DASHBOARD
# =====================================

app.add_url_rule(

    "/",

    "dashboard",

    dashboard

)






# =====================================
# INVESTIGATION WORKSPACE
# =====================================

app.add_url_rule(

    "/case/<case_id>",

    "case_view",

    case_view

)







# =====================================
# SOC ANALYST ACTIONS
# =====================================


app.add_url_rule(

    "/case/<case_id>/assign",

    "assign_case",

    assign_case,

    methods=["POST"]

)





app.add_url_rule(

    "/case/<case_id>/status",

    "update_status",

    update_status,

    methods=["POST"]

)





app.add_url_rule(

    "/case/<case_id>/note",

    "add_case_note",

    add_case_note,

    methods=["POST"]

)








# =====================================
# START SERVER
# =====================================


if __name__ == "__main__":


    print("=" * 60)

    print("🧬 SENTINEL DNA WEB PLATFORM")

    print("=" * 60)



    print("Starting Flask server...")



    print("")

    print("Dashboard:")

    print(
        "http://127.0.0.1:5000"
    )



    print("")

    print("Investigation Example:")

    print(
        "http://127.0.0.1:5000/case/INC-20260731-TEST01"
    )



    print("")

    print("SOC Actions Enabled:")

    print(
        "Assign Analyst"
    )

    print(
        "Update Case Status"
    )

    print(
        "Add Investigation Notes"
    )



    print("=" * 60)



    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )