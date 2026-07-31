from database.repository import incident_repository
from database.models import Incident


incident = Incident(

    threat="Phishing Attack",

    severity="HIGH",

    risk_score=90,

    mitre="T1566"

)


incident_id = incident_repository.create(
    incident
)


print(
    "Created Incident ID:",
    incident_id
)


incidents = incident_repository.get_all()


print("\nAll Incidents:")

for item in incidents:

    print(
        item.to_dict()
    )