import os

from gmail_analyzer import analyze_email
from incident_report import create_incident_report
from report_writer import save_report_to_json


def read_email_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    lines = content.splitlines()

    subject = ""
    sender = ""
    body_lines = []

    for line in lines:
        if line.startswith("Subject:"):
            subject = line.replace("Subject:", "").strip()
        elif line.startswith("Sender:"):
            sender = line.replace("Sender:", "").strip()
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()

    return subject, sender, body


def analyze_email_file(file_path):
    subject, sender, body = read_email_from_file(file_path)

    analysis_result = analyze_email(subject, sender, body)
    incident_report = create_incident_report(subject, sender, analysis_result)
    saved_file = save_report_to_json(incident_report)

    print("===== AI SOC ANALYST INCIDENT REPORT =====")
    print(f"Source File       : {file_path}")
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
    print("\n" + "=" * 60 + "\n")


def main():
    email_folder = "sample_emails"

    for filename in os.listdir(email_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(email_folder, filename)
            analyze_email_file(file_path)


main()