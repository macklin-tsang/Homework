# Greeting chatbot
# Author: Macklin Tsang
# Date: January 09, 2023

import random 

# Greet user and ask for the name.
print("Hello, what's your name")

# Allows an input for the name.
name = input()

# Displays the message with name.
print("Nice to meet you, " + name)

# Ask for favourite movie
print("What's your favourite movie?")

# Let user respond
movie = input()

# Make a comment about it
comments = [" is a good one!", " isn't that good..", " was mid.", " was pretty good!"]

# Choose one randomly from the list
random_comment = random.choice(comments)

# Display random comment

print(movie + random_comment)
