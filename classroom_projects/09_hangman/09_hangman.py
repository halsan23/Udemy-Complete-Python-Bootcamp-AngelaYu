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

# Run the game
correct_letters = []
game_over = False
while not game_over:

    # Clear Screen & Set Title
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print(f"{hangman_word}\n")
    print(hangman_text)

    if not correct_letters:
        current_text = placeholder
    else:
        current_text = display

    print(f"I'm thinking of a word: {current_text}\n")

    if "_" not in current_text:
        print("You Win!!")
        break

    # User Guess a letter
    user_choice = input("Guess a letter? (Quit to end play)  ").lower()

    display = ""

    if user_choice == "quit":
        break

    for letter in hangman_word:
        if letter == user_choice:
            display += letter
            correct_letters.append(user_choice)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Display = {display}")


# End the app
print("\n\n -  GAME  OVER  -")
print("\n--  End of Line --\n")
