#!/usr/bin/env python3
#
#  [Program]
#
#  Higher Lower Game
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
from os import system, name
from art import logo, vs
from game_data import data

def clear():
    """clears the terminal screen for windows or unix"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

current_score = 0

gameover = False
while not gameover:
    print(logo)
    random_number = (random.randint(0,49))
    random_number_2 = (random.randint(0,49))

    follower_count = (data[random_number]["follower_count"])
    follower_count_2 = (data[random_number_2]["follower_count"])

    print(f"Compare A: {data[random_number]['name']}, a {data[random_number]['description']}, from {data[random_number]['country']}")
    # print(follower_count)     UNCOMMENT FOR TROUBLESHOOTING
    print(vs)
    print(f"Against B: {data[random_number_2]['name']}, a {data[random_number_2]['description']}, from {data[random_number_2]['country']}")
    # print(follower_count_2)   UNCOMMENT FOR TROUBLESHOOTING

    answer = input("Who has more followers on Instagram? 'A' or 'B': ").lower()
    if answer == 'a':
        if follower_count > follower_count_2:
            current_score += 1
            clear()
            print(f"You're right! Current score: {current_score}.")
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            gameover = True   
    elif answer == 'b':
        if follower_count_2 > follower_count:
            current_score += 1
            clear()
            print(f"You're right! Current score: {current_score}.")
        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            gameover = True   
    else:
        print("Wrong Input")
        gameover = True   


