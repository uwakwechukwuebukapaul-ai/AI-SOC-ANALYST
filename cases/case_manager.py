"""
Sentinel DNA

Case Management System

Handles security investigations.
"""

import uuid
from datetime import datetime



class CaseManager:


    def __init__(self):

        self.cases = {}



    def create_case(
        self,
        title,
        severity,
        description
    ):


        case_id = (

            "CASE-"

            +

            str(uuid.uuid4())[:8].upper()

        )


        case = {


            "case_id":

                case_id,


            "title":

                title,


            "severity":

                severity,


            "description":

                description,


            "status":

                "OPEN",


            "created":

                str(datetime.now()),


            "evidence":

                [],


            "timeline":

                []

        }


        self.cases[case_id] = case


        return case





    def get_case(
        self,
        case_id
    ):

        return self.cases.get(
            case_id
        )




    def update_status(
        self,
        case_id,
        status
    ):


        if case_id in self.cases:

            self.cases[case_id][
                "status"
            ] = status


            return True


        return False





    def list_cases(self):

        return list(
            self.cases.values()
        )



case_manager = CaseManager()