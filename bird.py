"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet, environment_needs, flying = True):
        Animal.__init__(self, name, species, age, diet, environment_needs)
        self.__flying = flying

    def fly(self):
        if self.__flying:
            print(f"{self.get_name()} is flying.")
        else:
            print(f"{self.get_name()} cannot flying.")

