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
    print(f" 1)  Water\t{resources['water']}  units")
    print(f" 2)  Milk\t{resources['milk']}  units")
    print(f" 3)  Coffee\t{resources['coffee']}  units")
    print(f" 4)  Cash\t${resources["money"]:.2f}")
    print("-----------------------------")
    print(" 5)  Return to Main Menu")
    print(" 6)  Turn Coffee Machine Off")
    print("-----------------------------")
    print("(1 - 4) to add ingredients,")


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
    # set initial variables
    choice = None
    select = None

    # Main Menu user input
    while choice not in ('1', '2', '3', '4'):
        main_menu()
        choice = input("Please make a selection: ")
        if choice not in ('1', '2', '3', '4'):
            error(4)
            choice = None

        # process user input
        elif choice in (1, 2, 3):
            # make sure there is enough ingredients
            low_ingredients = False
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

            # prompt to pay for coffee
            else:
                paid = None
                while not paid:
                    paid = input(f"\nPlease insert ${MENU[select]["cost"]:.2f} for you hot cup of {select.capitalize()}: ")

                    # check user enters correct amount - EXACT CHANGE ONLY!!
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
                        print("\nInsufficient funds for the coffee.")
                        input("press any key to continue...")
                        paid = "pass"
                        main_menu()

                # coffee paid for  -  dispense the coffee
                if paid != "pass":
                    remove_ingredients(select)
                    print(f"\nEnjoy your {select.capitalize()}.")
                    choice = None
                    input("press any key to continue...")

        # Admin Menu
        else:
            # process admin input
            choice = None
            while choice not in ('1', '2', '3', '4', '5', '6'):
                admin_menu()
                choice = input("Please select (1 - 6): ")

                # Add ingredients
                if choice in ('1', '2', '3', '4'):
                    print(f"You Selected: {choice}")
                    end_app = True

                # input error
                elif choice not in ('5', '6'):
                    error(6)
                    choice = None

            # an input of 5 will just reroute back to the
            # beginning and return to the Main Menu.

            # Turn off Coffee Machine  - -  end app
            if choice == '6':
                end_app = True
                break



# End the app
print("\n\n--  End of Line --\n")
