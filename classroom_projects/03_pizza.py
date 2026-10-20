# Simple Pizza Order Form
#  to determine pizza's total amount
# -----------------------------------------------------------
# badDoggy | 10/20/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os

# Clear Screen
# -----------------------------------------------------------
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# base variables
# -----------------------------------------------------------
bill = 0


# Title
# -----------------------------------------------------------
print("Welcome to Python Pizzaria")
print("\nPizza Menu")
print("----------------------------------")
print(f"    - Small Pizza    $15.00.")
print(f"    - Medium Pizza   $20.00.")
print(f"    - Large Pizza    $25.00.\n")

print("Add Pepperoni")
print(f"    - Small          $ 2.00.")
print(f"    - Medium/Large   $ 3.00.\n")

print(f"Add Extra Cheese:    $ 1.00.")
print("----------------------------------\n")


# Input Choices
# -----------------------------------------------------------
size = input("Order Please, S, M, L? ").lower()
add_pep = input("\nAdd extra pepperoni? (Y/N) ").lower()
add_ch = input("\nAdd extra Cheese? (Y/N) ").lower()


# Calculate Total Bill
# -----------------------------------------------------------
if size == "l":
    size = "Lg."
    pizza = 25
elif size == "m":
    size = "Md."
    pizza = 20
else:
    size = "Sm."
    pizza = 15

if add_pep == "y":
    if size == "Sm.":
        pepperoni = 2
    else:
        pepperoni = 3

if add_ch == "y":
    cheese = 1

total_bill = pizza + pepperoni + cheese


# Print Out the Total Bill
# -----------------------------------------------------------
print("\n\nYour Total Bill:")
print("----------------------------------")
print(f"- {size} Pizza        ${pizza:.2f}")
print(f"- Extra Pepperoni   ${pepperoni:.2f}")
print(f"- Extra Cheese      ${cheese:.2f}")
print("----------------------------------")
print(f"            Total: ${total_bill:.2f}")


# -----------------------------------------------------------
print("\n\n- End of Line -\n")
