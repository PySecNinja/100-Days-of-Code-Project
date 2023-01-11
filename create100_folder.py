import os

numbers = list(range(1, 101))

for number in numbers:
    path = "day" + str(number)
    if not os.path.exists(path):
        os.mkdir(path)
