"""
Sentinel DNA
IOC Repository

Handles:
- Save IOC
- Get IOC
- Search IOC
- Statistics
"""

import sys
from pathlib import Path
from datetime import datetime
import uuid

# =====================================
# PROJECT PATH FIX
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from database.connection import database
from database.repository import create_case


# =====================================
# IOC ID
# =====================================

def generate_ioc_id():

    return "IOC-" + uuid.uuid4().hex[:8].upper()


# =====================================
# SAVE IOC
# =====================================

def save_ioc(
    case_id,
    ioc_type,
    value,
    confidence="MEDIUM",
    reputation="UNKNOWN",
    source="LOCAL"
):

    ioc_id = generate_ioc_id()

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO iocs
            (
                ioc_id,
                case_id,
                ioc_type,
                value,
                confidence,
                reputation,
                source,
                created
            )

            VALUES (?,?,?,?,?,?,?,?)
            """,
            (
                ioc_id,
                case_id,
                ioc_type,
                value,
                confidence,
                reputation,
                source,
                datetime.now().isoformat()
            )
        )

    return ioc_id


# =====================================
# GET IOCS BY CASE
# =====================================

def get_iocs(case_id):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM iocs
            WHERE case_id=?
            ORDER BY id DESC
            """,
            (case_id,)
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]


# =====================================
# GET ALL IOCS
# =====================================

def get_all_iocs():

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM iocs
            ORDER BY id DESC
            """
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]


# =====================================
# SEARCH IOC
# =====================================

def search_ioc(value):

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM iocs
            WHERE value LIKE ?
            ORDER BY id DESC
            """,
            (f"%{value}%",)
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]


# =====================================
# IOC COUNT
# =====================================

def count_iocs():

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM iocs
            """
        )

        return cursor.fetchone()[0]


# =====================================
# IOC COUNT BY TYPE
# =====================================

def count_by_type():

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                ioc_type,
                COUNT(*) AS total
            FROM iocs
            GROUP BY ioc_type
            ORDER BY total DESC
            """
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]


# =====================================
# IOC COUNT BY REPUTATION
# =====================================

def count_by_reputation():

    with database.session() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                reputation,
                COUNT(*) AS total
            FROM iocs
            GROUP BY reputation
            ORDER BY total DESC
            """
        )

        return [
            dict(row)
            for row in cursor.fetchall()
        ]


# =====================================
# TEST
# =====================================

if __name__ == "__main__":

    print("🧬 IOC REPOSITORY TEST")
    print("=" * 50)

    case_id = "INC-TEST-IOC"

    # Create test case if it doesn't exist
    try:

        create_case({

            "case_id": case_id,

            "title": "IOC Repository Test",

            "severity": "HIGH",

            "description": "Testing IOC Repository"

        })

    except Exception:
        # Ignore duplicate case_id
        pass

    save_ioc(
        case_id,
        "DOMAIN",
        "micr0soft-login.xyz",
        "HIGH",
        "SUSPICIOUS"
    )

    save_ioc(
        case_id,
        "URL",
        "https://micr0soft-login.xyz/login",
        "HIGH",
        "SUSPICIOUS"
    )

    save_ioc(
        case_id,
        "EMAIL",
        "admin@evil.xyz",
        "HIGH",
        "SUSPICIOUS"
    )

    print("\nIOC COUNT")
    print("-" * 40)
    print(count_iocs())

    print("\nCASE IOCS")
    print("-" * 40)

    for item in get_iocs(case_id):
        print(item)

    print("\nTYPE STATISTICS")
    print("-" * 40)

    for item in count_by_type():
        print(item)

    print("\nREPUTATION STATISTICS")
    print("-" * 40)

    for item in count_by_reputation():
        print(item)

    print("\n✅ IOC Repository test completed successfully.")