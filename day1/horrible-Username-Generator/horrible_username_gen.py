#!/usr/bin/env python3
#
#  [Program]
#
#  Horrible-Username-Generator
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


# Time module allows the delay of commands
import time
# Random module creates random number
import random

# Create a greeting for your program.
print("Welcome to the The Horrible User Name Generator ")
#Creates a 1 second delay before promting for question
time.sleep(2)
# Ask the user for the city that they grew up in.
name_of_city = input("What's name of the city you grew in? ")
# Ask the user for the name of a pet.
name_of_pet = input("What's your pet's name? ")
# Combine the name of their city and pet and show them their band name.
random_number_gen = str(random.randint(0,100))

print("Your Horrible User Name could be " + name_of_city + random_number_gen + name_of_pet)

# Can build on this..ideas prompts for another try, add more questions, create more "randomness" with random module  
