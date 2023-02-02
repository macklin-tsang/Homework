# Divisible Integer
# Author: Macklin Tsang
# Date: January 23, 2023

# This program is designed to determine if the input integer is divisible  it is
# divisible by 5 and 6, whether it is divisible by 5 or 6, and whether it is divisible by 5 or 6, but not both

# 1. Prompt user for an integer

integer = int(input("Enter an integer: "))

# 2. Set a variable for the result of each condition and pass through the integer through all the conditions, where each 
# line will return true or false, whether or not the condition is satisfied.

# Modulo 1 == 0 was used after the divison because if the post-divided integer had a remainder, it would not equal to 0. 
# All post-divided integers that did not have a remainder will equal to 0 after the modulo process,
# Which is the condition if the input integer is divisible. 

def calculate():
    five_and_six = (integer / 5) % 1 == (integer / 6) % 1 == 0
    five_or_six = (integer / 5) % 1 == 0 or (integer / 6) % 1 == 0
    both = five_and_six != five_or_six

# Concatenating the print statements by converting the input integer and condition variables into strings.

    print("Is " + str(integer) + " divisible by 5 and 6? " + str(five_and_six))
    print("Is " + str(integer) + " divisible by 5 or 6? " + str(five_or_six))
    print("Is " + str(integer) + " divisible by 5 or 6, but not both? " + str(both))

# 3. Display the results by calling the function.

calculate()