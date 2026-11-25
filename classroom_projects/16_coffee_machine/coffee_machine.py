"""
Coffee Machine Project

Author: badDoggy
Date: 11/25/2026
"""

# ##########  Imports  ##############
import subprocess
import os
from ascii_art import logo


# #########  Functions  ##############
# Clear Screen & Print Logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


clear_screen()


# End the app
print("\n\n--  End of Line --\n")
