# Custom Boxed Message
# Author: Macklin Tsang
# Date: January 15, 2023

# This program is to allow the user to set a message and have a box, made of their desired character, to surround the message. 

# 1. Ask user to enter a message and their desired box character.

message = input("What do you want your sign to say? ")

box_character = input("What character do you want for your box? ")

print()

# 2. Put the desired box character on both sides of the message, while using empty text strings as spacers and reassign message.

message = box_character + " " + message + " " + box_character

# 3. Print the amount of box characters in respect to the number of characters that the message will consist of including the box characters that surround the message.
# After the top of the box has been printed, the message will print on a separate line under the top of the box, continued by the bottom of the box printed below the message.

print (len(message)*box_character + '\n' + message + '\n' + len(message)*box_character)
