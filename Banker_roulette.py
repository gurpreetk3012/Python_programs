# Banker Roulette - Who will pay the bill

import random

names = input("Enter names of the people who are splitting the bill with a comma and a space:\n").split(", ")
length = len(names)
random_number = random.randint(0, length-1)
print(names[random_number])