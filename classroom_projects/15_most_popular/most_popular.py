"""
Most Popular game

Author: badDoggy
Date: 11/23/2026
"""

# ##########  Imports  ##############
import subprocess
import os
import random
from ascii_art import logo
from game_data import data


# #########  Functions  ##############
# Clear Screen & Print Logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)
    # score = max(score, 0)
    # print(f"Current Score: {score}\n\n")


def get_next(item):
    # get two random items from "data" for user to compare
    # each new round, item_1 becomes item_2 and item_2 gets a new assignment
    item_1 = item
    while True:
        item_2 = random.choice(data)
        if item_2 != item_1:
            break

    # check which is most popular
    if item_1["follower_count"] > item_2["follower_count"]:
        most_pop = item_1["name"]
    else:
        most_pop = item_2["name"]

    return item_1, item_2, most_pop


def check_answer(item, item_2, most_pop):
    if item["name"] == most_pop:
        print("\n- Correct Guess -")
        print(
            f"- {item['name']} has {item['follower_count']} followers, and {item_2['name']} only has {item_2['follower_count']} -"
        )
        return True

    print("\n- Incorrect Guess -")
    print(
        f"- {item['name']} has only {item['follower_count']} followers, and {item_2['name']} has {item_2['follower_count']} -"
    )
    return False


def reset(score):
    # clear the screen and get the two contestants
    # also determines which is most popular and returns their name
    clear_screen()
    choice = ""
    # Running display for current score
    print(f"Your Current Score: {score}\n")

    # display the two contestants for the user choice
    print(f"A) {item_a['name']}, {item_a['description']} from {item_a['country']}.\n")
    print("   or\n")
    print(f"B) {item_b['name']}, {item_b['description']} from {item_b['country']}.\n")

    return choice


# #########  Variables  ##############
correct = True
result = False
item_b = random.choice(data)
score = 0


while correct:
    # get two items from "data" to compare and set "most popular"
    item_a, item_b, most_popular = get_next(item_b)
    # clear the screen, reset choice = '', display user choices
    choice = reset(score)

    # input for users choice
    while choice not in ("a", "b", "q", "quit"):
        choice = input("\nSelect A, B, or Q)uit: ").lower()

        # Option for user to Quit the game
        if choice in ("q", "quit"):
            correct = False

        # Invalid input
        elif choice not in ("a", "b"):
            print("\nInvalid Input!!  A, B, or Q)uit only!!")
            input("press any key to continue ...")
            choice = reset(score)

    # Check user's guess
    if choice == "a":
        result = check_answer(item_a, item_b, most_popular)
    elif choice == "b":
        result = check_answer(item_b, item_a, most_popular)

    if result:
        input("\npress any key to continue...")
        score += 1

    else:
        print("\n- Game Over -")
        correct = False


# End the app
print("\n\n--  End of Line --\n")
