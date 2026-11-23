"""
Most Popular game

Author: badDoggy
Date: 11/23/2026
"""

# ##########  Imports  ##############
import subprocess
import os
from game_data import data


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


clear_screen()


for idx, item in enumerate(data):
    description = f"{item['name']} is a {item['description']} from {item['country']}."
    print()
    print(description)


# End the app
print("\n\n--  End of Line --\n")
