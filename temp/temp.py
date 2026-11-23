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


# Class Code
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(20)


############################################


# End the app
print("\n\n--  End of Line --\n")
