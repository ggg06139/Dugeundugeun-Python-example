import turtle
import random

t=turtle.Turtle()
A = ['red','green','blue']
def square(l):
    for i in range(5):
        t.fd(l)
        t.lt(144)
for j in range(10):
    t.penup()
    t.goto(random.randint(-200,200),random.randint(-200,200))
    t.pendown()
    t.color('black',random.choice(A))
    t.begin_fill()
    square(random.randint(50,100))
    t.end_fill()
