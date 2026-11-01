######################################
# Hangman
# Created by - badDoggy | 11/01/26
######################################


# ###########  Imports  ##############
import subprocess
import os
import random
from wordlist import words

# ######  Global Variables  ##########
hangman_word = random.choice(words)


# Clear Screen & Set Title
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print("****************************************")
print("*       - -   H A N G M A N   - -      *")
print("* ------------------------------------ *")
print("*   can you save me from the gallows   *")
print("****************************************\n")


# ##########  User Guess  ############
print("I'm thinking of a word..")

while True:
    # variables for loop
    match = False
    user_choice = input("Guess a letter? (Quit to end play)").lower()

    if user_choice == "quit":
        break

    for letter in hangman_word:
        if letter == user_choice:
            match = True
            break

    if match:
        print(f"Yes, there is an {user_choice} in {hangman_word}.\n")
    else:
        print(f"There is no {user_choice} in {hangman_word}.\n")


# Debug Code
# print(f"\nThe Word is: {hangman_word}")
# print(user_choice)


# End the app
print("\n\n--  End of Line --\n")
