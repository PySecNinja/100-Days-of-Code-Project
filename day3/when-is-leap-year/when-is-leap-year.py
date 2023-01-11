#!/usr/bin/env python3
#
#  [Program]
#
#  When is leap year?
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

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The {year} is a leap year.")
        else:
            print(f"The {year} is not a leap year.")
    else:
        print(f"The {year} is a leap year.")
else:
    print(f"The {year} is not a leap year.")

#The code below should work too.

# if (year % 4) == 0:
#     print(f"The {year} is a leap year.")
# elif (year % 100) == 0:
#     print(f"the {year} is a leap year.")
# elif (year % 400) == 0:
#     print(f"The {year} is a leap year.")
# else:
#     print(f"The {year} is not a leap year.")

