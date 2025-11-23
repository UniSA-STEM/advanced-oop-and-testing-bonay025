"""
File: filename.py
Description: A brief description of this Python module.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from mammal import Mammal
from staff import Staff
from healthRecord import HealthRecord

class Veterinarian(Staff):
    def __init__(self, first_name, last_name, role="Veterinarian"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)
        self.add_duty()

    def add_duty(self, duty):
        self.__duties.append(duty)

    def create_health_record(self, health_record, animal):
        animal.add_health_record(health_record)
        print(f"Health record added for {animal.get_name()} by {Staff.get_first_name(self)}.\n")

    def update_health_status(self, animal, status):
        animal.set_health_status(status)
        print(f"Health status updated for {animal.get_name()} by {Staff.get_first_name(self)}.\n")

    def __str__(self):
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"{animal.get_name()} \n"
        str_duties = ""
        for task in self.__duties:
            str_duties += f"{task} \n"
        return (f'Name: {Staff.get_first_name(self)} {Staff.get_last_name(self)} \n'
                f'Role: {Staff.get_role(self)} \n'
                f'Current responsibilities: \n'
                f'{self.__duties}'
                f'Animals: \n'
                f'{str_animals}\n')

