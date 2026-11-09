######################################
# App Name
# Created by - badDoggy | D A T E
######################################


# ###########  Imports  ##############
import subprocess
import os


# #########  Functions  ##############
# Clear Screen & display the logo
def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)


# Clear Screen
clear_screen()


# Classroom Work
############################################
# Standard Dictionary
capitols = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested Lists
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Print Lillie
print(f'Print "Lillie": {travel_log1["France"][1]}')


# -------------------------------------
nested_list = ["A", "B", ["C", "D"]]
# print D
print(f'\nPrint "D": {nested_list[2][1]}')

# -------------------------------------
# Nested Dictionaries
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}
# Print "Stuttgart"
print(f'\nPrint "Stuttgart": {travel_log2["Germany"]["cities_visited"][2]}')


############################################


# End the app
print("\n\n--  End of Line --\n")
