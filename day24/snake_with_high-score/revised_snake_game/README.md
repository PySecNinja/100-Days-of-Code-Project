# Steps to creating the snake game

### Saves the High score in a file called data.txt. Reset this back to zero if need be.

Create a snake body
Move the snake
Control the snake
Detect collision with food
Create a scoreboard
Detect collision with wall
Detect collision with tail

# Inheritance 

Class Inheritance helps in OOP

We can take an existing class and build on top of it with inheritance

# Slicing
In Python, "slicing" refers to taking a subset of elements from a sequence (such as a list, string, or tuple) and creating a new sequence with those elements. This is done by specifying a range of indices separated by a colon (:) within square brackets []. The syntax for slicing is as follows:

sequence[start:stop:step]

Lets say we want (c d e) in our list

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_keys[2:5]

Lets say we want everything but "do"

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[1:])

Maybe we want "do", "re", "mi"
print(piano_tuple[:3])


