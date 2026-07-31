"""
Sentinel DNA

Case Management Test

Tests:
- Case creation
- Evidence attachment
- Timeline events
"""


from cases.case_manager import create_investigation

from cases.evidence import add_evidence

from cases.timeline import add_timeline_event




# =====================================
# CREATE INVESTIGATION
# =====================================

case = create_investigation(

    title="Phishing Attack Investigation",

    severity="HIGH",

    description="Suspicious email campaign detected"

)




# =====================================
# ADD EVIDENCE
# =====================================

add_evidence(

    case,

    "URL",

    "https://fake-login.xyz"

)




# =====================================
# ADD TIMELINE EVENT
# =====================================

add_timeline_event(

    case["case_id"],

    "ANALYSIS",

    "Email analyzed by evidence engine",

    "AI ENGINE"

)




# =====================================
# OUTPUT RESULT
# =====================================

print("=" * 50)

print("🧬 SENTINEL DNA CASE")

print("=" * 50)


print(case)