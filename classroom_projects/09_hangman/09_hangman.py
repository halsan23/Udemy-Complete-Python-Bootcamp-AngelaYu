#####################################
# Hangman
# Created by - badDoggy | 11/01/26
#####################################

# ##########  Imports  ##############
import subprocess
import os
import random
from hangman_ascii import hangman_text, stages, words


# #########  Functions  ##############
def reset():
    hangman_word = random.choice(words)
    correct_letters = []
    lives = 7
    user_choice = ""
    input_error = ""

    placeholder = ""
    for x in range(len(hangman_word)):
        placeholder += "_"

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

    return (
        hangman_word,
        correct_letters,
        lives,
        user_choice,
        input_error,
        placeholder,
        letters,
    )


def play_again():
    again = input("Would you like yo play again?  (Y/N) ").lower()
    if again == "y":
        return True
    else:
        return False


# ######  Global Variables  ###########
end_game = True


# ##########  Run the game  ##########
while True:
    if end_game:
        end_game = False
        # get variables
        (
            hangman_word,
            correct_letters,
            lives,
            user_choice,
            input_error,
            placeholder,
            letters,
        ) = reset()
    # Clear Screen & Set Title
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    # Print Hangman logo
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
        print(f'\nSorry, You Lose!\nThe word was: "{hangman_word}"\n')
        again = play_again()
        if again:
            end_game = True
        else:
            print()
            break

    elif "_" not in current_text:
        print("\n -  You  Win!!  -\n")
        again = play_again()
        if again:
            end_game = True
        else:
            print()
            break

    if not end_game:
        # User Guess a letter
        print(f"Available letters: {"".join(letters)}\n{input_error}\n")

        user_choice = input("Guess a letter? (Quit to end play)  ").lower()

        if user_choice == "quit":
            break

        if user_choice.upper() in letters:
            input_error = ""

            for x in range(len(letters)):
                if letters[x] == user_choice.upper():
                    letters[x] = "_"

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
print(" -  GAME  OVER  -")
print("\n--  End of Line --\n")
