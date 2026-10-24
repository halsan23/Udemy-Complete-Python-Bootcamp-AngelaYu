######################################
# Rock - Paper - Scissors
# Created by - badDoggy | 09/15/26
# Updated by badDoggy | 10/24/26
######################################


# ############ Imports  ##############
import subprocess
import os
import random

# ####### Set Initial Variables  #####
# set computer choice options
computer_choices = ["Rock", "Paper", "Scissors"]
# set to 3 for game best 3 out of 5
win_score = 3


# ########## Functions  ##############
# Images
def images(choice):
    if choice.lower() == "rock":
        img = """    _______
---' ______)
    (______)
    (______)
    (______)
---.__(____)
        """
    elif choice.lower() == "paper":
        img = """    _______
---'   ____)______
        __________)
        __________)
        __________)
---.______________)
        """
    else:
        img = """    ______
---'   ___)_______
        __________)
    ______________)
    (________)
---.__(_____)
        """

    return img


# Initial Setup
def reset():
    # set variables
    user_score = 0
    comp_score = 0
    tie_score = 0
    turn = 1
    return user_score, comp_score, tie_score, turn


# function for Title Bar
def title_bar():
    print(
        f" User Score: {user_score} | Computer Score: {comp_score} | Tie Games: {tie_score}\n"
    )
    print(" *****************************")
    print(" *  Rock - Paper - Scissors  *")
    print(" *    Player vs. Computer    *")
    print(" *      Best 3 out of 5      *")
    print(" *****************************\n")


# function to test for win
def win_check(user, comp):
    # if a tie
    if user == comp.lower():
        winner = None
        win_text = "This round is a tie:"
        return winner, win_text

    # user win scenarios
    elif user == "rock" and comp == "Scissors":
        winner = "user"
        win_text = "You win this round: - Rock smashes Scissors"
    elif user == "paper" and comp == "Rock":
        winner = "user"
        win_text = "You win this round: - Paper covers Rock"
    elif user == "scissors" and comp == "Paper":
        winner = "user"
        win_text = "You win this round: - Scissors cut Paper"

    # computer win scenarios
    elif comp == "Rock" and user == "scissors":
        winner = "computer"
        win_text = "Computer wins this round: - Rock smashes Scissors"
    elif comp == "Paper" and user == "rock":
        winner = "computer"
        win_text = "Computer wins this round: - Paper covers Rock"
    else:
        comp == "Scissors" and user == "paper"
        winner = "computer"
        win_text = "Computer wins this round: - Scissors cut Paper"

    return winner, win_text


# reset initial variables
user_score, comp_score, tie_score, turn = reset()


# Play the Game
while True:
    # Clear Screen
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    # Display Title Bar
    title_bar()

    # User Input
    user = input("Enter R)ock, P)aper, S)cissors or (Q)uit to end the game: ").lower()

    # option for user to end game early
    if user == "q" or user == "quit":
        print("\n- User Quit -")
        break

    # invalid input check
    elif (
        (user != "r" and user != "rock")
        and (user != "p" and user != "paper")
        and (user != "s" and user != "scissors")
    ):
        print("\n- Invalid Input -\n")
        # Pause play so reader can see the error info
        input("- Press any key to continue -")

    else:
        # if user enters single letter input
        # convert into a word
        if user == "r":
            user = "rock"
        elif user == "p":
            user = "paper"
        elif user == "s":
            user = "scissors"

        # Display user choice
        print(f"\nYou Chose: - {user.capitalize()} -")
        print(images(user))

        # Computer selection
        comp = random.choice(computer_choices)

        # Display computer choice
        print(f"Computer Chooses: {comp}\n")
        print(images(comp))

        # No Input Errors - Check for win
        winner, win_text = win_check(user, comp)
        print(win_text)

        # Update Scores and round
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            comp_score += 1
        else:
            tie_score += 1
        turn += 1

        # Pause play so reader can see the results of this round
        input("\n- Press any key to continue -")

        # Game Over
        if user_score == win_score or comp_score == win_score:
            # Clear Screen
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

            # Display Title Bar
            title_bar()

            # Display the results of the game
            if user_score > comp_score:
                print(
                    f"You Won, {user_score} games to {comp_score}, in {turn - 1} rounds :)"
                )
            else:
                print(
                    f"The computer wins, {comp_score} games to {user_score}, in {turn - 1} rounds :("
                )

            # Ask to Play Again
            again = input("\nPlay Again? (Y/N) ")
            if again.lower() == "y" or again.lower() == "yes":
                # set initial variables
                user_score, comp_score, tie_score, turn = reset()
            else:
                break


# ########## Game Over  ##############
print("\nThanks for playing ...")
print("\n\n-- End of Line --\n")
