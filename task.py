"""
File: enclosure.py
Description: This module holds a task class for staff daily tasks.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""


class Task:
    """This class represents a task completed by staff."""
    def __init__(self, name, time, frequency):
        self.__name = name
        self.__time = time
        self.__frequency = frequency

    def __str__(self):
        return (f"Duty: {self.__name} \n"
                f"Time: {self.__time} \n"
                f"Frequency: {self.__frequency} \n")