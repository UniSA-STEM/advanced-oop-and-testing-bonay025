"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Staff:
    def __init__(self, first_name, last_name, role):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role
        self.__duties = []

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_role(self):
        return self.__role

    def add_duty(self, duty):
        self.__duties.append(duty)

    def __str__(self):
        return (f'Name: {self.__first_name} {self.__last_name}\n'
                f'Role: {self.__role}\n'
                f'Current responsibilities: {self.__duties}\n')

