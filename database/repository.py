"""
Sentinel DNA
Database Repository Layer
"""

from datetime import datetime
from database.connection import database



def create_case(case):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO cases
            (
                case_id,
                title,
                severity,
                description,
                status,
                created
            )

            VALUES (?,?,?,?,?,?)
            """,

            (
                case["case_id"],
                case["title"],
                case["severity"],
                case["description"],
                "OPEN",
                datetime.now().isoformat()
            )
        )


def get_cases():

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM cases
            ORDER BY id DESC
            """
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]



def get_case(case_id):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM cases
            WHERE case_id=?
            """,
            (case_id,)
        )

        row = cursor.fetchone()

        return dict(row) if row else None



def update_case_status(case_id, status):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE cases
            SET status=?
            WHERE case_id=?
            """,
            (
                status,
                case_id
            )
        )