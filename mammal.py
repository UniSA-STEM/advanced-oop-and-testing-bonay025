"""
File: filename.py
Description: A brief description of this Python module.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal

class Mammal(Animal):
    """This class represents a mammal subclass from the animal class."""
    def __init__(self, name, species, age, diet, environment_needs, producing_milk=False):
        Animal.__init__(self, name, species, age, diet, environment_needs)
        self.__producing_milk = producing_milk

    def produce_milk(self):
        self.__producing_milk = True
        print(f"{self.get_name()} is producing milk.")

