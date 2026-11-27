"""
Coffee Machine Project

Author: badDoggy
Date: 11/26/2026
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
    print("       Coffee    Menu")
    print("------------------------------")
    for x, (item, details) in enumerate(MENU.items(), start=1):
        print(f" {x}) {item.title()}\t\t${details['cost']:.2f}")
    print(" - - - - - - - - - - - - - - -")
    print(" 4) Ingredients Report")
    print(" 5) Turn Machine Off")
    print("------------------------------")


def report(cash):
    """
    Display the current available machine resources
    """
    print(" Current   Ingredients")
    print("-----------------------")
    print(f" 1)  Water\t{resources["water"]}ml")
    print(f" 2)  Milk\t{resources["milk"]}ml")
    print(f" 3)  Coffee\t{resources["coffee"]}g")
    print(f" 4)  Money\t${cash:.2f}")
    print("-----------------------")


def add_resources():
    """Add resources to the Coffee Machine"""
    clear_screen()
    report(resources["money"])
    choice = ""
    print(" 5)  Return to Main Menu")
    print("------------------------")
    while choice not in (1, 2, 3, 4, 5):
        try:
            choice = int(input("Which resource would you like to add? "))
            if choice == 5:
                return
            if 1 <= choice <= 5:
                select = resource_items[choice - 1]
                try:
                    add_resource = int(
                        input(
                            f"\nHow much {select.capitalize()} would you like to add? "
                        )
                    )
                    # new_value = resources[select] + add_resource
                    # resources.update({f"{resources[select]}": new_value})
                    resources[select] = resources[select] + add_resource
                    input(resources[select])
                    report(resources["money"])
                except ValueError:
                    error()
                    add_resources()
            else:
                error()
                add_resources()
        except ValueError:
            error()
            add_resources()


def insufficient_resources(coffee_item):
    """Display for insufficient resources to produce the user selected coffee"""
    print("\nInsufficient Resources!  Please check the reports.")
    print(f"{coffee_item.capitalize()} requires the following:")
    print("\n\tRequired\tOn Hand")
    print("--------------------------------")
    # print(f"Water\t {MENU[select]["ingredients"]["water"]}")
    for item, data in MENU[coffee_item]["ingredients"].items():
        print(f"{item.capitalize()}:\t  {data}\t\t{resources[item]}")
    print(f"Cost:\t  ${MENU[coffee_item]["cost"]:.2f}\t\t${resources["money"]}")
    print("--------------------------------")


def error():
    """Display for Invalid Input"""
    print("\nInvalid Input!  Select 1 to 5 only!")
    input("press any key to continue...\n")


# #########  Variables  ##############
options = ["espresso", "latte", "cappuccino"]
resource_items = ["water", "milk", "coffee", "money"]
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
                error()
                clear_screen()
                choice = ""
        except ValueError:
            error()
            clear_screen()
            choice = ""

    if choice in (1, 2, 3):
        select = options[choice - 1]
        if resources["money"] < MENU[select]["cost"]:
            insufficient_resources(select)
        else:
            print(f"\nEnjoy your {select.capitalize()}.")
        choice = ""
        input("press any key to continue...")

    # Display report for remaining resources
    elif choice == 4:
        clear_screen()
        report(resources["money"])
        choice = input("A)dd Resources or R)eturn to Menu? ").lower()
        if choice in ("a", "add"):
            add_resources()

    # Turn off the coffee machine (end the app)
    else:
        end_app = True
        break


# End the app
print("\n\n--  End of Line --\n")
