from database.models import Incident

incident = Incident(

    threat="Phishing Email",

    severity="HIGH",

    risk_score=92,

    mitre="T1566.001"

)

incident.validate()

print("=" * 50)

print("Sentinel DNA Incident Model Test")

print("=" * 50)

print(incident)

print()

print(incident.to_dict())