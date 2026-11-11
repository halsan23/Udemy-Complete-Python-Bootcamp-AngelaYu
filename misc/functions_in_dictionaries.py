###########################################
# Functions in Dictionaries and Variables
# badDoggy | 11/11/26
###########################################


# ##########  Imports  ##############
import subprocess
import os


# #########  Functions  ##############
# Clear Screen
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


clear_screen()


# Sometimes you may wish to call your functions from a variable or from within a dictionary.
#
# This is easily accomplished by omitting the parenthesis during variable/dictionary assignment.
# This works because it is the parenthesis that actually "call" the function.
#
# For example:
#     let's define some functions that perform math calculations


# Math Functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print("Define the functions:\n")
print("def add(n1, n2):")
print("    return n1 + n2")
print()
print("def subtract(n1, n2):")
print("    return n1 - n2")
print()
print("def multiply(n1, n2):")
print("    return n1 * n2")
print()
print("def divide(n1, n2):")
print("    return n1 / n2")
print("\n---------------------------------------------------\n")


# Now we could assign any one of these to a variable, by omitting the parenthesis.
# THis will assign the function to the variable WITHOUT ACTUALLY CALLING THE FUNCTION.
addition = add

# and now to use the function, call the variable WITH parenthesis AND the function parameters
print(f"Calling the add function from a variable:")
print("   **notice no parenthesis when assigning the variable,")
print("     only when calling the function (from the variable)\n")
print("addition = add")
print(f"addition(2, 2):      2 + 2 = {addition(2, 2)}")
print("\n---------------------------------------------------\n")


# USING DICTIONARIES
# We can do the same using a dictionary.
# First, let's define our dictionary
math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# So we are defining (+, -, *, /) as our "keys"
# We then define our math functions (minus the parenthesis), as the values
#
# So if we call:
#     math_operations["+"](num1, num2)
#          - runs the add function and adds num1 to num2
#
#     math_operations["-"](num1, num2)
#          - runs the subtract function and subtracts num2 from num1
#
#     math_operations["*"](num1, num2)
#          - runs the multiply function and multiplies num1 and num2
#
#     math_operations["/"](num1, num2)
#          - runs the divide function and divides num1 by num2
#
# **Notice the use of square brackets to identify the "KEY" and the
#   parenthesis to "call" the function with the required parameters

print("Calling the math functions from a dictionary.\n")
print("First, create the dictionary:")
print("    **notice no parenthesis when assigning the dictionary values,")
print("      only when calling the function (from the dictionary).\n")

print("math_operations = {")
print('     "+": add,')
print('     "-": subtract,')
print('     "*": multiply,')
print('     "/": divide,')
print("}\n")


print(f'math_operations["+"](5, 5):     5 + 5 = {math_operations["+"](5, 5)}')
print(f'math_operations["-"](5, 5):     5 - 5 = {math_operations["-"](5, 5)}')
print(f'math_operations["*"](5, 5):     5 * 5 = {math_operations["*"](5, 5)}')
print(f'math_operations["/"](5, 5):     5 / 5 = {math_operations["/"](5, 5)}')


# End the app
print("\n\n--  End of Line --\n")
