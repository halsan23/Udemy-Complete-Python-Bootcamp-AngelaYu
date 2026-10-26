######################################
# Password Generator
# Created by - badDoggy | 09/26/26
######################################


# ###########  Imports  ##############
import subprocess
import os


# ##########  Functions  #############
def yn_check(text):
    while True:
        select = input(f"{text}  (Y/N) ").lower()
        if select == "y" or select == "yes" or select == "n" or select == "no":
            return select
        else:
            print("Invalid Input - (Y/N) only!")


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

# Clear Screen
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# ###########  Title Bar  ############
print("pyPassword Generator")
print("---------------------------------------------------")


# ############  Inputs  ##############
# Password Length
# ------------------------------------
while True:
    try:
        pswd_length = int(input("Enter an integer between 8 and 20: "))
        if 8 <= pswd_length <= 20:
            break
        else:
            print("Input Error! Must be within range (8-20)")
    except ValueError:
        print("Input Error! Must be a number (8-20)")

# Use Uppercase Letters
# ------------------------------------
up_case = yn_check("Use Upper Case Letters?")

# Use Numbers
# ------------------------------------
numbs = yn_check("Use Numbers?")

# Use Special Characters
# ------------------------------------
spec_char = yn_check("Use Special Characters??")
# spec_char = input("Use Special Characters?  (Y/N) 8").lower()

# Calculate number of characters from each option for even distribution
# ---------------------------------------------------------------------
total_choices = 0
if up_case == "y" or up_case == "Y":
    total_choices += 1
if numbs == "y" or up_case == "Y":
    total_choices += 1
if spec_char == "y" or up_case == "Y":
    total_choices += 1

if pswd_length % total_choices == 0:
    lower_case = int(pswd_length / total_choices)
    each_opt = int(pswd_length / total_choices) - lower_case
else:
    lower_case = int(pswd_length / total_choices) + int((pswd_length % total_choices))
    each_opt = int(pswd_length / total_choices) - lower_case


# ########  Build Password  ##########


# debug code
# ------------------------------------
print(f"\nNumber of Characters: {pswd_length}")
print(f"Use Upper Case? {up_case.upper()}")
print(f"Use Numbers? {numbs.upper()}")
print(f"Use Special Characters? {spec_char.upper()}")
print(f"\nTotal Options Chosen: {total_choices}")
print(f"# of lower case: {lower_case}")
print(f"# in each of other options: {each_opt}")
print(f"\nTotal Characters Used: {lower_case + (each_opt * total_choices)}")
