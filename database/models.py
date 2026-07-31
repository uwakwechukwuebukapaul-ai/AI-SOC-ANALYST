"""
Sentinel DNA
Database Models
"""

from database.connection import database



def create_tables():

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT UNIQUE,

            title TEXT NOT NULL,

            severity TEXT,

            description TEXT,

            status TEXT DEFAULT 'OPEN',

            created TEXT

        )
        """)



        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evidence (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT,

            evidence_type TEXT,

            data TEXT,

            created TEXT,

            FOREIGN KEY(case_id)
            REFERENCES cases(case_id)

        )
        """)



        cursor.execute("""
        CREATE TABLE IF NOT EXISTS timeline (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT,

            event TEXT,

            created TEXT,

            FOREIGN KEY(case_id)
            REFERENCES cases(case_id)

        )
        """)



    return True