"""
Sentinel DNA
Database Models
"""

from database.connection import database


def create_tables():
    """
    Create all Sentinel DNA database tables.
    """

    with database.session() as conn:

        cursor = conn.cursor()

        # =====================================
        # CASES
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT UNIQUE NOT NULL,

            title TEXT NOT NULL,

            severity TEXT NOT NULL,

            description TEXT DEFAULT '',

            status TEXT DEFAULT 'OPEN',

            analyst TEXT DEFAULT '',

            created TEXT NOT NULL

        )
        """)

        # =====================================
        # CASE NOTES
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS case_notes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT NOT NULL,

            note TEXT NOT NULL,

            analyst TEXT DEFAULT '',

            created TEXT NOT NULL,

            FOREIGN KEY(case_id)
                REFERENCES cases(case_id)

        )
        """)

        # =====================================
        # EVIDENCE
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS evidence (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT NOT NULL,

            type TEXT NOT NULL,

            data TEXT NOT NULL,

            sha256 TEXT NOT NULL,

            created TEXT NOT NULL,

            FOREIGN KEY(case_id)
                REFERENCES cases(case_id)

        )
        """)

        # =====================================
        # TIMELINE
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS timeline (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            case_id TEXT NOT NULL,

            event_type TEXT NOT NULL,

            description TEXT NOT NULL,

            actor TEXT DEFAULT 'SYSTEM',

            created TEXT NOT NULL,

            FOREIGN KEY(case_id)
                REFERENCES cases(case_id)

        )
        """)

    return True


if __name__ == "__main__":

    create_tables()

    print("✅ Sentinel DNA database tables created successfully.")