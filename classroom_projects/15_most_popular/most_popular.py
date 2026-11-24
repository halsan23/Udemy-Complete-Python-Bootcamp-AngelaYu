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
    item_1 = item
    while True:
        item_2 = random.choice(data)
        if item_2 != item_1:
            break

    return item_1, item_2


# #########  Variables  ##############
correct = True
item_b = random.choice(data)
score = 0


while correct:
    clear_screen()
    item_a, item_b = get_next(item_b)

    print(
        f"A) {item_a['name']} is a {item_a['description']} from {item_a['country']}.\n"
    )
    print(f"   vs\n")
    print(
        f"B) {item_b['name']} is a {item_b['description']} from {item_b['country']}.\n"
    )

    again = input("\nSelect A, B, or Q)uit: ").lower()
    if again in ("q", "quit"):
        correct = False

    elif again == "a":
        if item_a["follower_count"] > item_b["follower_count"]:
            print(
                f"\nCorrect!! {item_a['name']} has {item_a['follower_count']} followers, while {item_b['name']} only has {item_b['follower_count']} followers."
            )
            score += 1
            input("\npress any key to continue: ")
        else:
            print(
                f"\nIncorrect!! {item_a['name']} only has {item_a['follower_count']} followers, while {item_b['name']} has {item_b['follower_count']} followers."
            )
            print("\nGame Over")
            correct = False


# End the app
print("\n\n--  End of Line --\n")
