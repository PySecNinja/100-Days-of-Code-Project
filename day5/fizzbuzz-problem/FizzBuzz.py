#The code from 100 days of code

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)


# The code I came up with before seeing the 'solution' works but i think i used whats called nested if statements. 

number = 0
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("BuzzFizz")
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Control or command + '/' to uncomment or comment highlighted code
    
