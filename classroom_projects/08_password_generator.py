######################################
# Password Generator
# Created by - badDoggy | 09/26/26
######################################


# ###########  Imports  ##############
import subprocess
import os
import random


# ##########  Functions  #############
def yn_check(text):
    while True:
        select = input(f"{text}  (Y/N) ").lower()
        if select == "y" or select == "yes" or select == "n" or select == "no":
            return select
        else:
            print("Invalid Input - (Y/N) only!\n")


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
temp_pswd = []
final_pswd = []
tmp_pswd = ""
password = ""

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
tmp_pswd = "".join(temp_pswd)

print(f"\ntemp password: {tmp_pswd}")

while temp_pswd:
    final_pswd.append(temp_pswd.pop(random.randrange(len(temp_pswd))))

password = "".join(final_pswd)
print(f"Final Password: {password}")


print("\n\n--  End of Line --\n")
