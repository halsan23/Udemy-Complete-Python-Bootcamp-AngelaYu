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
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
used_letters = letters
correct_letters = []
lives = 7
user_choice = ""
input_error = ""

placeholder = ""
for x in range(len(hangman_word)):
    placeholder += "_"


# ##########  Run the game  ##########
while True:
    # Clear Screen & Set Title
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(hangman_text)

    # Debug Code
    # print(f"{hangman_word}\n")

    if not correct_letters:
        current_text = placeholder
    else:
        current_text = display

    print(f"I'm thinking of a word: {current_text}")
    print(stages[lives])

    if lives == 0:
        end_text = f'Sorry, You Lose!\nThe word was: "{hangman_word}"\n'
        break
    elif "_" not in current_text:
        end_text = " -  You  Win!!  -"
        break

    # User Guess a letter
    print(f"Available letters: {"".join(used_letters)}\n{input_error}\n")

    user_choice = input("Guess a letter? (Quit to end play)  ").lower()

    if user_choice == "quit":
        break

    if user_choice.upper() in used_letters:
        input_error = ""

        for x in range(len(used_letters)):
            if used_letters[x] == user_choice.upper():
                used_letters[x] = "_"

        display = ""

        for letter in hangman_word:
            if letter == user_choice:
                display += letter
                correct_letters.append(user_choice)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        if user_choice not in hangman_word:
            lives -= 1

    else:
        input_error = "ERROR! Use only available letters"


# End the app
if user_choice == "quit":
    print("\n -  User  Quit  -")
else:
    print(end_text)
print(" -  GAME  OVER  -")
print("\n--  End of Line --\n")
