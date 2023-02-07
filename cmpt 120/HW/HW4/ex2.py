# Date Month Year Formatter
# Author: Macklin Tsang
# Date: January 30, 2023

# This program will read a string from a user in the format of MM-DD-YYYY and it will print the date in the format of Month(Full Word), DD, YYYY.
# For example, 01-30-2023 will be converted to January 30, 2023

# 1. Greet user and ask for mm-dd-yyyy.

print("Hello user!")

date = input("Please enter mm-dd-yyyy: ")

# 2. Split the input date string by the hyphens, resulting in a list of the input strings.

date = date.split("-")

# 3. Create a list of months.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']

# 4. Print the converted format.

# For looking up the months in the list: Grab the first string (which is the month in number form), convert it into an integer, 
# and use that key number to look up the month in the months list.

# A slight issue will occur, since the list count starts with the first string being recognized at position #0.
# For example, if the input month integer is 1 (January), it will print February which is technically in the "#1" position in the list, but is not the first month of the year.
# To resolve this issue, we will subtract the integer by 1, so that it will return the month in our intended position.

# For example, if the input month integer is 1 (January), it will subtract that integer by 1, resulting in 0. 
# This will print January which is technically "#0" position in the list, but is the first month of the year.

print(months[int(date[0])-1] + ' ' + date[-2] + ', ' + date[-1])
