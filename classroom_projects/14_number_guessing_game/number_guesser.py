"""
Number Guessing Game

Author: badDoggy
Date: 11/21/2026
------------------------
Three Difficulty levels:
Easy: 10 Guesses
Medium: 7 Guesses
Hard: 5 Guesses
"""

# ##########  Imports  ##############
import subprocess
import os
import random

# ############  Logo  ###############
LOGO = r"""
 _   _                 _
| \ | |               | |
|  \| |_   _ _ __ ___ | |__   ___ _ __
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|
     _____
    |  __ \
    | |  \/_   _  ___  ___ ___  ___ _ __
    | | __| | | |/ _ \/ __/ __|/ _ \ '__|
    | |_\ \ |_| |  __/\__ \__ \  __/ |
     \____/\__,_|\___||___/___/\___|_|

Can you guess my number between 1 and 100?
"""


# #########  Functions  ##############
# Clear Screen & Display Logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(LOGO)


def win_check(guess, num):
    win = ""
    text = ""
    if guess == num:
        win = True
        text = f"You Guessed it. My number is {num}"

    return win, text


def play_mode(difficult, guess):
    clear_screen()
    print(f"OK, {difficult} Mode: You get {guess} guesses.\n")


# #########  Variables  ##############
number = random.choice(range(1, 101))
game_over = False
choice = ""
difficulty = ""
guesses = 0


# Run the App
while not game_over:
    # Clear Screen & Display Logo
    clear_screen()

    # debug Code
    print(number)

    # Input for Difficulty Level
    while True:
        print("Choose difficulty level:")
        print(
            "\n  E)asy     10    Guesses\n  M)edium    7    Guesses\n  H)ard      5    Guesses\n  Q)uit\n"
        )
        choice = input("Your Choice? ").lower()
        # Quit Game
        if choice in ("q", "quit"):
            game_over = True
            break
        # Select Easy Game
        elif choice in ("e", "easy"):
            difficulty = "Easy"
            guesses = 10
            play_mode(difficulty, guesses)
            break
        # Select Medium Game
        elif choice in ("m", "medium"):
            difficulty = "Medium"
            guesses = 7
            play_mode(difficulty, guesses)
            break
        # Select Hard Game
        elif choice in ("h", "hard"):
            difficulty = "Hard"
            guesses = 5
            play_mode(difficulty, guesses)
            break
        # Invalid Input Display
        else:
            input("\nInvalid Input!!   Press any key to continue...")
            clear_screen()

    # Input for number guess
    while True:
        choice = ""
        try:
            choice = int(input("What is my number? "))
            if choice not in range(1, 101):
                print("\nInvalid Number Input!!   Must be between 1 and 100")
                input("Press any key to continue...")
                play_mode(difficulty, guesses)
            else:
                break
        except ValueError:
            print("\nInvalid Input!!   Must be a number between 1 and 100")
            input("Press any key to continue...")
            play_mode(difficulty, guesses)

    # Check user's input: Correct/Too High/Too Low

    # debug Code
    game_over = True


# End the app
print("\n\n--  End of Line --\n")
