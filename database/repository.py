"""
Sentinel DNA
Database Repository Layer

Handles:
- Case creation
- Case retrieval
- Case updates
- Analyst assignment
- Notes
- Evidence tracking
- Timeline support
"""


from datetime import datetime
import hashlib


from database.connection import database




# =====================================
# HASH GENERATOR
# =====================================

def generate_sha256(data):

    return hashlib.sha256(

        str(data).encode()

    ).hexdigest()





# =====================================
# CREATE CASE
# =====================================

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


    return case["case_id"]






# =====================================
# GET ALL CASES
# =====================================

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






# =====================================
# GET SINGLE CASE
# =====================================

def get_case(case_id):

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *

            FROM cases

            WHERE case_id=?

            """,

            (

                case_id,

            )

        )


        row = cursor.fetchone()


        return dict(row) if row else None





# =====================================
# UPDATE STATUS
# =====================================

def update_case_status(
        case_id,
        status
):

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






# =====================================
# ASSIGN ANALYST
# =====================================

def assign_analyst(
        case_id,
        analyst
):

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            UPDATE cases

            SET analyst=?

            WHERE case_id=?

            """,

            (

                analyst,

                case_id

            )

        )






# =====================================
# ADD NOTE
# =====================================

def add_note(
        case_id,
        note
):

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO case_notes
            (
                case_id,
                note,
                created
            )

            VALUES (?,?,?)

            """,

            (

                case_id,

                note,

                datetime.now().isoformat()

            )

        )






# =====================================
# GET NOTES
# =====================================

def get_notes(case_id):

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *

            FROM case_notes

            WHERE case_id=?

            ORDER BY id DESC

            """,

            (

                case_id,

            )

        )


        return [

            dict(row)

            for row in cursor.fetchall()

        ]






# =====================================
# ADD EVIDENCE
# =====================================

def add_evidence_record(
        case_id,
        evidence_type,
        evidence_data
):


    evidence_hash = generate_sha256(

        evidence_data

    )


    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO evidence
            (
                case_id,
                type,
                data,
                sha256,
                created
            )

            VALUES (?,?,?,?,?)

            """,

            (

                case_id,

                evidence_type,

                evidence_data,

                evidence_hash,

                datetime.now().isoformat()

            )

        )


    return evidence_hash






# =====================================
# GET EVIDENCE
# =====================================

def get_evidence(case_id):

    with database.session() as conn:

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *

            FROM evidence

            WHERE case_id=?

            ORDER BY id DESC

            """,

            (

                case_id,

            )

        )


        return [

            dict(row)

            for row in cursor.fetchall()

        ]