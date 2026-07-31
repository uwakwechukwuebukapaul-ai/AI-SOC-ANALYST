from database.models import create_tables
from database.repository import create_case, get_cases


create_tables()


create_case({

    "case_id":"INC-001",

    "title":"Phishing Investigation",

    "severity":"HIGH",

    "description":"Suspicious login email detected"

})


cases = get_cases()


for case in cases:

    print(case)