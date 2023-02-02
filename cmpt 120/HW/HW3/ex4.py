# Island Game
# Author: Macklin Tsang
# Date: January 23, 2023

# This program is a text based game, where the user is a survivor on a stranded island and must gather materials, in order to survive.

import random

# These prompts assume that the user will answer properly (type only y or n when asked to).

# 1. Ask if the user wants to play.

play = input("Do you want to play? Answer y/n --> ")

# 2. If the user wants to play, continue with the game. If not, end the game.

if play == "n":
    print("Sad to hear, please consider playing next time.")
    quit()
elif play == "y":
    print("Welcome to the game! You are stranded on a deserted island. \n")

# 3. Ask if user wants to harvest wood.

tree = input("You see a dead tree laying on the ground. Would you like to harvest the wood for shelter & fire? Answer y/n --> ")

if tree == "y":
    print("You have harvested wood for the shelter & fire!")

# 4. Ask if user wants to harvest coconut.

coconut = input("You see a coconut dropping from a tree. Would you like to harvest the coconut for water? Answer y/n --> ")

if coconut == "y":
    print("You have harvested coconut for your thirst!")

# 5. Ask if user wants to harvest fish.

fish = input("You see a crowd of fish swimming in the ocean. Would you like to harvest the fish? Answer y/n --> ")

if fish == "y":
    print("You have harvested fish for your hunger!")

# 6. Ask if user wants to start a fire with a singular match found. 
# If they want to, they must guess the number correctly to start the fire, as a chance type of situation.

fire = input("It is getting dark soon, would you like to build a fire? Answer y/n --> ")

if fire == "y":
    print("While gathering your materials for the fire, you luckily find a singular match!")

    success_matches = random.randint(0,5)

    matches = int(input("Guess a number between 0 - 5. If you are correct, the fire will light up. --> "))
    
    if matches == "5":
        print("Nice! Your fire is now blazing.")
    else:
        print("Unlucky! Your fire was not able to be lit.")

# 7. Ask if user wants to alert the helicopter. 
# If they do so, they will be rescued and live. If not, they will eventually die.
# Either way, the program will thank the user for playing and give a random number to how many days they remain on the island.

helicopter = input("You see a helicopter in the air. Would you like to create a signal to catch their attention? Answer y/n --> ")

if helicopter == "y":
    print('')
    print("Congratulations! The helicopter has seen your signal and is coming down to rescue you!")
    print("Thank you for playing the game! " + "You have been stranded for " + str(random.randint(1, 25)) + " days before getting back to your home!")
else:
    print('')
    print("Unfortunately the helicopter did not see you and you do not get rescued.")
    print("Thank you for playing the game! " + "You have survived for " + str(random.randint(50, 100)) + "days before eventually dying!")
