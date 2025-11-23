"""
File: filename.py
Description: A brief description of this Python module.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""


class HealthReport:
    def __init__(self):
        self.__health_records = []

    def generate_zoo_health_report(self, zoo):
        print(f"---Health Report for All Animals---")
        for animal in zoo:
            self.generate_animal_health_report(animal)
