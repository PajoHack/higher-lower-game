from art import logo, vs
from game_data import data
import random


def format_data(account):
    """
    Format the account data into printable format.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(f"Compare B: {format_data(account_b)}.")
