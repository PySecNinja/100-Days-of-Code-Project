#!/usr/bin/env python3
#
#  [Program]
#
#  Rock. Paper. Scissors. Shoot!
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

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("I am an AI bot created by drew. If you lose its because he is a great programmer.\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Sissors.")

list_of_attacks = [rock, paper, scissors]

if user_choice == "0":
    print(rock)
    user_choice = rock
elif user_choice == "1":
    print(paper)
    user_choice = paper
elif user_choice == "2":
    print(scissors)
    user_choice = scissors
else:
    print("Come on buddy! Can't you read directions? You didn't type any of the numbers listed.\nTry Again!")
    exit()

computer_choice = random.choice(list_of_attacks)

print("Computer Chose:")
print(computer_choice)

if computer_choice == rock and user_choice == scissors:
    print("You Lose!")
elif computer_choice == rock and user_choice == paper:
    print("You Win!")
elif computer_choice == scissors and user_choice == paper:
    print("You Lose!")
elif computer_choice == scissors and user_choice == rock:
    print("You Win!")
elif computer_choice == paper and user_choice == rock:
    print("You Lose!")
elif computer_choice == paper and user_choice == scissors:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw. Try Again.")

# Add a loop to this

#play again = input("Do you want to play again? Y or N \n")