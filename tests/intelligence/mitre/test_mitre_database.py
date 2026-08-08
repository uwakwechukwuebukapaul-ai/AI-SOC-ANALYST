from services.intelligence.mitre.mitre_database import (
    MitreDatabase,
)


def test_database():

    database = MitreDatabase()


    technique = database.get(
        "T1566"
    )


    assert technique.name == "Phishing"