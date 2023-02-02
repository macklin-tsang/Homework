# Bad Wifi Connection
# Author: Macklin Tsang
# Date: Jan 26, 2023

# The purpose of this program is to help troubleshoot a user that has issues with their internet.

internet = print("Hello! I am here to fix your internet. I will give you a method and you can respond with either yes or no if it worked or not.")

def solved():
    print("\nI am glad that your problem is solved. Enjoy your day!")
    quit()

computer = input("\nReboot the computer and try to connect. Did that fix the problem? Answer y/n --> ")

# If the suggested method did not work, ask the next question along the flowchart.

if computer == "n": 
    router = input("\nReboot the router and try to connect. Did that fix the problem? Answer y/n --> ")
   
    if router == "n":
        cables = input("\nMake sure that the cables between the router are plugged in firmly. Did that fix the problem? Answer y/n --> ")
        
        if cables == "n":
            location = input("\nMove the router to a new location and try to connect. Did that fix the problem? Answer y/n --> ")

            if location == "n":
                print("\nGet a new router.")

# Whenever the method works (user doesn't type n), it will skip to the end and print the solved function, which contains the solved prompt.

solved()
