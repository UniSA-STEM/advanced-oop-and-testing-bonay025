"""
File: enclosure.py
Description: This module hold the Animal class which represents an animal.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    """This class represents an animal."""
    def __init__(self, name:str, species:str, age:int, diet:str,
                 environment_needs):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__environment_needs = environment_needs
        self.__health_record = []
        self.__health_status = "Healthy"

    def get_name(self):
        return self.__name

    def get_health_record(self):
        return self.__health_record

    def set_health_status(self, status:str):
        self.__health_status = status

    def get_health_status(self):
        return self.__health_status

    def get_species(self):
        return self.__species

    def get_environment_needs(self):
        return self.__environment_needs

    def make_sound(self, sound:str):
        """This method makes the animal make a sound."""
        print(f"{sound}\n")

    def eat(self):
        """This method makes the animal eat."""
        print(f"{self.__name} is eating food.\n")

    def sleep(self):
        """This method makes the animal sleep."""
        print(f"{self.__name} is sleeping.\n")

    def add_health_record(self, health_record):
        """This method adds a health record to the animal history."""
        self.__health_record.append(health_record)

    def __str__(self):
        str_health_record = ""
        for health_record in self.__health_record:
            str_health_record += f"{health_record.get_issue()} \n"
        return (f"--{self.__name}-- \n"
                f"Age: {self.__age} \n"
                f"Species: {self.__species} \n"
                f"Diet: {self.__diet} \n"
                f"Status: {self.__health_status} \n"
                f"Health record: {str_health_record}\n")