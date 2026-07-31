from database.repository import (
    assign_analyst,
    update_case_status,
    get_case
)


case_id = "INC-20260731-FE4AD8"


assign_analyst(
    case_id,
    "Paul SOC Analyst"
)


update_case_status(
    case_id,
    "INVESTIGATING"
)


case = get_case(case_id)


print("🧬 ANALYST ACTION TEST")
print("="*40)

print(case)