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
     __                 _
  /\ \ \_   _ _ __ ___ | |__   ___ _ __
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /\  /| |_| | | | | | | |_) |  __/ |
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|

       ___
      / _ \_   _  ___  ___ ___  ___ _ __
     / /_\/ | | |/ _ \/ __/ __|/ _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  __/ |
    \____/ \__,_|\___||___/___/\___|_|

Can you guess my number between 1 and 100?
"""


# #########  Functions  ##############
# Clear Screen & Display Logo
def clear_screen():
    """Clear the terminal screen."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(LOGO)


def play_mode(mode, turns):
    clear_screen()

    if mode == "E":
        mode = "Easy"
    elif mode == "M":
        mode = "Medium"
    elif mode == "H":
        mode = "Hard"

    return f"OK, {mode} Mode: You get {turns} guesses.\n"


def win_check(guess, rand_num, turns_left):
    win = ""
    text = ""
    turns_left -= 1

    # if out of guesses
    if turns_left == 0:
        win = False
        text = f"\n\nYou ran out of guesses. My number is {rand_num}"
    # if guess is correct
    elif guess == rand_num:
        win = True
        text = f"\n\nYou Guessed it. My number is {rand_num}"
    # if guess too high
    elif guess > random_num:
        win = False
        text = "\nYou're too high."
    # if guess too low
    else:
        win = False
        text = "\nYou're too Low."

    return win, text, turns_left


# #########  Variables  ##############
game_over = False
choice = ""


# Run the App
while not game_over:
    # Clear Screen & Display Logo
    clear_screen()

    # user selects difficulty mode
    valid_inputs = ["E", "Easy", "M", "Medium", "H", "Hard", "Q", "Quit"]
    output = {"E": 10, "Easy": 10, "M": 7, "Medium": 7, "H": 5, "Hard": 5}

    while choice not in valid_inputs:
        # display input choices
        print("Choose difficulty level:\n")
        print("  E)asy    (10 Guesses)")
        print("  M)edium   (7 Guesses)")
        print("  H)ard     (5 Guesses)")
        print("  Q)uit Game\n")

        # input user choice
        choice = input("Your choice? ").capitalize()

        # user chooses quit game
        if choice in ("Q", "Quit"):
            game_over = True
            break

        # invalid inputs
        elif choice not in valid_inputs:
            input("\nInvalid Choice!!  press any key to continue ...")
            clear_screen()

    # Input for number guess
    if choice not in ("Q", "Quit"):
        print(play_mode(choice, output[choice]))
        random_num = random.choice(range(1, 101))
        rounds = output[choice]

        while rounds > 0:
            clear_screen()
            print(play_mode(choice, output[choice]))

            # DEBUG CODE ############################################
            print(f"Random Number: {random_num}\n")
            # DEBUG CODE ############################################

            number_guess = input("Q)uit, or Guess my number? ").capitalize()
            if number_guess in ("Q", "Quit"):
                game_over = True
                choice = "Q"
                break
            else:
                try:
                    this_guess = int(number_guess)
                    if this_guess not in range(1, 101):
                        print("\nInvalid Number Input!!   Must be between 1 and 100")
                        input("Press any key to continue...")
                    else:
                        # Check user's input: Correct/Too High/Too Low
                        win_game, win_text, rounds = win_check(
                            this_guess, random_num, rounds
                        )
                        if win_game:
                            print(win_text)
                            game_over = True
                            rounds = 0
                        else:
                            if rounds == 0:
                                print(win_text)
                                game_over = True
                            else:
                                print(win_text)
                                if rounds > 1:
                                    print(f"You have {rounds} guesses left...")
                                else:
                                    print(f"You have {rounds} guess left...")
                                input("\npress any key to continue...")

                except ValueError:
                    print("\nInvalid Input!!   Must be a number between 1 and 100")
                    input("Press any key to continue...")

    # Play Again Prompt
    if game_over and choice not in ("Q", "Quit"):
        again = input("\n\nPlay Again>  (Y/N) ").strip().lower()
        if again in ("y", "yes"):
            # Reset Variables and Deal the first 2 cards
            game_over = False
            choice = ""
        else:
            break


# End the app
print("\n\n--  End of Line --\n")
