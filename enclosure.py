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

class Enclosure:
    """This class represents a zoo enclosure."""
    def __init__(self, size, environmental_type, cleanliness_level,
                 animal_species, animals=[]):
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness_level = cleanliness_level
        self.__animal_species = animal_species
        self.__animals = animals

    def __str__(self):
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"{animal.get_name()} \n"
        return (f"---{self.__animal_species} Enclosure--- \n"
                f"Size: {self.__size}m\u00b2\n"
                f"Environmental Type: {self.__environmental_type} \n"
                f"Cleanliness Level: {self.__cleanliness_level} \n"
                f"Animal Species: {self.__animal_species} \n"
                f"Animals: \n"
                f"{str_animals} \n")
