#!/usr/bin/env python3
#
#  [Program]
#
#  How much time is left?
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

age = input("What is your current age? ")

lifespan = input("What age do you to expect to live too? The average lifespan in America is 77 years? ")

age_as_int = int(age)
lifespan_as_int =int(lifespan)

average_lifespan_america = 77

months_want_live = lifespan_as_int * 12
weeks_want_live = lifespan_as_int * 52
days_want_live = lifespan_as_int * 365

months_lived = age_as_int * 12
weeks_lived = age_as_int * 52
days_lived = age_as_int * 365

months_left = months_want_live - months_lived
weeks_left = weeks_want_live - weeks_lived
days_left = days_want_live - days_lived


message = f"\nYou have currently lived for {months_lived} months, {weeks_lived} weeks, and {days_lived} days. According to your expected amount of {lifespan} years to live, you have {days_left} days left, {weeks_left} weeks left, and {months_left} months left."
print(message)

# Can build this out further..Ideas include: Look at other countries average age and prompt user 
# to answer what country they are from, go grainular down to the seconds, add an exact 'Expiration date'...lol 
