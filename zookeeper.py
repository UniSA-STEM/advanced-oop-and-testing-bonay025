"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from mammal import Mammal
from staff import Staff
from enclosure import Enclosure
from task import Task

class Zookeeper(Staff):
    def __init__(self, first_name, last_name, role="Zookeeper"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__enclosure = None
        self.__animals = []

    def set_enclosure(self, enclosure):
        self.__enclosure = enclosure
        self.add_animal()

    def add_animal(self):
        list_animals = self.__enclosure.get_animals()
        for animal in list_animals:
            self.__animals.append(animal)

    def add_duty(self, duty):
        self.__duties.append(duty)

    def feed_animals(self):
        for animal in self.__animals:
            animal.eat()

    def clean_enclosure(self):
        self.__enclosure.clean()

    def __str__(self):
        if self.__enclosure is None:
            enclosure = ""
        else:
            enclosure = self.__enclosure.get_name()
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"- {animal.get_name()} \n"
        str_duties = ""
        for task in self.__duties:
            str_duties += f"{task}\n"
        return (f'Name: {Staff.get_first_name(self)} {Staff.get_last_name(self)} \n'
                f'Role: {Staff.get_role(self)} \n'
                f'Current responsibilities: \n'
                f'{str_duties}'
                f'Enclosure: {enclosure}\n'
                f'Animals: \n'
                f'{str_animals}\n')

