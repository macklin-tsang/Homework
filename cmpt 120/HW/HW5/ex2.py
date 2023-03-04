# Turtle Car
# Author: Macklin Tsang
# Date: February 27, 2023

# This program is designed to draw and color the car in the example.

# Importing the turtle

import turtle

# Top of Car 

turtle.forward(85) # Draw the back of the car

turtle.right(80) # Turn the pen 80 degrees

turtle.circle(50, -200) # Draw the top of the car in a semi circle

turtle.right(80) # Reset the pen to go forward

turtle.forward(120) # Draw the hood of the car

# Front bumper of car

turtle.pencolor("red") # Set pen color to red for the rest of the drawing

turtle.right(90) # Turn the pen to go downwards

turtle.forward(60) # Draw the front bumper of the car

# Bottom of car

turtle.right(90) # Turn the pen to draw the bottom of the car

turtle.forward(60) # Draw the bottom of the car

turtle.circle(30, 360) # Create a full circle for the wheel

turtle.forward(195) # Draw the bottom of the car

turtle.circle(30, 360) # Create a full circle for the wheel

turtle.forward(49) # Draw the last end of the car. (Had to be subtracted by 1 from 50 or else it will be short by 1 pixel)

# Rear of car

turtle.right(90) # Turn the pen to draw upwards

turtle.forward(60) # Draw the rear of the car

turtle.right(90) # End in the original direction

turtle.done() # Finish the drawing