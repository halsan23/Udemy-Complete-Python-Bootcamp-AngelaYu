######################################
# Rock - Paper - Scissors
# Created by - badDoggy | 09/15/26
# Updated by badDoggy | 10/23/26
######################################

#  Imports  ##########################
import subprocess
import os
import random

#  Set Initial Variables  ############
# set computer choice options
computer_choices = ["Rock", "Paper", "Scissors"]
# set to 3 for game best 3 out of 5
win_score = 3


#  Functions  ########################
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
    if user == comp:
        winner = None
        win_text = "This round is a tie:"
        return winner, win_text

    # user win scenarios
    elif user == "rock" and comp == "scissors":
        winner = "user"
        win_text = "You win this round: - Rock smashes Scissors"
        return winner, win_text
    elif user == "paper" and comp == "rock":
        winner = "user"
        win_text = "You win this round: - Paper covers Rock"
        return winner, win_text
    elif user == "scissors" and comp == "paper":
        winner = "user"
        win_text = "You win this round: - Scissors cut Paper"
        return winner, win_text

    # computer win scenarios
    elif comp == "rock" and user == "scissors":
        winner = "computer"
        win_text = "Computer wins this round: - Rock smashes Scissors"
        return winner, win_text
    elif comp == "paper" and user == "rock":
        winner = "computer"
        win_text = "Computer wins this round: - Paper covers Rock"
        return winner, win_text
    else:
        comp == "scissors" and user == "paper"
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
    user = input("Enter Rock, Paper, Scissors or (Q)uit to end the game: ").capitalize()

    # option for user to end game early
    if user.lower() == "Q" or user.lower() == "Quit":
        print("\n- User Quit -")
        break

    # invalid input check
    elif (
        user.lower() != "rock"
        and user.lower() != "paper"
        and user.lower() != "scissors"
    ):
        print("\n- Invalid Input -\n")
        # Pause play so reader can see the error info
        input("- Press any key to continue -")

    else:
        # Display computer pick
        # rand_num = randint(0, 2)
        # comp = computer_choices[rand_num]
        comp = random.choices(computer_choices)
        print(f"Computer Choice: - {comp} -\n")

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
            if again.lower() == "y":
                # set initial variables
                user_score, comp_score, tie_score, turn = reset()
            else:
                break

######################################
print("\nThanks for playing ...")
print("\n\n-- End of Line --\n")
