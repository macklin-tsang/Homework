# Group Assignment 2 - Turtles
# Authors: Macklin Tsang and Vansh Bali
# March 6, 2023

# This program is designed to draw 3 different pictures of our choice. 

# The program all contains pictures drawn using the Turtle module that consists of:
# Colorful drawings, 3+ right turns, 3 pen up & down changes, 3 for-loops, 
# 3 void functions for drawings / pen movement, 2+ functions with parameters,
# and a random color picker for pencolor and fillcolor using the Random module.

# All the defined functions are called at the end with arguments passed to the parameters.

# Import modules

import turtle
import random

# Colour list for random colour
colours = ["red","blue","green","yellow","pink","purple","orange","black"]

# Rename turtle
t = turtle.Turtle()

# User defined void function
# Parameters are x/y coordinates and radius.
# Output is a spiral.
def spiral(x,y,z):
    radius=z
    t.penup()
    t.goto(0+x,0+y)
    t.pendown()
    for i in range(25):
        t.pencolor(random.choice(colours))
        t.forward(5)
        t.circle(radius+i*5,360)

# User defined void function
# Parameters are x/y coordinates, radius, and colour.
# Output is mandala shape.
def mandala(x,y,z,colour_choice):
    radius=z
    t.penup()
    t.goto(0+x,0+y)
    t.pendown()
    t.pencolor(colour_choice)
    for i in range(20):
        t.forward(10)
        t.right(90)
        t.circle(radius+i*5,360)

# User defined void function
# Parameters are x/y coordinates.
# Output is random color-filled squares placed on top of each other.
def squares(x,y):
    t.penup()
    t.goto(0+x,0+y)
    t.pendown()
    for i in range(50):
        t.fillcolor(random.choice(colours))
        t.begin_fill()
        t.right(i*1.2)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.end_fill()

# Calling functions
spiral(-300,-300,10)
mandala(300,-300,10,"purple")
squares(300,300)

turtle.done()