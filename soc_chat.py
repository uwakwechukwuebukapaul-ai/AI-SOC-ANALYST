def soc_response(question):

    question = question.lower()


    if "phishing" in question:

        return """
🛡️ PHISHING INVESTIGATION STEPS:

1. Check sender email reputation
2. Analyze suspicious links
3. Verify domain age and ownership
4. Check email headers
5. Block malicious sender
6. Search for similar emails
7. Reset credentials if compromise is suspected
"""


    elif "malware" in question:

        return """
🦠 MALWARE RESPONSE:

1. Isolate affected endpoint
2. Collect malware sample
3. Run antivirus/EDR scan
4. Check persistence mechanisms
5. Remove malicious files
6. Monitor network activity
"""


    elif "incident" in question:

        return """
🚨 INCIDENT RESPONSE PROCESS:

1. Identification
2. Containment
3. Eradication
4. Recovery
5. Lessons learned
6. Update security controls
"""


    elif "mitre" in question:

        return """
🎯 MITRE ATT&CK ANALYSIS:

Common techniques:

T1566 - Phishing
T1059 - Command and Scripting Interpreter
T1204 - User Execution
T1071 - Application Layer Protocol
"""


    elif "ioc" in question or "indicator" in question:

        return """
🔎 IOC INVESTIGATION:

Check:

- IP addresses
- Domains
- File hashes
- URLs
- Email addresses

Validate indicators using threat intelligence platforms.
"""


    else:

        return """
🤖 AI SOC Assistant:

I recommend:

1. Review security logs
2. Investigate indicators of compromise
3. Check threat intelligence
4. Document findings
5. Follow incident response procedures
"""