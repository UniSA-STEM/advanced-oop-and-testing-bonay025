"""
File: enclosure.py
Description: This module holds a demonstration script of the zoo system.
Author: Amelia Bond
ID: 110457542
Username: bonay025
This is my own work as defined by the University's Academic Integrity Policy.
"""
from healthRecord import HealthRecord
from mammal import Mammal
from reptile import Reptile
from bird import Bird
from enclosure import Enclosure
from report import Report
from veterinarian import Veterinarian
from zookeeper import Zookeeper
from task import Task


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

# Create list for zoo animals
zoo_animals = [Nala, Leo, Apollo, Brandy, Pebbles, Snowflake, Ollie, Pascal, Donna, Melvin, Draco, Lizzie]

# Creates six enclosures, one for each species
enclosure1 = Enclosure("Enclosure1",100, "Savannah", "Lion")
enclosure2 = Enclosure("Enclosure2",100, "Savannah", "Barking Owl")
enclosure3 = Enclosure("Enclosure3",100, "Savannah", "Komodo Dragon")
enclosure4 = Enclosure("Enclosure4",100, "Aquatic", "Otter")
enclosure5 = Enclosure("Enclosure5",100, "Aquatic", "Little Penguin")
enclosure6 = Enclosure("Enclosure6",100, "Aquatic", "Aldabra Tortoise")

# Creates list for zoo enclosures
zoo_enclosures = [enclosure1, enclosure2, enclosure3, enclosure4, enclosure5, enclosure6]

# Add animals to enclosures
enclosure1.add_animal(Nala)
# Shows trying to add a different species to an enclosure
enclosure1.add_animal(Draco)
# Shows trying to add a species with different environmental needs
enclosure1.add_animal(Brandy)
enclosure1.add_animal(Leo)
enclosure2.add_animal(Ollie)
enclosure2.add_animal(Pascal)
enclosure3.add_animal(Draco)
enclosure3.add_animal(Lizzie)
enclosure4.add_animal(Apollo)
enclosure4.add_animal(Brandy)
enclosure5.add_animal(Pebbles)
enclosure5.add_animal(Snowflake)
enclosure6.add_animal(Donna)
enclosure6.add_animal(Melvin)

# Create Staff
ben = Zookeeper("Ben", "Smith")
jane = Veterinarian("Jane", "Doe")
bob = Zookeeper("Bob", "Jones")

# Creates list for zoo staff
zoo_staff = [ben, jane, bob]

# Adds zoo information to report class
report = Report(zoo_animals, zoo_enclosures, zoo_staff)

# Generates reports for animals, enclosures and staff
report.generate_enclosure_report()
report.generate_animal_report()
report.generate_staff_report()

# Add an enclosure to Ben and add duties
ben.set_enclosure(enclosure1)
ben.add_duty(Task("Feed Lions", "9am", "Daily"))
ben.add_duty(Task("Clean enclosure", "8pm Tuesday", "Weekly"))
print(ben)

# Assign animals to Jane
jane.add_animal(Apollo)
jane.add_animal(Brandy)

#Create a health record and update health status
jane.create_health_record(HealthRecord("Broken Leg", "10/08/25",
                                       "Serious",
                                       "Place in cast", "Monitor weekly"), Apollo)
jane.update_health_status(Apollo, "Under Treatment")

# Generates reports for one and all animals
report.generate_animal_health_report(Apollo)
report.generate_zoo_health_report()

# Trying to remove an animal under treatment from an enclosure
enclosure4.remove_animal(Apollo)

zoo_animals.remove(Donna)

report.generate_animal_report()

