"""
File: filename.py
Description: This module holds a class which generate zoo reports.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""


class Report:
    """This class generates zoo reports."""
    def __init__(self, zoo_animals=[], zoo_enclosures=[], zoo_staff=[]):
        self.__zoo_animals = zoo_animals
        self.__zoo_enclosures = zoo_enclosures
        self.__zoo_staff = zoo_staff

    def generate_animal_health_report(self, animal):
        """This method generates a report for animal health."""
        list_records = animal.get_health_record()
        if not list_records:
            print(f"**{animal.get_name()}**\n"
                  f"Status: {animal.get_health_status()}\n"
                  f"No current history.\n")
        else:
            str_records = ""
            for record in list_records:
                str_records += f"{record.get_issue()} {record.get_date()} \n"
            print(f"**{animal.get_name()}**\n"
                  f"Status: {animal.get_health_status()}\n"
                  f"{str_records}")

    def generate_zoo_health_report(self):
        """This method generates a report for all zoo animals
        health."""
        print(f"=== Health Report for All Animals ===")
        for animal in self.__zoo_animals:
            self.generate_animal_health_report(animal)

    def generate_animal_report(self):
        """This method generates a report for all zoo animals by
        species."""
        animal_species = {}
        for animal in self.__zoo_animals:
            animal_species[animal.get_species()] = []
        for animal in self.__zoo_animals:
            animal_species[animal.get_species()].append(animal)
        print(f"=== Animals in Zoo ===")
        str_animals = ""
        for species, animals in animal_species.items():
            str_animals += f"**{species}s** \n"
            for animal in animals:
                str_animals += f"{animal}\n"
        print(str_animals)

    def generate_enclosure_report(self):
        """This method generates a report for all zoo enclosures."""
        print(f"=== Enclosure Report ===")
        for enclosure in self.__zoo_enclosures:
            print(enclosure)

    def generate_staff_report(self):
        """This method generates a report for all zoo staff."""
        print(f"=== Staff Report ===")
        for staff in self.__zoo_staff:
            print(staff)

