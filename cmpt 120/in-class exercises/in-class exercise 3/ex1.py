# In Class Activity 3 - Chatbot v2
# Author: Macklin Tsang
# Date: Feb 2, 2023

# import the random module

import random

# create lists for yes answers, no answers and goodbyes

yeses = ["yes", "y", "of course", "certainly yes", "sure"]
noses = ["no", "n", "no way", "of course not", "never"]
byes = ["Goodbye!", "See you!", "ciao", "Have a good day"]

# ask the user if she wants to talk

talk = input("Hi dear user! Do you want to talk to me ==> ")

# check whether the user provides a valid answer.

while True:
    if talk in yeses:
        print("Great! Let's talk, my friend!")
        break
    if talk in noses:
        print(random.choice(byes))
        quit()
    if talk not in yeses or noses:
        print("Please input a valid answer.")
        talk = input("Hi dear user! Do you want to talk to me ==> ") # get the user's answer again

# show different responses based on the user's answer

# ask the user to ask a question and randomly provide a response from the yeses and noses lists

question = input("Ask me any question you want ==> ")

print(random.choice(yeses or noses) + "\n")

# ask the user to ask another question and randomly provide a response from the yeses and noses lists

question = input("Ask me other question you want ==> ")

print(random.choice(yeses or noses) + "\n")

# end the conversation and randomly provide a goodbye message from the byes list

print("OK, enough talking! \n" + random.choice(byes))