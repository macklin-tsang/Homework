# Monthly Payment Car Loan Calculator
# Author: Macklin Tsang
# Date: January 12, 2023

# 1. Prompt user to fill in loan amount, which will convert to float if possible because payment may not neccessarily be flat.
# For example, the loan amount could be $30,486.98 .

print("This program will calculate your monthly car loan payment on a 10 month period. Please enter in your loan amount.")

loan_amount = float(input('Please enter the loan amount: '))

# 2. Calculate the effective interest given the loan amount.

effective_interest = (loan_amount / 100) / 12

# 3. Calculate payment when given loan amount, effective interest and number of months.

payment = loan_amount * (effective_interest / (1-(1+effective_interest)**(-10)))

# 4. Rounding the payment to three decimal points and assigning the total as "total".

total = "%.3f" % payment

# 5. Display the monthly payment for the car loan.

print('Your monthly payment will be: $' + total)