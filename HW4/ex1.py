# Location Acronym
# Author: Macklin Tsang
# Date: January 30, 2023

# This program is designed to take the first character of the strings containing the city, province and country name and printing them as an acronym.
# For example, if the user enters Richmond, BC, Canada, the program should display R.B.C. 

# 1. Greet and ask user to input city, province and country.

print("Hello user! \n")

# 2. Split the input answer into separate strings.

location = input("Please input your city, province and country: ").split()

# 3. Create a container labelled acronym

acronym = []

for x in location:
    acronym.append(x[0])

print('.'.join(acronym))

print("\nGoodbye user!")