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
    def __init__(self, name, size, environmental_type, animal_species, cleanliness_level="Clean"):
        self.name = name
        self.__size = size
        self.__environmental_type = environmental_type
        self.__cleanliness_level = cleanliness_level
        self.__animal_species = animal_species
        self.__animals = []

    def get_name(self):
        return self.__name

    def get_animals(self):
        return self.__animals

    def add_animal(self, animal):
        """Adds an animal to the enclosure."""
        if animal.get_environment_needs() != self.__environmental_type:
            print(f"This enclosure does not have the right environment type for {animal.get_name()}.\n")
        elif animal.get_species() != self.__animal_species:
            print(f"This enclosure is for {self.__animal_species}s, {animal.get_name()} is a {animal.get_species()}.\n")
        else:
            self.__animals.append(animal)
            self.__animal_species = animal.get_species()

    def remove_animal(self, animal):
        """Removes an animal from the enclosure."""
        health_status = animal.get_health_status()
        if health_status == "Under Treatment":
            print(f"{animal.get_name()} is currently under treatment and cannot be moved.\n")
        else:
            self.__animals.remove(animal)

    def clean(self):
        self.__cleanliness_level = "Clean"

    def __str__(self):
        str_animals = ""
        for animal in self.__animals:
            str_animals += f"- {animal.get_name()} \n"
        return (f"---{self.__animal_species} Enclosure--- \n"
                f"Size: {self.__size}m\u00b2\n"
                f"Environmental Type: {self.__environmental_type} \n"
                f"Cleanliness Level: {self.__cleanliness_level} \n"
                f"Animal Species: {self.__animal_species} \n"
                f"Animals: \n"
                f"{str_animals} \n")
