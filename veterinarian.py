"""
File: filename.py
Description: A brief description of this Python module.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
from mammal import Mammal
from staff import Staff

class Veterinarian(Staff):
    def __init__(self, first_name, last_name, role="Vetinarian"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)
        self.add_duty()

    def add_duty(self):
        for animal in self.__animals:
            self.__duties.append(f"Health checks for {animal.get_name()}")

    def __str__(self):
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"{animal.get_name()} \n"
        return (f'Name: {Staff.get_first_name(self)} {Staff.get_last_name(self)} \n'
                f'Role: {Staff.get_role(self)} \n'
                f'Current responsibilities: {self.__duties}\n'
                f'Animals: \n'
                f'{str_animals}\n')
