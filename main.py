"""
File: enclosure.py
Description: This module hold the Enclosure class which represents a
zoo enclosure.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from enclosure import Enclosure

# Creates two animals of each species
Nala = Mammal("Nala", "Lion", 4, "Carnivore", "Savannah")
Leo = Mammal("Leo", "Lion", 4, "Carnivore", "Savannah")
Apollo = Mammal("Apollo", "Otter", 7, "Omnivore", "Aquatic")
Brandy = Mammal("Brandy", "Otter", 10, "Omnivore", "Aquatic")
Pebbles = Bird("Pebbles", "Little Penguin", 3, "Seafood", "Aquatic", 20)
Snowflake = Bird("Snowflake", "Little Penguin", 3, "Seafood", "Aquatic", 18)
Ollie = Bird("Ollie", "Barking Owl", 11, "Carnivore", "Savannah", 88)
Pascal = Bird("Pascal", "Barking Owl", 15, "Carnivore", "Savannah", 95)
Donna = Reptile("Donna", "Aldabra Tortoise", 70, "Herbivore", "Aquatic")
Melvin = Reptile("Melvin", "Aldabra Tortoise", 111, "Herbivore", "Aquatic")
Draco = Reptile("Draco", "Komodo Dragon", 22, "Carnivore", "Savannah")
Lizzie = Reptile("Lizzie", "Komodo Dragon", 17, "Carnivore", "Savannah")

print(Nala)

