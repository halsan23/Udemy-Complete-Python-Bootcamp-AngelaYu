"""
Coffee Machine Project

Author: badDoggy
Date: 11/25/2026
"""

# ##########  Imports  ##############
import subprocess
import os
from ascii_art import logo
from data import MENU, resources


# #########  Functions  ##############
# Clear Screen, Print Logo, Display the Menu
def clear_screen():
    """Clear the terminal screen.
    \nDisplay the Logo"""
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)
    print(logo)


def menu():
    """Displays the menu for the Coffee Machine choices"""
    print("    Coffee   Menu")
    print("----------------------------")
    x = 1
    for key in MENU:
        print(f" {x}) {key.title()}")
        x += 1
    print(" 4) Print Report")
    print(" 5) Turn Coffee Machine Off")
    print("----------------------------")


# #########  Variables  ##############
end_app = False

# ########  Run the App  #############
while not end_app:
    # Clear Screen, Print Logo, Display the Menu
    choice = ""

    # user input
    while choice not in (1, 2, 3, 4, 5):
        clear_screen()
        menu()
        try:
            choice = int(input("Please make a selection: "))

            if not 1 <= choice <= 5:
                print("\nInvalid Selection!!  Choose 1 to 5 only.")
                input("press any key to continue...")
                clear_screen()
                choice = ""

        except ValueError:
            print("\nInvalid Selection!!  Please use the number keys to make a choice.")
            input("press any key to continue...")
            clear_screen()
            choice = ""

    if choice in (1, 2, 3):
        print(f"\nYou selected: {choice}")
        choice = ""
        input("press any key to continue...")

    # Display report for remaining resources
    elif choice == 4:
        clear_screen()
        print("  Resource     Amount")
        print("-----------------------")
        for key, value in resources.items():
            print(f"   {key.capitalize()} \t{value}")
        print("-----------------------")
        choice = ""
        input("Press any key to continue...")

    # Turn off the coffee machine (end the app)
    else:
        end_app = True
        break

print(f"\n{MENU},\n\n{resources}")


# End the app
print("\n\n--  End of Line --\n")
