import random

print("Welcome to the Horrible Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters_in_password = int(input("How many letters would you like in your password?\n"))
symbols_in_password = int(input("How many symbols would you like?\n"))
numbers_in_password = int(input("How many numbers would you like?\n"))

password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#This is easy for a hacker to crack if they figure out the positioning of the letters, symbols and numbers are in the same spot everytime.

for char in range(1, letters_in_password + 1):
   password += random.choice(letters)

for char in range(1, symbols_in_password +1):
    password += random.choice(symbols)

for char in range(1, numbers_in_password + 1):
    password += random.choice(numbers)

print(f"Here is your password: {password} \nDont share it with Anyone!")


#Try to fix this before looking at 2.0-not-so-horrible-password-generator.py
