#####################################
# Hangman
# Created by - badDoggy | 11/01/26
#####################################


# ##########  Imports  ##############
import subprocess
import os
import random
from wordlist import words, letters
from hangman_ascii import hangman_text, stages


# #########  Functions  #############
# Play Again
def again(text):
    print(text)
    again = input("Play Again?  (Y/N)  ").lower()
    if again != "y" and again != "yes":
        print()
        return False
    else:
        return True


# set default values
def reset():
    # ######  Global Variables  ##########
    hangman_word = random.choice(words)  # random word from list
    used_letters = letters  # which letters have been used
    correct_letters = []  # correctly guessed letters for output display
    lives = 7
    user_choice = ""  # user selected letter
    input_error = ""  # misc error messages
    end_text = ""  # win/lose display

    placeholder = ""  # empty set of line before any letters filled in
    for x in range(len(hangman_word)):
        placeholder += "_"

    return (
        hangman_word,
        used_letters,
        correct_letters,
        lives,
        user_choice,
        input_error,
        end_text,
        placeholder,
    )


# #########  Variables  #############
lives = 0

# ##########  Run the game  ##########
while True:
    if lives == 0:
        (
            hangman_word,
            used_letters,
            correct_letters,
            lives,
            user_choice,
            input_error,
            end_text,
            placeholder,
        ) = reset()

    # print(f"hangman_word: {hangman_word}")
    # print(f"used_letters: {used_letters}")
    # print(f"correct_letters: {correct_letters}")
    # print(f"lives: {lives}")
    # print(f"user_choice: {user_choice}")
    # print(f"input_error: {input_error}")
    # print(f"end_text: {end_text}")
    # print(f"hangman_word: {placeholder}")
    # break

    # Clear Screen & Set Title
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    # Hangman logo display
    print(hangman_text)

    # Debug Code - shows current hangman word
    print(f"{hangman_word}\n")

    # shows either empty lines or combo of lines and correctly chosen letters
    if not correct_letters:
        current_text = placeholder
    else:
        current_text = display

    if end_text != "":
        print(end_text)

    # user chosen letters display - initially empty lines
    print(f"I'm thinking of a word: {current_text}")
    print(stages[lives])

    # Display a list of available letters
    print(f"Available letters: {"".join(used_letters)}\n{input_error}\n")
    # User Guess a letter
    user_choice = input("Guess a letter? (Quit to end play)  ").lower()

    # option to quit the game before finishing
    if user_choice == "quit":
        break

    # check for valid user input
    # can only pick letters from the "available" list (used_letters)
    if user_choice.upper() in used_letters:
        input_error = ""

        # if user chosen letter is a valid letter that has not been used yet,
        # replace the letter in the 'used_letters' list with a "_" line
        for x in range(len(used_letters)):
            if used_letters[x] == user_choice.upper():
                used_letters[x] = "_"

        # sets the display for the word the user is trying to solve
        # this is displayed above at line 37
        display = ""

        for letter in hangman_word:
            if letter == user_choice:
                display += letter
                correct_letters.append(user_choice)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        # if the user selected letter is not in the 'hangman word'
        # lose a life
        if user_choice not in hangman_word:
            lives -= 1

        # check for end game status
        if lives == 0:
            end_text = f'\nSorry, You Lose!\nThe word was: "{hangman_word}"\n'
            if again(end_text):
                lives = 0
            else:
                break
        elif "_" not in current_text:
            end_text = "\n -  You  Win!!  -\n"
            if again(end_text):
                lives = 0
            else:
                break

    # set error message if user tries invalid input or
    # a letter that has already been used
    else:
        input_error = "ERROR! Use only available letters"


# End the app
if user_choice == "quit":
    print("\n -  User  Quit  -")
print(" -  GAME  OVER  -")
print("\n--  End of Line --\n")
