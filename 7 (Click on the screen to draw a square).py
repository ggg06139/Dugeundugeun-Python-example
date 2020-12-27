import turtle
t =turtle.Turtle()
t.shape('turtle')

def s(l):
    for _ in range(4):
        t.fd(l)
        t.lt(360/4)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color('red')
    s(100)
    t.end_fill()

s = turtle.Screen()
s.onscreenclick(drawit)
