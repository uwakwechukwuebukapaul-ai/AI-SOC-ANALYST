"""
Sentinel DNA
Database Test Module

Tests:
- Database table creation
- Case creation
- Case retrieval
"""

from database.models import create_tables
from database.repository import create_case, get_cases

from datetime import datetime
import uuid



# Initialize database tables

create_tables()



# Generate unique case ID

case_id = (
    "INC-"
    + datetime.now().strftime("%Y%m%d")
    + "-"
    + str(uuid.uuid4())[:6].upper()
)



# Create test case

new_case = {

    "case_id": case_id,

    "title": "Phishing Investigation",

    "severity": "HIGH",

    "description":
        "Suspicious login email detected"

}



create_case(new_case)



# Retrieve cases

cases = get_cases()



print("🧬 SENTINEL DNA DATABASE TEST")

print("=" * 40)



for case in cases:

    print(dict(case))