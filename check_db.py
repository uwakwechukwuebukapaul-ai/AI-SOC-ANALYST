import sqlite3


conn = sqlite3.connect("soc.db")

cursor = conn.cursor()


cursor.execute("PRAGMA table_info(incidents)")


print("\nDATABASE COLUMNS\n")


for column in cursor.fetchall():

    print(column)



print("\nLATEST INCIDENT\n")


cursor.execute(
    "SELECT * FROM incidents ORDER BY id DESC LIMIT 1"
)


print(cursor.fetchone())


conn.close()