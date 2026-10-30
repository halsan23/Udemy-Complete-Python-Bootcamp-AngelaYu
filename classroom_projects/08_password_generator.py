######################################
# Password Generator
# Created by - badDoggy | 10/30/26
######################################


# Imports
import subprocess
import os
import random

# Variables
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# Functions
def yn_check(text):
    while True:
        select = input(f"{text}  (Y/N) ").lower()
        if select == "":
            select = "y"
        if select == "y" or select == "yes" or select == "n" or select == "no":
            return select
        else:
            print("Invalid Input - (Y/N) only!\n")


# Title Bar
print("pyPassword Generator")
print("---------------------------------------------------\n")


# Run the Generator
while True:
    # Clear Screen
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    # Variables
    initial_password = ""
    password = ""

    # Password Length Input
    while True:
        try:
            password_length = int(
                input("How many Characters for your password? (8-20) ")
            )
            if 8 <= password_length <= 20:
                break
            else:
                print("\nInput Error! Must be within range (8-20)")
        except ValueError:
            print("\nInput Error! Must be a number (8-20)")

    # Use Uppercase Letters
    up_case = yn_check("\nUse Upper Case Letters?")

    # Use Numbers
    numbs = yn_check("Use Numbers?")

    # Use Special Characters
    spec_char = yn_check("Use Special Characters??")

    # Build the  initial password
    x = 1
    while x <= password_length:
        initial_password += random.choice(letters)
        x += 1
        if x > password_length:
            break
        if up_case == "y" or up_case == "yes":
            initial_password += random.choice(letters).upper()
            x += 1
            if x > password_length:
                break
        if numbs == "y" or numbs == "yes":
            initial_password += random.choice(numbers)
            x += 1
            if x > password_length:
                break
        if spec_char == "y" or spec_char == "yes":
            initial_password += random.choice(symbols)
            x += 1
            if x > password_length:
                break

    # Randomize the password
    password = "".join(random.sample(initial_password, len(initial_password)))

    # output the results
    print(f"\nYour new password is: {password}")

    # Confirm User likes new password
    again = yn_check("\nKeep this password?")
    if again == "" or again == "y" or again == "yes":
        break


# End the app
print("\n\n--  End of Line --\n")
