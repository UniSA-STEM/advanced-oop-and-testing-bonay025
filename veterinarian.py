"""
File: filename.py
Description: This file hold a veterinarian staff member class.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff


class Veterinarian(Staff):
    """This represents a veterinarian staff member."""
    def __init__(self, first_name, last_name, role="Veterinarian"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__animals = []

    def add_animal(self, animal):
        """Assigns an animal to the veterinarian staff member."""
        self.__animals.append(animal)

    def add_duty(self, duty):
        """Adds a duty to the veterinarian staff member."""
        self.__duties.append(duty)

    def create_health_record(self, health_record, animal):
        """Creates a health record from the veterinarian staff member."""
        animal.add_health_record(health_record)
        print(f"Health record added for {animal.get_name()} by "
              f"{Staff.get_first_name(self)}.\n")

    def update_health_status(self, animal, status):
        """Updates the health status of an animal from the veterinarian staff member."""
        animal.set_health_status(status)
        print(f"Health status updated for {animal.get_name()} by "
              f"{Staff.get_first_name(self)}.\n")

    def __str__(self):
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"{animal.get_name()} \n"
        str_duties = ""
        for task in self.__duties:
            str_duties += f"{task} \n"
        return (f'Name: {Staff.get_first_name(self)} '
                f'{Staff.get_last_name(self)} \n'
                f'Role: {Staff.get_role(self)} \n'
                f'Current responsibilities: \n'
                f'{str_duties}'
                f'Animals: \n'
                f'{str_animals}')

