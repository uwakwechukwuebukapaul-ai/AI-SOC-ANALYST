import sqlite3
import json

from datetime import datetime


DB_NAME = "soc_incidents.db"



def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    # Create table if it does not exist

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

        response_time TEXT

    )
    """)



    # Upgrade old databases automatically

    cursor.execute(
        "PRAGMA table_info(incidents)"
    )

    columns = [

        column[1]

        for column in cursor.fetchall()

    ]



    new_columns = {

        "response_status": "TEXT",

        "response_actions": "TEXT",

        "response_time": "TEXT"

    }



    for column, datatype in new_columns.items():

        if column not in columns:

            cursor.execute(

                f"ALTER TABLE incidents ADD COLUMN {column} {datatype}"

            )



    conn.commit()

    conn.close()





def save_incident(alert):


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    response = alert.get(

        "response",

        {}

    )



    actions = response.get(

        "automated_actions",

        []

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

        response_time

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

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


        json.dumps(actions),


        response.get(

            "time",

            str(datetime.now())

        )

    ))



    conn.commit()

    conn.close()





def get_incidents():


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()



    cursor.execute(

        "SELECT * FROM incidents ORDER BY id DESC"

    )



    incidents = cursor.fetchall()



    conn.close()



    return incidents





if __name__ == "__main__":


    create_database()


    print("✅ SOC Database Ready")