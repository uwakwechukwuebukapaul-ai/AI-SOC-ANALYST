import sqlite3
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

        status TEXT

    )
    """)


    conn.commit()

    conn.close()




def save_incident(alert):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO incidents
    (time, threat, severity, score, mitre, status)

    VALUES (?, ?, ?, ?, ?, ?)

    """,

    (

        str(datetime.now()),

        alert.get("type"),

        alert.get("severity"),

        alert.get("score"),

        alert.get("mitre"),

        "OPEN"

    ))


    conn.commit()

    conn.close()




def get_incidents():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM incidents ORDER BY id DESC"
    )


    data = cursor.fetchall()


    conn.close()


    return data



if __name__ == "__main__":

    create_database()

    print("✅ SOC Database Ready")