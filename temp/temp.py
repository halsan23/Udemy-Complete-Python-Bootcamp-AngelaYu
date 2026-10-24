import subprocess
import os
import random

computer_choices = ["Rock", "Paper", "Scissors"]


while True:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    # id = random.randint(0, len(computer_choices) - 1)
    # print(f"Id = {id}  |  Computer Choice = {computer_choices[id]}")

    pick = random.choice(computer_choices)
    print(f"Computer Choice = {pick}")

    end = input("Any key to continue = B)reak: ")
    if end == "b":
        break
