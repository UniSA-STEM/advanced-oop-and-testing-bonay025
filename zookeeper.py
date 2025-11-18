"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, first_name, last_name, role="Zookeeper"):
        Staff.__init__(self, first_name, last_name, role)
        self.__duties = []
        self.__enclosures = []

    def add_duty(self, duty):
        Staff.add_duty(self, duty)

    def add_enclosure(self, enclosure):
        self.__enclosures.append(enclosure)




