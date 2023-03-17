# recursion

import turtle

max = turtle.Turtle()

def draw_tree(level, branch_length):

    if level == 0:
        max.color("green")
        max.stamp()
        max.color("brown")

    else:
        max.forward(branch_length)

        draw_tree(level-1, branch_length/1.61)

        max.left(40)
        draw_tree(level-1, branch_length/1.61)

        max.right(80)
        draw_tree(level-1, branch_length/1.61)
        
        max.left(40)
        max.back(branch_length)

max.speed(0)
max.left(90)
max.width(2)

draw_tree(5 , 120)

turtle.done()