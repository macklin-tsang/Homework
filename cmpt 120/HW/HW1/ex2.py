# Name: User Input
# Author: Macklin Tsang
# Date: January 9, 2023

# This exercise is to create a program that will display the profits made by a company when given total sales amount. 
# This will be done by storing the number of total sales, multiply it by 0.25, and then printing the product which will represent the profit. 

# First, the program will ask what the projected total sales amount is.

print("What is your projected total sales amount?")

# Secondly, you will be able to input your projected total sales and the variable "total_sales" will contain the number (as a float if possible).

total_sales = float(input('Enter total sales amount: '))

# Thirdly, I created another variable where the "total_sales" variable will be multiplied by the float value of 0.25 (as the annual profit is typically 25% of total sales).
# The input and the 25% we are multiplying must be classified as float or int (in this case I set both to float) due to Python constraints with multiplying two different data types.

profit = total_sales * float(0.25)

# Lastly, the program will print out the profit after calculations.

print(profit)