from database.connection import database

print("=" * 50)
print("Sentinel DNA Database Test")
print("=" * 50)

with database.session() as conn:

    cursor = conn.cursor()

    cursor.execute("SELECT sqlite_version();")

    version = cursor.fetchone()[0]

    print("SQLite Version :", version)

print("\nDatabase connection successful!")