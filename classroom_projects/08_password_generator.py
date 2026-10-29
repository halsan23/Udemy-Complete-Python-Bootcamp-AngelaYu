######################################
# Password Generator
# Created by - badDoggy | 10/29/26
######################################


# ###########  Imports  ##############
import subprocess
import os
import random

# ###########  Variables  ############
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
end = 0


# ##########  Functions  #############
def yn_check(text):
    while True:
        select = input(f"{text}  (Y/N) ").lower()
        if select == "":
            select = "y"
        if select == "y" or select == "yes" or select == "n" or select == "no":
            return select
        else:
            print("Invalid Input - (Y/N) only!\n")


# ###########  Title Bar  ############
print("pyPassword Generator")
print("---------------------------------------------------\n")


# ############  Inputs  ##############
# ------------------------------------
while True:
    # Clear Screen
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    # ###########  Variables  ############
    temp_pswd = []
    finished_pswd = []
    password = ""

    # Password Length
    # ------------------------------------
    while end == 0:
        try:
            pswd_length = int(input("How many Characters for your password? (8-20) "))
            if 8 <= pswd_length <= 20:
                break
            else:
                print("\nInput Error! Must be within range (8-20)")
        except ValueError:
            print("\nInput Error! Must be a number (8-20)")

    # Use Uppercase Letters
    # ------------------------------------
    up_case = yn_check("\nUse Upper Case Letters?")

    # Use Numbers
    # ------------------------------------
    numbs = yn_check("\nUse Numbers?")

    # Use Special Characters
    # ------------------------------------
    spec_char = yn_check("\nUse Special Characters??")

    # ######  Build the Password  ########
    # ------------------------------------
    # build original password LIST based
    # on the options selected
    # ------------------------------------
    while end == 0:
        x = 1
        while x <= pswd_length:
            temp_pswd.append(random.choice(letters))
            x += 1
            if x > pswd_length:
                break
            if up_case == "y" or up_case == "yes":
                temp_pswd.append(random.choice(letters).upper())
                x += 1
                if x > pswd_length:
                    break
            if numbs == "y" or numbs == "yes":
                temp_pswd.append(random.choice(numbers))
                x += 1
                if x > pswd_length:
                    break
            if spec_char == "y" or spec_char == "yes":
                temp_pswd.append(random.choice(symbols))
                x += 1
                if x > pswd_length:
                    break

    # build the finished password LIST
    # ------------------------------------
    while temp_pswd:
        finished_pswd.append(temp_pswd.pop(random.randrange(len(temp_pswd))))

    # convert the password LIST to a STRING
    # ------------------------------------
    password = "".join(finished_pswd)

    # output the results
    # ------------------------------------
    print(f"\nYour new password is: {password}")

    # ## Confirm User likers new password #
    # ------------------------------------
    again = yn_check("\nKeep this password?")
    if again == "" or again == "y" or again == "yes":
        break


print("\n\n--  End of Line --\n")
