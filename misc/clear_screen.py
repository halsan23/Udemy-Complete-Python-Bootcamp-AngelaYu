#####################################
# Clear Screen Function
# Created by - badDoggy | 11/07/26
#####################################


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


# End the app
print("\n\n--  End of Line --\n")
