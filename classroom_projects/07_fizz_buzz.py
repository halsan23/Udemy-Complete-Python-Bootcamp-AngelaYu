######################################
# Fizz/Buzz Challenge
# Created by - badDoggy | 09/25/26
######################################


# ############ Imports  ##############
import subprocess
import os

# Clear Screen
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


print("The Fizz/Buzz Challenge")
print("---------------------------------------------------")
print("Print out all numbers between 1 and 100 (inclusive)")
print('If number is evenly divisible by 3, print "Fizz"')
print('If number is evenly divisible by 5, print "Buzz"')
print("---------------------------------------------------")
for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
