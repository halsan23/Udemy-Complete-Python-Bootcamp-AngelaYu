# Basic print out "Hello World"#
# badDoggy | 10/17/26
# -----------------------------------------------------------


# Imports
# -----------------------------------------------------------
import subprocess
import os

# Clear Screen
# -----------------------------------------------------------
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# Output
print("Hello World!")
