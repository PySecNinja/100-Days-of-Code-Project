#!/usr/bin/env python3
#
#  [Program]
#
#  Regular Calculator
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
print(logo)

#add function
def add(n1, n2):
    return n1 + n2

#subtract function
def subtract(n1, n2):
    return n1 - n2 

#multiply function
def multiply(n1, n2):
    return n1 * n2

#divide function
def divide(n1, n2):
    return n1 / n2

#dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
} 

def calculator():
    num1 = float(input("Whats the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation.\n")
        num2 = float(input("Whats the next number?: "))
        calculation_function =  operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation\n") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()


#Ideas add square root add exponet, line 43 give user option to  quit calc