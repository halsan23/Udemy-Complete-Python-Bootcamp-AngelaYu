#####################################
# Hangman
# Created by - badDoggy | 11/04/26
#####################################

# ##########  Imports  ##############
import subprocess
import os
import random
from hangman_ascii import hangman_text, stages, words


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


# Reset Variables
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


def play_again(text):
    print(text)
    again = input("Would you like to play again?  (Y/N) ").lower()
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
    clear_screen()
    # Print Hangman logo
    print(hangman_text)

    # Debug Code
    # print(f"{hangman_word}\n")

    if not correct_letters:
        current_text = placeholder
    else:
        current_text = display

    print(f"To save me, show them the secret word: {current_text}")
    print(stages[lives])

    if lives == 0:
        end_game = play_again(f'\nSorry, You Lose!\nThe word was: "{hangman_word}"\n')
        if not end_game:
            print()
            break

    elif "_" not in current_text:
        end_game = play_again(f' -  You  Win!!  -\nThe word was: "{hangman_word}"\n')
        if not end_game:
            print()
            break

    if not end_game:
        # User Guess a letter
        print(f"Available letters: {''.join(letters)}\n{input_error}\n")

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

            if user_choice.lower() not in hangman_word.lower():
                lives -= 1

        else:
            input_error = (
                "ERROR! Please enter a single unused letter from the list above."
            )


# ##########  End the app  ##########
print("\n\n--  End of Line --\n")
