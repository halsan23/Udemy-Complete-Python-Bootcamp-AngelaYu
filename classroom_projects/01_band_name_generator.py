# Simple Band Name Generator that shows
# how to combine inputs for a single output
# -----------------------------------------------------------
# badDoggy | 10/18/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os

# Clear Screen
# -----------------------------------------------------------
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Title & Description
# -----------------------------------------------------------
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
