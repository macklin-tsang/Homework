# Salary Increase Program
# Author: Macklin Tsang
# Date: January 23, 2023

# This program is designed to calculate a percentage increase in salary,
# dependant on whether or not the salary is greater than 70000. 

# 1. Prompt user to input the salary

salary = float(input("Please enter your salary:"))

# 2. If salary is greater than 70000 , increase by 3%.
# If not, increase by 1%.

if salary >= 70000:
    print("The increased salary is: " + "$" + str(salary*1.03))
else:
    print("The increased salary is: " + "$" + str(salary*1.01))