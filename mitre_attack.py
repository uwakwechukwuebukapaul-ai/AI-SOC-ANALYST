MITRE = {

"phishing":
"T1566",

"credential theft":
"T1056",

"malware":
"T1204"

}


def get_attack(technique):
    return MITRE.get(
        technique,
        "Unknown"
    )