# Tuition Price 
# Author: Macklin Tsang
# Date: January 23, 2023

# This program is designed to display the projected semester tuition amount for the next 5 years.

# 1. Print the header for the table.

print('Year     Projected Tuition (per Semester)')
print('-----------------------------------------')

# 2. Save the initial tuition as $ 8000.

initialTuition = 8000

# 3. Calculate the tuition in year 1.

for i in range(1,6):
    initialTuition = 1.03 * initialTuition
    price = str(i) + '        $ ' + str("%.2f" % initialTuition)
    print(price)
    