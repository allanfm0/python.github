from art import logo
from art import vs
from game_data import data
import os

import random


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    accout_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {accout_descr}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and followers counts and returns if they got it rigth."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_corret = check_answer(guess, a_follower_count, b_follower_count)


    if is_corret:
        score += 1
        print(f"You're rigth. current score: {score}.\n")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
