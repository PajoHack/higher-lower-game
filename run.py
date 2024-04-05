from art import logo, vs
from game_data import data
import random
import os


def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for Unix (Linux, macOS)
    else:
        _ = os.system('clear')


def format_data(account):
    """
    Formats the account data into a printable string.
    
    Parameters:
    - account (dict): Account information including name, description, and country.
    
    Returns:
    - str: Formatted string describing the account.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """
    Determines if the user's guess is correct based on follower counts.
    
    Parameters:
    - guess (str): The user's guess ('a' or 'b').
    - a_followers (int): Follower count for account A.
    - b_followers (int): Follower count for account B.
    
    Returns:
    - bool: True if the guess is correct, False otherwise.
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0 # Initialize the score
game_should_continue = True # Flag to control game loop
account_b = random.choice(data) # Pre-select account B to start the comparison

while game_should_continue:
    
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        game_should_continue = False
        print(f"Sorry, that's incorrect :( Final score: {score}")
