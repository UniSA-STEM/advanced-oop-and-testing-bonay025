"""
File: filename.py
Description: A brief description of this Python module.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

class HealthRecord:
    def __init__(self, issue, date, severity_level, treatment_plan, notes):
        self.__date = date
        self.__severity_level = severity_level
        self.__issue = issue
        self.__treatment_plan = treatment_plan
        self.__notes = notes

    def __str__(self):
        return (f"---{self.__issue}--- \n"
                f"Date: {self.__date} \n "
                f"Severity: {self.__severity_level} \n"
                f"Treatment Plan: {self.__treatment_plan} \n"
                f"Notes: {self.__notes}\n")

