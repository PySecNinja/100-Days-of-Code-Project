#!/usr/bin/env python3
#
#  [Program]
#
#  Tip Calculator
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


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12,15 or 20? "))
number_of_people = int(input("How many people to split the bill? "))

bill_with_tip = tip_percentage / 100 
total_tip_amount = bill * bill_with_tip
total_bill = bill + total_tip_amount
bill_perperson = total_bill / number_of_people
final_amount = "{:.2f}".format(bill_perperson)

print(f"Each person should pay: ${final_amount} ")

#The variable(bill_with_tip) can be broken down into a different formula. Feel free to comment ideas
