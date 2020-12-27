import turtle as t

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t.bgcolor('black')
t.speed(0)
t.width(4)

l = 10

while l < 500:
    t.fd(l)
    t.pencolor(colors[l%6])
    t.rt(89)
    l +=5
