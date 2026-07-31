"""
Sentinel DNA
IOC Extraction Engine

Extracts:
- URLs
- Domains
- Email Addresses
- IPv4 Addresses
- SHA256
- SHA1
- MD5
- File Names
"""

import re


# ===============================
# REGEX PATTERNS
# ===============================

URL_PATTERN = re.compile(
    r"https?://[^\s\"'<>]+",
    re.IGNORECASE
)

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

IPV4_PATTERN = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)

DOMAIN_PATTERN = re.compile(
    r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
)

SHA256_PATTERN = re.compile(
    r"\b[a-fA-F0-9]{64}\b"
)

SHA1_PATTERN = re.compile(
    r"\b[a-fA-F0-9]{40}\b"
)

MD5_PATTERN = re.compile(
    r"\b[a-fA-F0-9]{32}\b"
)

FILENAME_PATTERN = re.compile(
    r"\b[\w,\-]+\.(?:exe|dll|zip|rar|pdf|docx|xlsx|js|vbs|ps1|bat)\b",
    re.IGNORECASE
)


# ===============================
# IOC EXTRACTOR
# ===============================

def extract_iocs(text):
    """
    Extract all IOCs from text.
    """

    iocs = []

    for url in set(URL_PATTERN.findall(text)):
        iocs.append({
            "type": "URL",
            "value": url,
            "confidence": "HIGH"
        })

    for email in set(EMAIL_PATTERN.findall(text)):
        iocs.append({
            "type": "EMAIL",
            "value": email,
            "confidence": "HIGH"
        })

    for ip in set(IPV4_PATTERN.findall(text)):
        iocs.append({
            "type": "IP",
            "value": ip,
            "confidence": "HIGH"
        })

    for domain in set(DOMAIN_PATTERN.findall(text)):
        iocs.append({
            "type": "DOMAIN",
            "value": domain,
            "confidence": "MEDIUM"
        })

    for sha256 in set(SHA256_PATTERN.findall(text)):
        iocs.append({
            "type": "SHA256",
            "value": sha256,
            "confidence": "HIGH"
        })

    for sha1 in set(SHA1_PATTERN.findall(text)):
        iocs.append({
            "type": "SHA1",
            "value": sha1,
            "confidence": "HIGH"
        })

    for md5 in set(MD5_PATTERN.findall(text)):
        iocs.append({
            "type": "MD5",
            "value": md5,
            "confidence": "HIGH"
        })

    for filename in set(FILENAME_PATTERN.findall(text)):
        iocs.append({
            "type": "FILE",
            "value": filename,
            "confidence": "MEDIUM"
        })

    return iocs


# ===============================
# TEST
# ===============================

if __name__ == "__main__":

    sample = """
URGENT: Verify your account

Email:
admin@evil.xyz

Website:
https://micr0soft-login.xyz/login

Server:
185.199.108.153

Hash:
9ad8d1251a2bdbf205fc5c73de00a23957ace178b8d4c58ef575db4f59dfc20c

Attachment:
invoice.pdf
"""

    print("🧬 IOC EXTRACTION TEST")
    print("=" * 50)

    for ioc in extract_iocs(sample):
        print(ioc)