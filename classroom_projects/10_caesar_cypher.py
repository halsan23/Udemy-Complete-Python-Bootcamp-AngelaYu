#####################################
# Caesar Cypher
# Created by - badDoggy | 11/06/26
#####################################

# ##########  Imports  ##############
import subprocess
import os

# #########  Variables  #############
alphabet = [
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
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP""  ""  `"Y8ba,   ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88

           ##             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""  ""  88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
end_app = False


# #########  Functions  ##############
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            cipher_text += alphabet[
                (alphabet.index(letter) + shift_amount) % len(alphabet)
            ]
        else:
            cipher_text += " "

    return cipher_text


def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            cipher_text += alphabet[
                (alphabet.index(letter) - shift_amount) % len(alphabet)
            ]
        else:
            cipher_text += " "

    return cipher_text


# Run the app
while True:
    # for run app again loop
    if end_app:
        break

    # local variable
    good_input = False

    # Clear Screen & display the logo
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print(logo)

    # Encrypt or Decrypt Input
    while not good_input:
        direction = input(
            "   E)ncode to encrypt \n   D)ecode to decrypt\n   Q)uit\n\nPlease choose: "
        ).lower()

        if direction == "q" or direction == "quit":
            end_app = True
            good_input = True
            break
        elif direction == "e":
            process = "encrypt"
            break
        elif direction == "d":
            process = "decrypt"
            break
        else:
            print("\nInvalid Input!! | Choose from available options only!\n")
            break

    # Shift Amount Input
    while not good_input:
        try:
            shift = int(input("Type the shift number: (1 to 26) "))
            if shift < 1 or shift > 26:
                print("\nInvalid Input!! | Choose a valid number: (1 to 26)!\n")
            else:
                break
        except:
            print("\nInvalid Input!! | Choose a valid number: (1 to 26)!\n")

    # Message to Encrypt or Decrypt Input
    while not good_input:
        text = input(f"\nEnter the message to {process}: ").lower()
        for letter in text:
            if letter not in alphabet and letter != " ":
                print(
                    "\nInvalid Input!! | Choose a valid letter (A to Z) or a space only!\n"
                )
                break
        break

    # routing for either encrypt or decrypt
    if not good_input:
        # Encrypt
        if direction == "e" or direction == "encode":
            print(f"\nYour encrypted message is: {encrypt(text, shift)}")
        # Decrypt
        elif direction == "d" or direction == "decode":
            print(f"\nYour decrypted message is: {decrypt(text, shift)}")

    # run app again?
    while not end_app:
        again = input("\nRun Again?  (Y/N) ").lower()
        if again == "n":
            end_app = True
        break


# ##########  End the app  ##########
print("\n\n--  End of Line --\n")
