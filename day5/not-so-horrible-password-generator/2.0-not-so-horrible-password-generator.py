
#!/usr/bin/env python3
#
#  [Program]
#
#  2.0  Not So Horrible Password Generator
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.


import random

print("Welcome to the Horrible Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters_in_password = int(input("How many letters would you like in your password?\n"))
symbols_in_password = int(input("How many symbols would you like?\n"))
numbers_in_password = int(input("How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, letters_in_password + 1):
   password_list.append(random.choice(letters))

for char in range(1, symbols_in_password +1):
    password_list +=(random.choice(symbols))

for char in range(1, numbers_in_password + 1):
    password_list += (random.choice(numbers))

random.shuffle(password_list)

# The Output of password_list is in a list right now and looks like ['s', ')', '5', '4', '%', '3', ')', 'G', '3', '&', 't', '3', 'O', '!', 'G']

# Next command uses a for loop to turn the list back into a string; basically getting rid of all the extra weird symboles above

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password} \nDont share it with Anyone!")


#Ideas to build upon: maybe change the code or create another .py file from this to not require so much user input just ask do you want a random password? 
