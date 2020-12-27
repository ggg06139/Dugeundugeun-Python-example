import turtle

def tree(length):
    if length>5:
        t.fd(length)
        t.right(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.right(20)
        t.backward(length)

t =turtle.Turtle()
t.shape('turtle')
t.lt(90)
t.color('green')
tree(90)
