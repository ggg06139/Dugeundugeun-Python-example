import random
import turtle as t

t.shape('turtle')

for _ in range(30):
    l = random.randint(1,100)
    t.fd(l)
    a = random.randint(-180,180)
    t.lt(a)
