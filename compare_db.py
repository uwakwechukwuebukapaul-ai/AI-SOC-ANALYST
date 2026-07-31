import sqlite3


databases = [
    "soc.db",
    "soc_incidents.db"
]


for db in databases:

    print("\n==============================")
    print("DATABASE:", db)
    print("==============================")


    try:

        conn = sqlite3.connect(db)

        cursor = conn.cursor()


        cursor.execute(
            "SELECT COUNT(*) FROM cases"
        )


        count = cursor.fetchone()[0]


        print(
            "Cases:",
            count
        )


        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )


        tables = cursor.fetchall()


        print(
            "Tables:",
            tables
        )


        conn.close()


    except Exception as e:

        print(
            "ERROR:",
            e
        )