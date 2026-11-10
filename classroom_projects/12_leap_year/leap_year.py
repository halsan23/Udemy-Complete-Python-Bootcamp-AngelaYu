######################################
# Leap Year Calculator
# Created by - badDoggy | 11/10/26
######################################


# ###########  Imports  ##############
import subprocess
import os


# #########  Functions  ##############
# Clear Screen & display the logo
def clear_screen():
    """
    Clears the screen and displays the app title
    """
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True, check=False)

    # Display Title
    print("------------------------")
    print("  Leap Year Calculator")
    print("------------------------")


# Determine if is a leap year
def is_leap_year(year):
    """
    Takes a year as an input and
    determines if it is a Leap Year
    """
    output = False
    if year % 4 == 0:
        if year % 100 != 0:
            output = True
        elif year % 400 == 0:
            output = True

    if output:
        return f"\n{year} is a leap year."
    else:
        return f"\n{year} is not a leap year."


# #########  Variables  ##############
end_app = False


while not end_app:
    # Clear Screen
    clear_screen()

    # Input - Year to check
    while True:
        year_to_check = input("\nQ)uit or enter the year you would like to check? ")
        if year_to_check == "q" or year_to_check == "quit":
            end_app = True
            break
        else:
            try:
                # convert input to an integer
                year_to_check = int(year_to_check)
                # Check if input is a leap year
                print(is_leap_year(year_to_check))
                break
            except:
                print("\nINVALID INPUT!  Input must be a 4 digit year!")
                input("\nPress any key to continue..")
                clear_screen()

    # Run Again?
    if not end_app:
        again = input("\nCheck Another year?  (Y/N)").lower()
        if again == "n":
            break


# End the app
print("\n\n--  End of Line --\n")
