# 🧬 Sentinel DNA

AI-Powered Security Operations Center (SOC) Investigation Platform

Sentinel DNA is a Python-based SOC platform designed to automate phishing investigations, manage security cases, collect digital evidence, extract Indicators of Compromise (IOCs), and assist analysts through an integrated investigation workflow.

It combines email analysis, evidence management, IOC intelligence, timeline tracking, and a web dashboard into a single investigation platform.

---

## Features

✅ Email Analysis Engine

• Phishing keyword detection
• Suspicious sender analysis
• URL extraction
• Risk scoring

✅ Case Management

• Automatic case creation
• Analyst assignment
• Status tracking

✅ Evidence Engine

• SHA-256 hashing
• Evidence repository
• Chain-of-custody support

✅ IOC Intelligence

• Domain extraction
• URL extraction
• Email extraction
• IOC repository
• IOC statistics

✅ Investigation Timeline

• Alert events
• Evidence collection
• Analyst actions
• Investigation history

✅ Dashboard

• Live Flask dashboard
• Case statistics
• IOC statistics
• Evidence statistics

---

## Architecture

Email

↓

Evidence Engine

↓

Investigation Pipeline

↓

Case Management

↓

Evidence Repository

↓

IOC Intelligence

↓

Timeline

↓

Dashboard

---

## Technologies

Python

Flask

SQLite

HTML/CSS

Git

GitHub

ReportLab (planned)

---

## Project Structure

Sentinel-DNA/
├── cases/
├── dashboard/
├── database/
├── evidence_engine/
├── ioc_engine/
├── services/
├── reports/
├── tests/
└── README.md

---

## Roadmap

Sprint 1
Core Email Analyzer

Sprint 2
Evidence Repository

Sprint 3
Investigation Pipeline

Sprint 4
IOC Intelligence

Sprint 5
SOC Dashboard

Sprint 6
PDF Reports

Sprint 7
AI SOC Analyst

---

## Upcoming Features

• PDF Investigation Reports
• MITRE ATT&CK Mapping
• VirusTotal Integration
• AI Investigation Assistant
• Threat Intelligence Feeds
• REST API
• Authentication
• Multi-user SOC Console

---

## License

MIT License
