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


# Run App
############################################
# Clear Screen
clear_screen()


############################################


# End the app
print("\n\n--  End of Line --\n")
