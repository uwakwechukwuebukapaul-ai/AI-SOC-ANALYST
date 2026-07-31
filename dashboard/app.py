from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent.parent / "soc.db"


def query_one(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    value = cursor.fetchone()[0]
    conn.close()
    return value


@app.route("/")
def dashboard():

    stats = {
        "cases": query_one("SELECT COUNT(*) FROM cases"),
        "evidence": query_one("SELECT COUNT(*) FROM evidence"),
        "timeline": query_one("SELECT COUNT(*) FROM timeline"),
        "iocs": query_one("SELECT COUNT(*) FROM iocs"),
    }

    return render_template(
        "dashboard.html",
        stats=stats
    )


if __name__ == "__main__":
    app.run(debug=True)