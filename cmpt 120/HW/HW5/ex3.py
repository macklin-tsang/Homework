import turtle

c = turtle.Turtle()
c.getscreen()

# Base of car
'''
turtle.forward(300)
turtle.circle(10, 180)
turtle.forward(600)
turtle.circle(10, 180)
turtle.forward(300)'''

# Left headlight

turtle.up()
turtle.left(180)
turtle.forward(250)
turtle.right(90)
turtle.forward(20)
turtle.down()
turtle.forward(125)
turtle.circle(-45, 180)
turtle.forward(125)

# Moving to other side

turtle.up()
turtle.left(90)
turtle.forward(315)

# Right headlight

turtle.left(90)
turtle.down()
turtle.forward(125)
turtle.circle(-45, 180)
turtle.forward(125)

# moving to the middle

turtle.right(90)
turtle.forward(90)


# Middle piece

turtle.right(90)
turtle.forward(135)

# Hood

turtle.left(38)
turtle.circle(215, 98)

# Hood outline
'''
turtle.circle(157, 180)
turtle.forward(25)'''



''' turtle.up()
turtle.left(90)
turtle.forward(20)
turtle.down()
turtle.forward(100)'''

turtle.done()
