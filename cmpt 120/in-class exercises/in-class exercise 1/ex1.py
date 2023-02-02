# Weekly Pay Calculator
# Author: Macklin Tsang
# Date: January 12, 2023

# 1. Prompt user to input their hourly wage, regular hour amount and overtime hour amount. 
# The input values have been set to convert to float, if possible, as both hourly shifts and wages can be fractional.
# For example, working a 7.5 hour shift for $15.65 an hour.

print("This program will calculate your weekly pay. Please enter in your hours worked and your wage rate.")

hourly_wage = float(input('Enter your hourly wage: '))

regular_hours = float(input('Enter your regular hours: '))

overtime_hours = float(input('Enter your overtime hours: '))

# 2. Calculate amount made from hourly wage & regular hours

regular_wage = hourly_wage * regular_hours

# 3. Calculate amount made at an overtime hourly wage & overtime hours

overtime_wage = (1.5 * hourly_wage) * overtime_hours

# 4. Add the regular wage and overtime wage amounts.

total_pay = regular_wage + overtime_wage

# 5. Round the total weekly pay to 1 decimal.

total_pay = "%.1f" % total_pay 

# 6. Display the total weekly pay.

print('Your total weekly pay is $' + str(total_pay) + '.')