# This is a keyword argument 

# Keyword argument > Positional argument
# * most of the time but depending on the need

# See how greet_with is using n= and l= to define argument

name = input("what name do you want?\n")
location = input("what location do you want?\n")

def greet_with(n=name, l=location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with(l=location, n=name)