import sqlite3


DATABASE = "soc.db"


conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()



# Add analyst and notes columns if missing

try:

    cursor.execute(
        """
        ALTER TABLE incidents
        ADD COLUMN analyst TEXT DEFAULT 'None'
        """
    )

except:

    pass



try:

    cursor.execute(
        """
        ALTER TABLE incidents
        ADD COLUMN notes TEXT DEFAULT 'No investigation notes'
        """
    )

except:

    pass



# Fix old records

cursor.execute(
    """
    UPDATE incidents

    SET analyst='None',

    notes='No investigation notes'

    WHERE analyst IS NULL
    """
)



conn.commit()

conn.close()



print("✅ Database migration completed")