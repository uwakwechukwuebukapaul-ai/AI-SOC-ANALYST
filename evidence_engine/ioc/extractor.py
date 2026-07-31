"""
Sentinel DNA
IOC Extraction Engine

Extracts Indicators of Compromise
from security evidence.
"""

import re


class IOCExtractor:


    def __init__(self):

        self.patterns = {


            "ipv4": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",


            "email":
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",


            "url":
            r"https?://[^\s]+",


            "domain":
            r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",


            "md5":
            r"\b[a-fA-F0-9]{32}\b",


            "sha1":
            r"\b[a-fA-F0-9]{40}\b",


            "sha256":
            r"\b[a-fA-F0-9]{64}\b"

        }



    def extract(
        self,
        text
    ):

        """

        Extract all indicators.

        """


        results = {}


        for name, pattern in self.patterns.items():


            matches = re.findall(

                pattern,

                text

            )


            results[name] = list(

                set(matches)

            )


        return results




    def summary(
        self,
        text
    ):


        indicators = self.extract(text)


        total = sum(

            len(value)

            for value in indicators.values()

        )


        return {

            "total_indicators":
                total,

            "indicators":
                indicators

        }



ioc_extractor = IOCExtractor()