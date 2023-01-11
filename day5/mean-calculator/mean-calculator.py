#!/usr/bin/env python3
#
#  [Program]
#
#  Mean Calculator
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




list_num = input("Give me a list of number's. Ill find the Mean. ").split()
for n in range(0, len(list_num)):
  list_num[n] = int(list_num[n])

num_added = 0 
for num in list_num:
    num_added += num
 

total_num = 0
for num in list_num:
    total_num += 1

mean_of_list = round(num_added / total_num)
print(f"The rounded mean is {mean_of_list}.")

#Ideas to build  loop and ask if it wants the mean rounded or not

