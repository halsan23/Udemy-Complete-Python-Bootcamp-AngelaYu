"""
Coffee Machine Project

Author: badDoggy
Date: 11/27/2026
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
        print(f" {x})  {item.title()}\t\t${details['cost']:.2f}")
    print(" - - - - - - - - - - - - - - -")
    print(" 4)  Ingredients Report")
    print(" 5)  Turn Machine Off")
    print("------------------------------")


def report(cash):
    """
    Display the current available machine resources
    """
    print(" Current   Ingredients")
    print("-------------------------")
    print(f" 1)  Water\t{resources['water']} ml")
    print(f" 2)  Milk\t{resources['milk']} ml")
    print(f" 3)  Coffee\t{resources['coffee']} g")
    print(f" 4)  Money\t${cash:.2f}")
    print("-------------------------")


def add_ingredients():
    """Add resources to the Coffee Machine"""
    while True:
        clear_screen()
        report(resources["money"])
        print(" 5)  Return to Main Menu")
        print("-------------------------")
        try:
            this_choice = int(input("Which resource would you like to add? "))
            if this_choice == 5:
                break
            if 1 <= this_choice <= 4:
                this_selection = resource_items[this_choice - 1]
                try:
                    add_resource = int(
                        input(
                            f"\nHow much {this_selection.capitalize()} would you like to add? "
                        )
                    )
                    resources[this_selection] = resources[this_selection] + add_resource
                    report(resources["money"])
                except ValueError:
                    error()
            else:
                error()
        except ValueError:
            error()


def remove_ingredients(coffee):
    """Removes ingredients from the DataBase for the coffee created"""
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["money"] -= MENU[coffee]["cost"]


def insufficient_resources(coffee_item):
    """Display for insufficient resources to produce the user selected coffee"""
    print("\nInsufficient Resources!  Please check the reports.")
    print(f"{coffee_item.capitalize()} requires the following:")
    print("\n\tRequired\tOn Hand")
    print("--------------------------------")
    # print(f"Water\t {MENU[select]["ingredients"]["water"]}")
    for item, data in MENU[coffee_item]["ingredients"].items():
        print(f"{item.capitalize()}:\t  {data}\t\t{resources[item]}")
    print(f"Cost:\t  ${MENU[coffee_item]['cost']:.2f}\t\t${resources['money']:.2f}")
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
    choice = None
    select = None
    # user input
    while choice not in (1, 2, 3, 4, 5):
        clear_screen()
        menu()
        try:
            choice = int(input("Please make a selection: "))
            if not 1 <= choice <= 5:
                error()
                clear_screen()
                choice = None
        except ValueError:
            error()
            clear_screen()
            choice = None
    # process user input
    if choice in (1, 2, 3):
        # make sure there is enough ingredients
        select = options[choice - 1]
        if resources["water"] < MENU[select]["ingredients"]["water"]:
            insufficient_resources(select)
        elif resources["milk"] < MENU[select]["ingredients"]["milk"]:
            insufficient_resources(select)
        elif resources["coffee"] < MENU[select]["ingredients"]["coffee"]:
            insufficient_resources(select)
        elif resources["money"] < MENU[select]["cost"]:
            insufficient_resources(select)
        # if enough ingredients, remove the ingredients from the resources and make the coffee
        else:
            remove_ingredients(select)
            print(f"\nEnjoy your {select.capitalize()}.")
        choice = None
        input("press any key to continue...")

    # Display report for remaining resources
    # Option to add resources
    elif choice == 4:
        while True:
            try:
                clear_screen()
                report(resources["money"])
                print(" 5)  Add Resources")
                print(" 6)  Return to Main Menu")
                print("-------------------------")
                # options to "Add" ingredients to the machine or "Return" to the Main Menu
                sub_choice = int(input("Please make a selection: "))
                if sub_choice not in (5, 6):
                    print("\nInvalid Input!  Select 1 to 6 only!")
                    input("press any key to continue...\n")
                elif sub_choice == 5:
                    choice = None
                    select = None
                    add_ingredients()
                    break
                else:
                    break
            except ValueError:
                print("\nInvalid Input!  Select 1 to 6 only!")
                input("press any key to continue...\n")

    # Turn off the coffee machine (end the app)
    else:
        end_app = True
        break


# End the app
print("\n\n--  End of Line --\n")
