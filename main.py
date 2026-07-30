import os
import sys

from gmail_analyzer import analyze_email
from incident_report import create_incident_report
from report_writer import save_report_to_json
from csv_logger import log_incident_to_csv
from summary_writer import save_summary_to_json


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


def print_incident_report(file_path, incident_report, saved_file, csv_log):
    print("===== AI SOC ANALYST INCIDENT REPORT =====")
    print(f"Source File       : {file_path}")
    print(f"Incident ID       : {incident_report['incident_id']}")
    print(f"Created At        : {incident_report['created_at']}")
    print(f"Title             : {incident_report['title']}")
    print(f"Sender            : {incident_report['sender']}")
    print(f"Risk Level        : {incident_report['risk_level']}")
    print(f"Risk Score        : {incident_report['risk_score']}")

    print("\nIndicators:")
    if incident_report["indicators"]:
        for indicator in incident_report["indicators"]:
            print("-", indicator)
    else:
        print("No suspicious indicators found.")

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

    print("\nCSV Log Updated:")
    print(csv_log)

    print("\n" + "=" * 60 + "\n")


def analyze_email_file(file_path, risk_filter=None):
    subject, sender, body = read_email_from_file(file_path)

    analysis_result = analyze_email(subject, sender, body)
    incident_report = create_incident_report(subject, sender, analysis_result)
    saved_file = save_report_to_json(incident_report)
    csv_log = log_incident_to_csv(incident_report)

    if risk_filter is None or incident_report["risk_level"] == risk_filter:
        print_incident_report(file_path, incident_report, saved_file, csv_log)

    return incident_report


def print_summary_dashboard(incident_reports):
    total_emails = len(incident_reports)
    high_risk = 0
    medium_risk = 0
    low_risk = 0

    for report in incident_reports:
        if report["risk_level"] == "HIGH":
            high_risk += 1
        elif report["risk_level"] == "MEDIUM":
            medium_risk += 1
        elif report["risk_level"] == "LOW":
            low_risk += 1

    summary = {
        "total_emails": total_emails,
        "high_risk": high_risk,
        "medium_risk": medium_risk,
        "low_risk": low_risk,
        "reports_saved": total_emails,
    }

    summary_file = save_summary_to_json(summary)

    print("===== DAILY SOC SUMMARY =====")
    print(f"Total Emails Analyzed : {summary['total_emails']}")
    print(f"High Risk             : {summary['high_risk']}")
    print(f"Medium Risk           : {summary['medium_risk']}")
    print(f"Low Risk              : {summary['low_risk']}")
    print(f"Reports Saved         : {summary['reports_saved']}")
    print(f"Summary Saved To      : {summary_file}")


def main():
    if len(sys.argv) > 1:
        email_folder = sys.argv[1]
    else:
        email_folder = "sample_emails"

    if len(sys.argv) > 2:
        risk_filter = sys.argv[2].upper()
    else:
        risk_filter = None

    incident_reports = []

    for filename in os.listdir(email_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(email_folder, filename)
            incident_report = analyze_email_file(file_path, risk_filter)
            incident_reports.append(incident_report)

    print_summary_dashboard(incident_reports)


main()