"""
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Staff:
    def __init__(self, staff_name, role):
        self.__staff_name = staff_name
        self.__role = role
        self.__responsibilities = []

    def add_responsibility(self, responsibility):
        self.__responsibilities.append(responsibility)

    def __str__(self):
        return (f'Name: {self.__staff_name}\n'
                f'Role: {self.__role}\n'
                f'Current responsibilities: {self.__responsibilities}\n')

