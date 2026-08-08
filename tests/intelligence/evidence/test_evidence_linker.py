from services.intelligence.evidence.evidence_linker import (
    EvidenceLinker,
)


def test_link():

    linker = EvidenceLinker()


    linker.link(
        "case-1",
        "ioc-1",
        "contains",
    )


    assert len(
        linker.get_links()
    ) == 1