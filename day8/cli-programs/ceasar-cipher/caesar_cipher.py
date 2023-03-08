#!/usr/bin/env python3
#
#  [Program]
#
#  Ceaser Cipher
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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)                     #What happens if the user enters a number/symbol/space?
        new_position = position + shift_amount              #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        end_text += alphabet[new_position]                  #e.g. start_text = "meet me at 3"
    else:                                                   #end_text = "•••• •• •• 3"
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
print(logo)

#Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Try creating a while loop that continues to execute the program if the user types 'yes'. 
    
# play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Think about how you can use the modulus (%).
    shift = shift % 26 
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if play_again == "yes":
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    elif play_again == "no":
        should_continue = False
        print("Goodbye")
    else:
        print("You didnt type 'yes' or 'no'\n Goodbye!")
        exit() # can flip should_continue=False or just use exit() cmd