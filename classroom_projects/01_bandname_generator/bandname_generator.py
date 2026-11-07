# Simple Band Name Generator that shows
# how to combine inputs for a single output
# -----------------------------------------------------------
# badDoggy | 10/18/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


# Title & Description
# -----------------------------------------------------------
clear_screen()
print("Band Name Generator")

print('We\'re going to help you create a "Band Name".\n')


# Inputs
# -----------------------------------------------------------
city = input("Which city did you grow up in? ")
pet = input("What is the name of your favorite pet? ")


# output
# -----------------------------------------------------------
print(f"\nYour band's name could be: {city} {pet}.")
print("\n\n- End of Line -\n")
