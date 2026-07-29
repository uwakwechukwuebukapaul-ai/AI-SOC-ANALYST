from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import json



def generate_pdf(incident):


    filename = (
        f"SOC_Incident_Report_{incident[0]}.pdf"
    )


    doc = SimpleDocTemplate(filename)



    styles = getSampleStyleSheet()


    content = []



    content.append(
        Paragraph(
            "🤖 AI SOC Incident Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            f"Incident ID: {incident[0]}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Time: {incident[1]}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Threat: {incident[2]}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Severity: {incident[3]}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Risk Score: {incident[4]}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"MITRE ATT&CK: {incident[5]}",
            styles["Normal"]
        )
    )



    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            "⚡ Automated Response",
            styles["Heading2"]
        )
    )



    content.append(
        Paragraph(
            f"Status: {incident[7]}",
            styles["Normal"]
        )
    )



    try:

        actions = json.loads(
            incident[8]
        )


        for action in actions:

            content.append(

                Paragraph(

                    f"✓ {action}",

                    styles["Normal"]

                )

            )


    except:


        content.append(

            Paragraph(

                "No response actions",

                styles["Normal"]

            )

        )



    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            "🔎 Evidence",
            styles["Heading2"]
        )
    )



    try:

        evidence = json.loads(
            incident[12]
        )


        for key,value in evidence.items():

            content.append(

                Paragraph(

                    f"{key}: {value}",

                    styles["Normal"]

                )

            )


    except:


        content.append(

            Paragraph(

                "No evidence available",

                styles["Normal"]

            )

        )




    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            "🕒 Investigation Timeline",
            styles["Heading2"]
        )
    )



    try:

        timeline = json.loads(
            incident[13]
        )


        for event in timeline:


            content.append(

                Paragraph(

                    f"{event['time']} - {event['event']}",

                    styles["Normal"]

                )

            )


    except:


        content.append(

            Paragraph(

                "No timeline available",

                styles["Normal"]

            )

        )




    doc.build(content)



    return filename