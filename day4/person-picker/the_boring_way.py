import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_choice = random.random_choice(names)
print(random_choice + "has been chosen!")