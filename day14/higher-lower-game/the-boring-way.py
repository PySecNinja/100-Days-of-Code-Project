from art import logo, vs
from os import system, name
from game_data import data
import random

def clear():
    """clears the terminal screen for windows or unix"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def format_data(account):
    """Takes the account data and returns into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    acount_country = account["country"]
    return (f"{account_name}, a {account_descr} from {acount_country}")

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower count and returns if they got it right."""
    if a_followers > b_followers:
      return guess == "a"
    else:
        return guess == "b"

score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    print(logo)
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Check if user is correct
    guess = input("Who has more Instagram followers? Type 'A' or 'B' ").lower()

    # Check if user is correct
    # Get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    #Clears the screen    
    clear()
    
    # Give user feedback on their guess.
    # Score Keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        game_should_continue =  False
        print(f"Sorry thats wrong. Final score: {score}")
        

    #make account at position B becomew the next account possible
