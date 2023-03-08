#!/usr/bin/env python3
#
#  [Program]
#
#  Secret Auction Program
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

from art import logo
from os import system, name
def clear():
    if name == 'nt':
        _ + system('cls')
    else:
        _ = system('clear')

print(logo)
print("Welcome to the secret auction program.\n")
bids = {}
other_bidders = False

def find_highest_bidder(bidding_reccord):
    highest_bid = 0 
    winner = ""
    # bidding_record = {"cain": 15, "abel: 31"}
    for bidder in bidding_reccord:
        bid_amount = bidding_reccord[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid anount of ${highest_bid}.")        

while not other_bidders:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "yes":
        clear()
        print(logo)
        other_bidders = False
    elif other_bidders == "no":
        other_bidders = True
        find_highest_bidder(bids)
    else:
        print("Wrong Input\n GoodBye!")
        exit()
        






