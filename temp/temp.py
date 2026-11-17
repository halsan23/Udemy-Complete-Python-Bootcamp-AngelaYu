"""
App Name

Author: badDoggy
Date: mm/dd/yyyy
"""

#####################################


# ###########  Imports  ##############
import subprocess
import os


# #########  Functions  ##############
# Clear Screen & display the logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


# Run App
############################################
# Clear Screen
clear_screen()


############################################


# End the app
print("\n\n--  End of Line --\n")
