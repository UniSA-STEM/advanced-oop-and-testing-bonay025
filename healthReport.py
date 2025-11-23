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

    def generate_animal_health_report(self, animal):
        list_records = animal.get_health_record()
        if not list_records:
            print(f"Health Report for {animal.get_name()}\n"
                  f"No current health information available for {animal.get_name()}\n")
        else:
            str_records = ""
            for record in list_records:
                str_records += f"{record} \n"
            print(f"Health Report for {animal.get_name()}\n"
                  f"{str_records}")

    def generate_zoo_health_report(self, zoo):
        print(f"---Health Report for All Animals---")
        for animal in zoo:
            self.generate_animal_health_report(animal)
