# Simple Coin Toss Game
# -----------------------------------------------------------
# badDoggy | 10/23/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os
import random

# Set Variables
coin = ["Heads", "Tails"]


# Run Game
while True:
    # Clear Screen
    # -----------------------------------------------------------
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    # get random number between 0 and 1
    numb = random.randint(0, 1)

    # Title Bar
    print("    -   Coin   Toss   -")
    print("-----------------------------")

    # Input User Choice
    pick = input("Call It | H)eads or T)ails? ").lower()

    # debug
    # print(f"Pick: {pick} | Number: {numb}")

    if pick != "h" and pick != "t" and pick != "heads" and pick != "tails":
        input("\n**Invalid Input : Press any key to continue: ")
    else:
        if pick == "h" or pick == "heads":
            print(f"\n   You called {coin[0]}")
            if numb == 0:
                print(f"   It was {coin[0]}, You Win!")
            else:
                print(f"   It was {coin[1]}, Sorry You Lose!")
        elif pick == "t" or pick == "tails":
            print(f"\n   You called {coin[1]}")
            if numb == 1:
                print(f"   It was {coin[1]}, You Win!")
            else:
                print(f"   It was {coin[0]}, Sorry You Lose!")

        again = input("\n\nPlay Again? (Y/N) ").lower()
        if again != "y":
            break


print("\n- Thanks for playing -")
print("\n- End of Line -\n")
