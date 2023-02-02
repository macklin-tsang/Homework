# Feet to meters conversion
# Author: Macklin Tsang
# Date: January 15, 2023

# This program is to allow the user to enter a measurement in feet and have the conversion to meters displayed.

# 1. Ask user to enter a measurement in feet and convert the inputted value as a float if possible.

feet = float(input('How many feet? '))

# 2. Convert feet to meters and have it display as 1 decimal.

meters = 0.3048 * float(feet)

meters = ("%.1f" % meters)

# 3. Display the converted value from feet to meters to exactly 1 decimal. 

print(str(feet) + " is about " + str(meters) + " meters")