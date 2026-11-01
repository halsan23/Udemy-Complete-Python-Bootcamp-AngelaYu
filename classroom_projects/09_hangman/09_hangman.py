######################################
# Hangman
# Created by - badDoggy | 11/01/26
######################################


# ###########  Imports  ##############
import subprocess
import os
import random
from wordlist import words

# Clear Screen
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


word = random.choice(words)
print(word)
