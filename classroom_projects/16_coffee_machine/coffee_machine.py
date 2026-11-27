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


def main_menu():
    """Displays the menu for the Coffee Machine choices"""
    clear_screen()
    print("       Coffee    Menu")
    print("------------------------------")
    for x, (item, details) in enumerate(MENU.items(), start=1):
        print(f" {x})  {item.title()}\t\t${details['cost']:.2f}")
    print("------------------------------")
    print(" 4)  Admin Menu")
    print("------------------------------")


def admin_menu():
    """Displays administrator options"""
    clear_screen()
    print("  Current    Ingredients")
    print("-----------------------------")
    print(f" 1)  Water\t{resources['water']} ml")
    print(f" 2)  Milk\t{resources['milk']} ml")
    print(f" 3)  Coffee\t{resources['coffee']} g")
    print(f" 4)  Cash\t${resources["money"]:.2f}")
    print("-----------------------------")
    print(" 5)  Add Ingredients")
    print(" 6)  Return to Main Menu")
    print(" 7)  Turn Coffee Machine Off")
    print("-----------------------------")


def add_ingredients():
    """Add resources to the Coffee Machine"""
    while True:
        clear_screen()
        report(resources["money"])
        print(" 4)  Return to Admin Menu")
        print("-------------------------")
        try:
            this_choice = int(input("Which resource would you like to add? "))
            if this_choice == 4:
                break
            if 1 <= this_choice <= 3:
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
    print(f"{coffee_item.capitalize()} requires the following:")
    print("\n\tRequired\tOn Hand")
    print("--------------------------------")
    # print(f"Water\t {MENU[select]["ingredients"]["water"]}")
    for item, data in MENU[coffee_item]["ingredients"].items():
        print(f"{item.capitalize()}:\t  {data}\t\t{resources[item]}")
    print("--------------------------------")


def error(num):
    """Display for Invalid Input"""
    print(f"\nInvalid Input!  Select 1 to {num} only!")
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
    while choice not in (1, 2, 3, 4):
        main_menu()
        try:
            choice = int(input("Please make a selection: "))
            if not 1 <= choice <= 4:
                error(4)
                choice = None
        except ValueError:
            error(4)
            choice = None
    # process user input
    if choice in (1, 2, 3):
        low_ingredients = False
        # make sure there is enough ingredients
        select = options[choice - 1]
        if resources["water"] < MENU[select]["ingredients"]["water"]:
            low_ingredients = True
        elif resources["milk"] < MENU[select]["ingredients"]["milk"]:
            low_ingredients = True
        elif resources["coffee"] < MENU[select]["ingredients"]["coffee"]:
            low_ingredients = True

        if low_ingredients:
            print(f"\nWe're sorry, The machine is out of {select.capitalize()}.")
            print("Please notify your administrator.")
            input("\npress any key to continue...")

        else:
            paid = None
            while not paid:
                paid = input(f"\nPlease insert ${MENU[select]["cost"]:.2f} for you hot cup of {select.capitalize()}: ")
                try:
                    if float(paid) == MENU[select]["cost"]:
                        resources["money"] += float(paid)
                    else:
                        print("\nInvalid Amount:")
                        input("press any key to continue...")
                        paid = "pass"
                        main_menu()
                        break
                except ValueError:
                    print("You need to add the cost of the coffee.")
                    input("press any key to continue...")
                    paid = None
            if paid != "pass":
                remove_ingredients(select)
                print(f"\nEnjoy your {select.capitalize()}.")
                choice = None
                input("press any key to continue...")

    else:
        admin_menu()

        # Turn off the coffee machine (end the app)
        # else:
        end_app = True
        break


# End the app
print("\n\n--  End of Line --\n")
