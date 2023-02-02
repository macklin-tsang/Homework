# Pocket Roulette
# Author: Macklin Tsang
# Date: January 23, 2023

# This program is a roulette wheel consisting of 36 pockets.
# It is designed to return the respective pocket color based on the input integer provided.

# 1. Prompt the user for a pocket number and convert to integer.

pocket = int(input("Enter a pocket number: "))

# 2. Create a function consisting of passing through the integer along the constrictions provided.
# The pocket color will differ between red or black, if the number is between a certain range and whether or not it's even or odd.
# If the number is 0, the pocket color is green.
# Pocket Modulo (%) 2 == 0 determines if the pocket number is even or not. Even numbers will result in 0 after modulo 2.

def roulette():
    if pocket > 36 or pocket < 0:
        print("Please input a number between 0 and 36.")
        # If the number is out of range, it will return an error message.
    if pocket == 0:
        print("Green")
    if 10 >= pocket >= 1 or 28 >= pocket >= 19: # If number is between 1-10 or 19-28:
        if pocket % 2 == 0: # If pocket is even:
            print("Black")
        else: # If pocket is not even:
            print("Red")
    if 18 >= pocket >= 11 or 36 >= pocket >= 29: # If number is between 11-18 or 29-36:
        if pocket % 2 == 0: # If pocket is even: 
            print("Red")
        else: # If pocket is not even:
            print("Black")

# 3. Call the function to display pocket color based on input pocker number.
roulette()