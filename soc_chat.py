def ask_soc(question):

    question = question.lower()


    if "phishing" in question:

        return (
            "⚠️ Phishing detected.\n\n"
            "Indicators:\n"
            "- Suspicious sender\n"
            "- Social engineering language\n"
            "- Possible credential theft attempt\n\n"
            "MITRE ATT&CK:\n"
            "T1566 - Phishing\n\n"
            "Recommended Actions:\n"
            "1. Block sender\n"
            "2. Report email\n"
            "3. Reset affected credentials"
        )


    elif "malware" in question:

        return (
            "🦠 Malware investigation started.\n\n"
            "Recommended Actions:\n"
            "- Isolate affected host\n"
            "- Run endpoint scan\n"
            "- Review persistence mechanisms"
        )


    elif "mitre" in question:

        return (
            "⚔️ MITRE ATT&CK is a knowledge base "
            "of adversary tactics and techniques.\n\n"
            "Example:\n"
            "T1566 = Phishing"
        )


    elif "incident" in question:

        return (
            "📊 Incident response workflow:\n\n"
            "1. Identify\n"
            "2. Contain\n"
            "3. Eradicate\n"
            "4. Recover\n"
            "5. Document"
        )


    else:

        return (
            "🤖 SOC Assistant ready.\n\n"
            "Ask me about:\n"
            "- phishing\n"
            "- malware\n"
            "- MITRE ATT&CK\n"
            "- incident response"
        )