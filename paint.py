import turtle

t = turtle
t.setup(700,600)
t.title("paint app")

def forward():
    t.forward(10)
def back():
    t.back(10)
def right():
    t.right(10)
def left():
    t.left(10)

def red():
    t.pencolor("red")

def blue():
    t.pencolor("blue")

def black():
    t.pencolor("black")
    
def white():
    t.pencolor("white")
def green():
    t.pencolor("green")
def yellow():
    t.pencolor("yellow")

def clear():
    t.clear()

def square():
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    

def penup():
    t.penup()
def pendown():
    t.pendown()

t.onkey(forward, "Up")
t.onkey(back, "Down")
t.onkey(right, "Right")
t.onkey(left, "Left")
t.onkey(blue, "q")
t.onkey(black, "b")
t.onkey(white, "w")
t.onkey(red, "r")
t.onkey(green, "g")
t.onkey(yellow, "y")
t.onkey(clear, "Delete")
t.onkey(square, "1")
t.onkey(penup, "u")
t.onkey(pendown, "d")


t.listen()
t.mainloop()
