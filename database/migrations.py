"""
Sentinel DNA
Database Migration Manager
"""

from pathlib import Path

from database.connection import database


SCHEMA_FILE = Path(
    "database/schema.sql"
)


def run_migrations():

    """
    Apply database schema.
    """

    if not SCHEMA_FILE.exists():

        raise FileNotFoundError(
            "schema.sql not found"
        )


    with open(
        SCHEMA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        schema = file.read()


    with database.session() as conn:

        cursor = conn.cursor()

        cursor.executescript(
            schema
        )


    print(
        "✅ Database migration completed"
    )



if __name__ == "__main__":

    run_migrations()