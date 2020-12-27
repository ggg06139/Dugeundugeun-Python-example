from tkinter import *

mycolor = 'blue'

def paint(event):
    x1, y1 = (event.x-1),(event.y+1)
    x2, y2 = (event.x-1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2, fill = mycolor)
def change_red():
    global mycolor
    mycolor = 'red'

def change_green():
    global mycolor
    mycolor = 'green'

def change_purple():
    global mycolor
    mycolor = 'purple'

window = Tk()

canvas = Canvas(window)
canvas.pack()
canvas.bind('<B1-Motion>',paint)
button1 = Button(window, text='빨간색', command = change_red)
button1.pack()
button2 = Button(window, text='초록색', command = change_green)
button2.pack()
button3 = Button(window, text='보라색', command = change_purple)
button3.pack()

window.mainloop()
