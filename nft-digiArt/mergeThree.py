import turtle
import math
s = turtle.Screen()


s.bgcolor('white')
s.setup(width=1000, height=1000, startx=0, starty=0)

t = turtle.Turtle()


triangle_length = 2
directionValue = 0
turtle.tracer(0, 0)

for i in range(200):
    radius = triangle_length / math.sqrt(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(directionValue)
    t.forward(radius)
    t.pendown()
    t.right(150)
    t.forward(triangle_length)
    t.right(120)
    t.forward(triangle_length)
    t.right(120)
    t.forward(triangle_length)
    directionValue = directionValue + 2
    triangle_length = triangle_length + 2

    turtle.update()

turtle.update()

turtle.done()

# turtle.speed (0)
#
# turtle.pencolor("blue")
# for i in range (100):
#     turtle.forward(200)
#     turtle.left(125)

