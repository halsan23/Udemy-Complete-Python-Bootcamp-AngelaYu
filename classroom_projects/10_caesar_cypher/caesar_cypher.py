#####################################
# Caesar Cypher
# Created by - badDoggy | 11/07/26
#####################################

# ##########  Imports  ##############
import os
import subprocess
from data import alphabet, logo


# #########  Functions  ##############
# Clear Screen & display the logo
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


def cypher(original_text, shift_amount, cypher_type):
    cipher_text = ""
    for letter in original_text:
        # if the letter is alphabetic
        if letter in alphabet:
            if cypher_type == "encode":
                cipher_text += alphabet[
                    (alphabet.index(letter) + shift_amount) % len(alphabet)
                ]
            else:
                cipher_text += alphabet[
                    (alphabet.index(letter) - shift_amount) % len(alphabet)
                ]
        # if the letter is non-alphabetic
        else:
            cipher_text += letter

    return cipher_text


# #########  Variables  #############
end_app = False


# Run the app
while True:
    # run app again loop
    if end_app:
        break

    # local variable
    good_input = False

    clear_screen()

    # Encrypt or Decrypt Input
    while not good_input:
        direction = input(
            "Would you like to:\n\n   E)ncode\n   D)ecode\n   Q)uit\n\nPlease choose: "
        ).lower()

        if direction == "q" or direction == "quit":
            end_app = True
            good_input = True
            break
        elif direction == "e":
            process = "encode"
            break
        elif direction == "d":
            process = "decode"
            break
        else:
            clear_screen()
            print("\nInvalid Input!! Choose from available options only!\n")

    # Shift Amount Input
    while not good_input:
        try:
            shift = int(
                input(f"What shift amount should I use for the {process}: (1 to 26) ")
            )
            if shift < 1 or shift > 26:
                print("\nInvalid Input!! | Choose a valid number: (1 to 26)!\n")
            else:
                break
        except ValueError:
            print("\nInvalid Input!! | Choose a valid number: (1 to 26)!\n")

    # Message to Encode or Decode Input
    while not good_input:
        text = input(f"\nEnter the message to be {process}d: ").lower()
        break

    # routing for either encrypt or decrypt
    if not good_input:
        print(f"\nYour {process}d message is: {cypher(text, shift, process)}")

    # run app again?
    while not end_app:
        again = input("\nRun Again?  (Y/N) ").lower()
        if again == "n":
            end_app = True
        break


# ##########  End the app  ##########
print("\n\n--  End of Line --\n")
