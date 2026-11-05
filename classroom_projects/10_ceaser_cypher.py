#####################################
# Caesar Cypher
# Created by - badDoggy | 11/xx/26
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


# Run the app
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


# Output
print(f"\nYour encrypted message: {encrypt(text, shift)}")


# ##########  End the app  ##########
print("\n\n--  End of Line --\n")
