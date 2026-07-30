# AI SOC Analyst

A Python-based phishing detection and SOC automation project.

## Features

- Analyze multiple sample emails
- Detect suspicious phishing keywords
- Detect suspicious sender domains
- Extract URLs from email bodies
- Flag suspicious URLs
- Generate structured incident reports
- Save reports as JSON files
- Log incidents to a CSV file
- Print a daily SOC summary dashboard

## Project Structure

```text
AI-SOC-Analyst/
├── main.py
├── gmail_analyzer.py
├── incident_report.py
├── report_writer.py
├── csv_logger.py
├── sample_email.txt
├── sample_emails/
│   ├── email1.txt
│   ├── email2.txt
│   └── email3.txt
├── reports/
├── logs/
└── README.md
```

## How It Works

1. The program reads email samples from the `sample_emails` folder.
2. Each email is analyzed for phishing indicators.
3. The analyzer assigns a risk score and risk level.
4. A structured incident report is created.
5. The report is saved as a JSON file.
6. The incident is logged in a CSV file.
7. A daily SOC summary is printed.

## How to Run

```powershell
python main.py
```

## Sample Output

```text
===== DAILY SOC SUMMARY =====
Total Emails Analyzed : 3
High Risk             : 2
Medium Risk           : 0
Low Risk              : 1
Reports Saved         : 3
```

## Skills Demonstrated

- Python programming
- File handling
- Regex URL extraction
- CSV logging
- JSON report generation
- Basic phishing detection
- SOC-style incident reporting
- Git and GitHub version control

## Future Improvements

- Connect to Gmail
- Add AI-powered analysis
- Send Slack alerts
- Save reports to Notion
- Add VirusTotal URL checks
- Add a simple dashboard interface