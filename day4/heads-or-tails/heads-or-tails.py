#!/usr/bin/env python3
#
#  [Program]
#
#  Heads or Tails
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

ready_to_play = input("Welcome to heads or tails! Are you ready to play? Y or N\n").lower()
if ready_to_play == "n":
    print("Goodbye!")
    exit()
elif ready_to_play == "y":
    ask_question = input("Heads or Tails. Press \"enter\" to toss the coin!")
    random_number = random.randint(0, 1)
    if random_number == 0:
        print("Heads will roll!")
    elif random_number == 1:
        print("Tails never fails")
else:
    print("Did you just try to SQL inject me?")
    exit()

#Ideas to build on import time module and have the user click enter and show an ASCII coin fliping 