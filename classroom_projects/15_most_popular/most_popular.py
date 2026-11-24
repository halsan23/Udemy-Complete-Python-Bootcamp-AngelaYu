"""
Most Popular game

Author: badDoggy
Date: 11/23/2026
"""

# ##########  Imports  ##############
import subprocess
import os
from ascii_art import logo
from game_data import data


# #########  Functions  ##############
# Clear Screen & Print Logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


clear_screen()


for idx, item in enumerate(data):
    print(f"{item['name']} is a {item['description']} from {item['country']}.\n")


# End the app
print("\n\n--  End of Line --\n")
