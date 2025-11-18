"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
import enclosure
from mammal import Mammal
from staff import Staff
from enclosure import Enclosure

class Zookeeper(Staff):
    def __init__(self, first_name, last_name, role="Zookeeper"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__enclosure = None
        self.__animals = []

    def add_duty(self, duty):
        Staff.add_duty(self, duty)

    def set_enclosure(self, enclosure):
        self.__enclosure = enclosure
        self.add_animal()

    def add_animal(self):
        list_animals = self.__enclosure.get_animals()
        for animal in list_animals:
            self.__animals.append(animal)






