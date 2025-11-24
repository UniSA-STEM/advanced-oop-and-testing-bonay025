"""
File: enclosure.py
Description: This module holds a reptile class which represents animals
of type reptile.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal


class Reptile(Animal):
    """This class represents a reptile subclass of Animal."""
    def __init__(self, name, species, age, diet, environment_needs,
                 laid_eggs = False):
        Animal.__init__(self, name, species, age, diet, environment_needs)
        self.__laid_eggs = laid_eggs

    def lay_eggs(self):
        """This method allows the reptile to lay eggs."""
        self.__laid_eggs = True
        print(f"{self.get_name()} has laid eggs")

