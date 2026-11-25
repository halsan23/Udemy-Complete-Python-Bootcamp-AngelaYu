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


def get_next(item):
    """
    Receives one item and selects a new random item from "data" for comparison.
    \nEach new round, item_1 becomes item_2 and item_2 gets a new assignment.
    """
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


def check_answer(user_choice, item_2, most_pop):
    """
    Check if user guess is correct
    \nReturns True or False
    """
    if user_choice["name"] == most_pop:
        print(
            f"\nCorrect, {user_choice['name']} has {user_choice['follower_count']} followers, and {item_2['name']} only has {item_2['follower_count']} -"
        )
        return True

    print(
        f"\nIncorrect, {user_choice['name']} only has {user_choice['follower_count']} followers, and {item_2['name']} has {item_2['follower_count']} -"
    )
    return False


def screen_display(user_score, item_1, item_2):
    """
    Clears the screen, displays the current score, and shows the two choices.
    """
    clear_screen()
    # Running display for current score
    print(f"Your Current Score: {user_score}\n")

    # display the two contestants for the user choice
    print(f"A) {item_1['name']}, {item_1['description']} from {item_1['country']}.\n")
    print("   or\n")
    print(f"B) {item_2['name']}, {item_2['description']} from {item_2['country']}.\n")


# #########  Variables  ##############
correct = True
result = False
item_b = random.choice(data)
score = 0


while correct:
    # get two items from "data" to compare and set "most popular"
    item_a, item_b, most_popular = get_next(item_b)
    # clear the screen, reset choice = '', display user choices
    choice = ""
    screen_display(score, item_a, item_b)

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
            choice = ""
            screen_display(score, item_a, item_b)

    # Check user's guess
    if choice == "a":
        result = check_answer(item_a, item_b, most_popular)
    elif choice == "b":
        result = check_answer(item_b, item_a, most_popular)

    if result:
        input("\npress any key to continue...")
        score += 1

    else:
        print(f"\nGame Over with a final score of {score}")
        correct = False


# End the app
print("\n\n--  End of Line --\n")
