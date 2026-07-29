import sqlite3
import json

from datetime import datetime


DB_NAME = "soc_incidents.db"





def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        time TEXT,

        threat TEXT,

        severity TEXT,

        score INTEGER,

        mitre TEXT,

        status TEXT,

        response_status TEXT,

        response_actions TEXT,

        response_time TEXT,

        assigned_to TEXT,

        investigation_notes TEXT

    )
    """)



    # Upgrade existing database

    cursor.execute(
        "PRAGMA table_info(incidents)"
    )


    columns = [

        column[1]

        for column in cursor.fetchall()

    ]



    upgrades = {

        "assigned_to": "TEXT",

        "investigation_notes": "TEXT"

    }



    for column, datatype in upgrades.items():

        if column not in columns:

            cursor.execute(

                f"ALTER TABLE incidents ADD COLUMN {column} {datatype}"

            )



    conn.commit()

    conn.close()






def incident_exists(alert):


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        """

        SELECT id

        FROM incidents

        WHERE threat = ?

        AND severity = ?

        AND score = ?

        """,

        (

            alert.get("type"),

            alert.get("severity"),

            alert.get("score")

        )

    )



    result = cursor.fetchone()



    conn.close()



    return result is not None







def save_incident(alert):


    if incident_exists(alert):

        return False



    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    response = alert.get(

        "response",

        {}

    )



    cursor.execute("""

    INSERT INTO incidents

    (

        time,

        threat,

        severity,

        score,

        mitre,

        status,

        response_status,

        response_actions,

        response_time,

        assigned_to,

        investigation_notes

    )


    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """,

    (

        str(datetime.now()),

        alert.get("type"),

        alert.get("severity"),

        alert.get("score"),

        alert.get("mitre"),

        "OPEN",

        response.get(

            "status",

            "NOT STARTED"

        ),

        json.dumps(

            response.get(

                "automated_actions",

                []

            )

        ),

        response.get(

            "time",

            str(datetime.now())

        ),

        "Unassigned",

        "No investigation notes yet"

    ))



    conn.commit()

    conn.close()



    return True







def get_incidents():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        "SELECT * FROM incidents ORDER BY id DESC"

    )


    data = cursor.fetchall()


    conn.close()


    return data







def update_incident_status(incident_id, new_status):


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE incidents

        SET status = ?

        WHERE id = ?

        """,

        (

            new_status,

            incident_id

        )

    )



    conn.commit()

    conn.close()








def assign_analyst(incident_id, analyst):


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE incidents

        SET assigned_to = ?

        WHERE id = ?

        """,

        (

            analyst,

            incident_id

        )

    )



    conn.commit()

    conn.close()







def add_investigation_notes(incident_id, notes):


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        """

        UPDATE incidents

        SET investigation_notes = ?

        WHERE id = ?

        """,

        (

            notes,

            incident_id

        )

    )



    conn.commit()

    conn.close()







if __name__ == "__main__":


    create_database()


    print("✅ SOC Database Ready")