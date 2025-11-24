"""
File: filename.py
Description: This module holds a mammal class which represents animals
of type mammal.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Mammal(Animal):
    """This class represents a mammal subclass from the animal class."""
    def __init__(self, name, species, age, diet, environment_needs,
                 producing_milk=False):
        Animal.__init__(self, name, species, age, diet, environment_needs)
        self.__producing_milk = producing_milk

    def produce_milk(self):
        """This method allows the mammal to produce milk."""
        self.__producing_milk = True
        print(f"{self.get_name()} is producing milk.")

