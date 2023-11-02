import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def random_color():
    return random.choice(colors)

def random_shape():
    shape = random.choice(['circle', 'square', 'triangle', 'star'])
    if shape == 'circle':
        turtle.circle(50)
    elif shape == 'square':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    elif shape == 'triangle':
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    elif shape == 'star':
        for i in range(5):
            turtle.forward(100)
            turtle.right(144)

turtle.speed('fastest')
for i in range(10):
    turtle.pencolor(random_color())
    random_shape()
    turtle.penup()
    turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
    turtle.pendown()

import turtle
import random
t=turtle.Turtle()
t.speed(0)
colors =["red","orange","yellow","green","blue","purple"]
def draw_shapes(sides):
    for i in range(sides):
        t.forward(100)
        t.right(360/sides)

while True:
    sides=random.randint(3,10)
    color=random.choice(colors)
    t.pencolor(color)
    draw_shapes(sides)
    t.right(10)
turtle.done()
