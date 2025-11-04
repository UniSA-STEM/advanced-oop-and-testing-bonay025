"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    def __init__(self, name:str, species:str, age:int, diet:str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet

    def __str__(self):
        return (f"---{self.__name}--- \n"
                f"Age: {self.__age} \n"
                f"Species: {self.__species} \n"
                f"Diet: {self.__diet} \n")