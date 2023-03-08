# This is a positional argument 

# Keyword arguments > Positional arguments
# * most of the time but depending on the need

# Section 1
# See line 11 and line 15
# Name and location are in the same postion

name = input("what name do you want?\n")
location = input("what location do you want?\n")

def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with(name, location)

#Section 2
# See line 25 and line 29
# Name and location are in the swapped postion
# This code wont run as expected
name = input("what name do you want?\n")
location = input("what location do you want?\n")

def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with(location, name)
