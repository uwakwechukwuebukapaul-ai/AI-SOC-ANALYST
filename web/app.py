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



# Dashboard

app.add_url_rule(
    "/",
    "dashboard",
    dashboard
)



# Investigation Workspace

app.add_url_rule(
    "/case/<case_id>",
    "case_view",
    case_view
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
    print("http://127.0.0.1:5000")

    print("")
    print("Investigation Example:")
    print("http://127.0.0.1:5000/case/INC-20260731-TEST01")

    print("=" * 60)


    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )