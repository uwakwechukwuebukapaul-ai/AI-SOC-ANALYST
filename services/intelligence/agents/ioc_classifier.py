"""
IOC Classifier

Responsible for identifying the type of an Indicator of Compromise (IOC).

Supported IOC Types

- IPv4 Address
- Domain
- URL
- Email Address
- MD5
- SHA1
- SHA256

The classifier is intentionally lightweight and deterministic.
Threat intelligence providers can later reuse this output.
"""

from __future__ import annotations

import ipaddress
import re
from enum import Enum


class IOCType(str, Enum):
    IP = "ip"
    DOMAIN = "domain"
    URL = "url"
    EMAIL = "email"
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    UNKNOWN = "unknown"


class IOCClassifier:
    """
    Detects IOC types.
    """

    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    URL_REGEX = re.compile(
        r"^(http|https)://",
        re.IGNORECASE,
    )

    DOMAIN_REGEX = re.compile(
        r"^(?!-)[A-Za-z0-9-]{1,63}"
        r"(\.[A-Za-z0-9-]{1,63})+$"
    )

    MD5_REGEX = re.compile(r"^[A-Fa-f0-9]{32}$")

    SHA1_REGEX = re.compile(r"^[A-Fa-f0-9]{40}$")

    SHA256_REGEX = re.compile(r"^[A-Fa-f0-9]{64}$")

    @classmethod
    def classify(cls, indicator: str) -> IOCType:
        """
        Detect the IOC type.

        Parameters
        ----------
        indicator:
            IOC value.

        Returns
        -------
        IOCType
        """

        indicator = indicator.strip()

        if cls._is_ip(indicator):
            return IOCType.IP

        if cls.EMAIL_REGEX.fullmatch(indicator):
            return IOCType.EMAIL

        if cls.URL_REGEX.match(indicator):
            return IOCType.URL

        if cls.MD5_REGEX.fullmatch(indicator):
            return IOCType.MD5

        if cls.SHA1_REGEX.fullmatch(indicator):
            return IOCType.SHA1

        if cls.SHA256_REGEX.fullmatch(indicator):
            return IOCType.SHA256

        if cls.DOMAIN_REGEX.fullmatch(indicator):
            return IOCType.DOMAIN

        return IOCType.UNKNOWN

    @staticmethod
    def _is_ip(value: str) -> bool:
        """
        Returns True if the value is a valid IPv4/IPv6 address.
        """

        try:
            ipaddress.ip_address(value)
            return True
        except ValueError:
            return False

    @classmethod
    def is_supported(cls, indicator: str) -> bool:
        """
        Returns True if the IOC type is supported.
        """

        return cls.classify(indicator) != IOCType.UNKNOWN