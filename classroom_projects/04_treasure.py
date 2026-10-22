# Simple text based Treasure Hunt Game
# -----------------------------------------------------------
# badDoggy | 10/21/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os

# Clear Screen
# -----------------------------------------------------------
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# set win_lose variable
# -----------------------------------------------------------
win_lose = "-- You Lose --"


# supplied text graphic
# -----------------------------------------------------------
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


# Play the Game
# -----------------------------------------------------------
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("-------------------------------------")

print("\nYou stand at a fork in thew road.")
move = input("Do you want to veer L)eft or R)ight? ").lower()
if move == "r":
    print("\nARRGH!! You've fallen to your doom into an endless chasm!")
else:
    print("\nYou come to a lake.")
    move = input("Do you want to G)o around or S)wim across? ").lower()
    if move == "s":
        print("\nARRGH!! You've been eaten by a demon trout!!")
    else:
        print("\nYou come to a house with three doors.")
        move = input(
            "Do you want to enter the R)ed door, the B)lue door, or the Y)ellow door? "
        ).lower()
        if move == "y":
            print("\n** You Found the Treasure **")
            win_lose = "** You Win **"
        elif move == "r":
            print("\nARRGH!! The room exploded and you burned to death!!")
        else:
            print("\nARRGH!! You we're eaten by a room full of carnivorous beasts!!")

print("\n-------------------------------------")
print(f"\n{win_lose}")
print("-- Game Over --")
print("\n- End of Line -")
