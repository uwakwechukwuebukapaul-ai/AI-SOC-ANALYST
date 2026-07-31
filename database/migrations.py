"""
Sentinel DNA
Database Migration Runner
"""

from database.models import create_tables


if __name__ == "__main__":

    print("🧬 Sentinel DNA Database Migration")

    create_tables()

    print("✅ Database initialized")