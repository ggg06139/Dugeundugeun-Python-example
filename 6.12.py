import math
import turtle as t
t.shape('turtle')
t.color('red')

for i in range(361):
    sine = math.sin(3.14*i/180)
    t.goto(i,sine*100)
