from gmail_analyzer import analyze_email
from incident_report import create_incident_report
from report_writer import save_report_to_json


subject = "URGENT: Verify your account"
sender = "security@micr0soft-login.xyz"
body = """
Your account has been suspended.
Click here immediately to verify your password:
http://micr0soft-security-login.xyz
"""

analysis_result = analyze_email(subject, sender, body)
incident_report = create_incident_report(subject, sender, analysis_result)
saved_file = save_report_to_json(incident_report)

print("===== AI SOC ANALYST INCIDENT REPORT =====")
print(f"Incident ID       : {incident_report['incident_id']}")
print(f"Created At        : {incident_report['created_at']}")
print(f"Title             : {incident_report['title']}")
print(f"Sender            : {incident_report['sender']}")
print(f"Risk Level        : {incident_report['risk_level']}")
print(f"Risk Score        : {incident_report['risk_score']}")

print("\nIndicators:")
for indicator in incident_report["indicators"]:
    print("-", indicator)

print("\nURLs Found:")
if incident_report["urls"]:
    for url in incident_report["urls"]:
        print("-", url)
else:
    print("No URLs found.")

print("\nRecommended Action:")
print(incident_report["recommended_action"])

print("\nReport Saved To:")
print(saved_file)