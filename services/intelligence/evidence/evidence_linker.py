"""
Sentinel DNA Evidence Linker

Creates relationships between evidence.
"""

from __future__ import annotations

from typing import Any


class EvidenceLinker:

    def __init__(self):

        self.links: list[dict[str, Any]] = []


    def link(
        self,
        source_id: str,
        target_id: str,
        relationship: str,
    ):

        link = {

            "source": source_id,

            "target": target_id,

            "relationship": relationship,

        }


        self.links.append(
            link
        )


        return link



    def get_links(self):

        return self.links