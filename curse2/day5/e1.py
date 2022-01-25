from turtle import *
import random
import turtle 

line = Turtle()
screen = Screen()

#siempre se debe de poner color mode
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    random_col= (r,g,b)
    return random_col


def edges(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        line.forward(30)
        line.right(angle)

for i in range(3,11):
    edges(i)
    line.color()


'''for _ in range(3):

    line.forward(30)
    #triangle
    #line.right(240)
    #saquare
    line.right(90)
'''

screen.exitonclick()