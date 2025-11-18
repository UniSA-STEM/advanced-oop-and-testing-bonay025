"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    def __init__(self, name:str, species:str, age:int, diet:str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__health_record = []

    def make_sound(self):
        print("Making sound")

    def eat(self, food):
        print(f"Eating {food}")

    def sleep(self):
        print("Sleeping")

    def get_name(self):
        return self.__name

    def add_health_record(self, health_record):
        self.__health_record.append(health_record)

    def __str__(self):
        return (f"---{self.__name}--- \n"
                f"Age: {self.__age} \n"
                f"Species: {self.__species} \n"
                f"Diet: {self.__diet} \n")