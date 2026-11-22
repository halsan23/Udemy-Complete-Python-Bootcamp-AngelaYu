"""
Number Guessing Game

Author: badDoggy
Date: 11/22/2026
------------------------
Three Difficulty levels:
Easy:  10 Guesses
Medium: 7 Guesses
Hard:   5 Guesses
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
    """Clear the terminal screen and display the game logo."""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(LOGO)


def play_mode(mode, turns):
    """
    Used for feedback to user.
    \nClears the screen.
    \nDisplays game Mode and number of initial guesses the user is allowed.
    """
    clear_screen()

    if mode in ("e", "easy"):
        mode_display = "Easy"
    elif mode in ("m", "medium"):
        mode_display = "Medium"
    elif mode in ("h", "hard"):
        mode_display = "Hard"
    else:
        mode_display = mode

    return f"OK, {mode_display} Mode: You get {turns} guesses.\n"


def win_check(guess, rand_num, turns_left, user_choice, guesses):
    """
    Determines game status.
    \n  Is user guess too high or too low.
    \n  Is user out of turns (guesses).
    \n  Is user guess correct.
    """
    clear_screen()
    print(play_mode(user_choice, guesses))

    win = False
    turns_left -= 1

    # if out of guesses
    if turns_left == 0:
        text = f"\nYou ran out of guesses. My number is {rand_num}"
    # if guess is correct
    elif guess == rand_num:
        win = True
        text = f"\nYou Guessed it. My number is {rand_num}"
    # if guess too high
    elif guess > rand_num:
        text = f" {guess} is too high."
    # if guess too low
    else:
        text = f" {guess} is too low."

    return win, text, turns_left


# #########  Variables  ##############
game_over = False
choice = ""


# Run the App
while not game_over:
    # Clear Screen & Display Logo
    clear_screen()

    # user selects difficulty mode
    valid_inputs = ["e", "easy", "m", "medium", "h", "hard", "q", "quit"]
    output = {"e": 10, "easy": 10, "m": 7, "medium": 7, "h": 5, "hard": 5}

    # input user choice for difficulty mode
    while choice not in valid_inputs:
        # display input choices
        print("Choose difficulty level:\n")
        print("  E)asy    (10 Guesses)")
        print("  M)edium   (7 Guesses)")
        print("  H)ard     (5 Guesses)")
        print("  Q)uit Game\n")

        # normalize input to lowercase and strip whitespace
        choice = input("Your choice? ").strip().lower()

        # user chooses quit game
        if choice in ("q", "quit"):
            game_over = True

        # invalid inputs
        elif choice not in valid_inputs:
            input("\nInvalid Choice!!  press any key to continue ...")
            clear_screen()

    # after user has selected game difficulty, user guesses number
    if choice not in ("q", "quit"):
        # display for user reference
        print(play_mode(choice, output[choice]))
        # pick random number for user to guess
        random_num = random.randint(1, 100)
        # set variable to track how many rounds user has left
        rounds = output[choice]

        # this loop will accept a user guess if they have any round guesses left
        while rounds > 0:
            # clear the screen and display user mode select and number of guesses they get
            clear_screen()
            print(play_mode(choice, output[choice]))

            # DEBUG CODE ############################################
            # print(f"Random Number: {random_num}\n")
            # DEBUG CODE ############################################

            # input for user to guess the number
            number_guess = input("Q)uit, or Guess my number? ").strip().lower()

            # if user ends game
            if number_guess in ("q", "quit"):
                game_over = True
                rounds = 0
                choice = "q"
            # check for proper input
            else:
                try:
                    this_guess = int(number_guess)
                    # if this_guess is an integer, but out of range(1, 101)
                    if this_guess not in range(1, 101):
                        print("\nInvalid Number Input!!   Must be between 1 and 100")
                        input("Press any key to continue...")
                    # Check user's input
                    else:
                        win_game, win_text, rounds = win_check(
                            this_guess, random_num, rounds, choice, output[choice]
                        )
                        # user guess is correct
                        if win_game:
                            print(win_text)
                            game_over = True
                            rounds = 0
                        else:
                            # if user out of guesses
                            if rounds == 0:
                                print(win_text)
                                game_over = True
                            # user guess is too high or too low
                            else:
                                print(win_text)
                                if rounds == 1:
                                    print(f" You have {rounds} guess left...")
                                else:
                                    print(f" You have {rounds} guesses left...")
                                input("\npress any key to continue...")
                # if this_guess is not an integer
                except ValueError:
                    print("\nInvalid Input!!   Must be a number between 1 and 100")
                    input("Press any key to continue...")

    # Play Again Prompt
    if game_over and choice not in ("q", "quit"):
        again = input("\n\nPlay Again>  (Y/N) ").strip().lower()
        # Reset variables to restart the game
        if again in ("y", "yes"):
            game_over = False
            choice = ""
        # end game
        else:
            break


# End the app
print("\n\n--  End of Line --\n")
