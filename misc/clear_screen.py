"""
Clear Screen

Author: badDoggy
Date: 11/17/2026
"""

#####################################


# ##########  Imports  ##############
import subprocess
import os


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


clear_screen()


# End the app
print("\n\n--  End of Line --\n")
