import turtle as t
t.shape('turtle')

for _ in range(3):
    t.fd(100)
    t.lt(360/3)

t.penup()
t.goto(200,0)
t.pendown()

for _ in range(4):
    t.fd(100)
    t.lt(360/4)
