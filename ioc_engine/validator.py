"""
Sentinel DNA
IOC Validator

Validates:
- IPv4
- Email
- Domain
- URL
- MD5
- SHA1
- SHA256
"""

import ipaddress
import re


EMAIL_REGEX = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

DOMAIN_REGEX = re.compile(
    r"^(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$"
)

URL_REGEX = re.compile(
    r"^https?://[^\s]+$",
    re.IGNORECASE
)


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_valid_email(email):
    return bool(EMAIL_REGEX.match(email))


def is_valid_domain(domain):
    return bool(DOMAIN_REGEX.match(domain))


def is_valid_url(url):
    return bool(URL_REGEX.match(url))


def is_valid_md5(value):
    return len(value) == 32 and all(
        c in "0123456789abcdefABCDEF"
        for c in value
    )


def is_valid_sha1(value):
    return len(value) == 40 and all(
        c in "0123456789abcdefABCDEF"
        for c in value
    )


def is_valid_sha256(value):
    return len(value) == 64 and all(
        c in "0123456789abcdefABCDEF"
        for c in value
    )


if __name__ == "__main__":

    print("🧬 IOC VALIDATOR TEST")
    print("=" * 40)

    print("IP:", is_valid_ip("185.199.108.153"))
    print("Email:", is_valid_email("admin@evil.xyz"))
    print("Domain:", is_valid_domain("micr0soft-login.xyz"))
    print("URL:", is_valid_url("https://micr0soft-login.xyz"))
    print(
        "SHA256:",
        is_valid_sha256(
            "9ad8d1251a2bdbf205fc5c73de00a23957ace178b8d4c58ef575db4f59dfc20c"
        )
    )