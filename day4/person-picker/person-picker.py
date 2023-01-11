#!/usr/bin/env python3
#
#  [Program]
#
#  Person Picker
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

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items -1)
chosen = names[random_choice]

print(f"{chosen} has been chosen!")

#Loop this. 

#input("Would you like to choose another person? Y or N? \n")

#input("Would you like to use the same list or another list? Y or N? \n")