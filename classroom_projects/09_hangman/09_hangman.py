#####################################
# Hangman
# Created by - badDoggy | 11/01/26
#####################################

# ##########  Imports  ##############
import subprocess
import os
import random
from wordlist import words
from hangman_ascii import hangman_text, stages

# ######  Global Variables  ##########
hangman_word = random.choice(words)
placeholder = ""
for x in range(len(hangman_word)):
    placeholder += "_"


while True:
    # variables for loop
    display = ""

    # Clear Screen & Set Title
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print(f"{hangman_word}\n")
    print(hangman_text)
    print(f"I'm thinking of a word: {placeholder}\n")

    # User Guess a letter
    user_choice = input("Guess a letter? (Quit to end play)  ").lower()

    if user_choice == "quit":
        break

    for letter in hangman_word:
        if letter == user_choice:
            display += letter
        else:
            display += "_"
    break

print(display)

print()
for x in range(len(stages)):
    print(stages[x])


# End the app
print("\n\n -  GAME  OVER  -")
print("\n--  End of Line --\n")
