#!/usr/bin/env python3
#
#  [Program]
#
#  Number Guessing Game
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
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1, 100) # Generate a pseudo-random number between 0 and 100.
# Uncomment below to troubleshoot code
# print(random_number)

#Runs the easy function
def easy():
    """plays the easy difficulty of the game"""
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a Guess\n"))
    game_over = False
    while not game_over:
        if attempts > 0:
            if guess > random_number:
                attempts -= 1
                print(f"Too High.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a Guess\n"))
            elif guess < random_number:
                attempts -= 1
                print(f"Too Low.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a Guess\n"))
            elif guess == random_number: 
                print(f"You Win! The answer was {random_number}")
                game_over = True
            else:
                game_over = True
        else:
            print(f"You Lose! The answer was {random_number}")
            game_over = True

#Runs the hard function
def hard():
    """plays the hard difficulty of the game"""
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a Guess\n"))
    game_over = False
    while not game_over:
        if attempts > 0:
            if guess > random_number:
                attempts -= 1
                print(f"Too High.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a Guess\n"))
            elif guess < random_number:
                attempts -= 1
                print(f"Too Low.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
                guess = int(input("Make a Guess\n"))
            elif guess == random_number: 
                print(f"You Win! The answer was {random_number}")
                game_over = True
            else:
                game_over = True
        else:
            print(f"You Lose! The answer was {random_number}")
            game_over = True

if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()
else:
    print("Wrong Input.")
    exit()


 
# Try to make the game play again || issue with global/local scope varriables if i create a start_game() function


# play_again = input("Would you like to play again? Type 'y' or 'n'. ")
# if play_again == 'y':
#     start_game()
# elif play_again == 'n':
#     exit()
# else:
#     exit()