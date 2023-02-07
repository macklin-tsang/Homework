# Choice Game
# Author: Macklin Tsang
# Date: Feb 2, 2023

# This program will show users a set of choices, and then respond to those choices until they choose to quit, using the keyword 'q'.

print("Welcome! What would you like to do?")

# Ask the user to enter the string of even length. It will display the last half string.
# For example, the word "HelloWorld" will be displayed as "World"

def halfString():
        string = input('Please input string of even length: ')

        if len(string) % 2 != 0: # If the user enters an uneven string, it will ask them to re-enter an even string.
            print("Please enter an even string.")
        elif len(string) % 2 == 0:
            print(string[len(string)//2:]) # It will splice and print the characters starting from the middlemost position to the end of the word.

# As the k user to enter the string. Your function should display the string made up of the first three characters.
# For example, HelloWorld will display Hel.

def firstThree():
        string = input('Please enter a string: ')
        if string == "": # If the string is empty, it will display "Empty String"
            print("Empty String.")
        print(string[:3]) # If the string is shorter than 3, it will print out what has been input already.

# Creating a quit function with the print statement and quit function.

def ending():
    print('See you later.')
    quit()

# Create a while loop so the menu of option constantly appears after responses.

while True:

    word = input('''
[1] Enter 1 to print Half string.
[2] Enter 2 to print First three characters.
[q] Enter 'q' to quit.
Enter your options:
''')

    if word == "1": # If the user inputs 1, it will call the halfString function.
        halfString()
    elif word == "2": # If the user inputs 2, it will call the firstThree function.
        firstThree()
    elif word == "q": # When a user enters ‘q’, it should display “See you later”. 
        ending()
    else:
        print("Please enter a valid character.")
