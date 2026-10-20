# Simple Tip Calculator that takes
# - the Bill Amount
# - Percentage of Tip, and
# - # of people paying
#  to determine each person's total amount
# -----------------------------------------------------------
# badDoggy | 10/19/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os

# Clear Screen
# -----------------------------------------------------------
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Title
# -----------------------------------------------------------
print("Tip Calculator!\n")

# Inputs to set variables
# -----------------------------------------------------------
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? ")) / 100
people = int(input("How many people to split the bill? "))

# Calculate each person amount due (including tip)
# -----------------------------------------------------------
tip_amt = bill * tip
print(f"\nTip Amount ${tip_amt:.2f}")

each = (bill + tip_amt) / people

# ***NOTE
# :.2f
# -----------------------------------------------------------
# sometimes when you try to round a float to two digits, if the float
# only has 1 decimal place, it will NOT round to two decimal places.
# - THE FIX -
# using the (:.2f) on a string to format it to 2 decimal places
# -----------------------------------------------------------
# when running this app with the following inputs:
#   - bill: 150
#   - # of people: 5
#   - tip percent: 12
# each person would owe 33 dollars and 60 cents, but it would
# output as $33.6
# -----------------------------------------------------------

# by using the (:.2f) - it forces the output to 2 decimal places : $33.60
print(f"\nEach person owes ${each:.2f}")

print("\n\n- End of Line -")
