import turtle as t
import random as r

def randomColor():
    t.colormode(255)
    re = r.randint(0,255)
    g = r.randint(0,255)
    b = r.randint(0,255)
    return(re,g,b)

def move():
    t.setheading(360)
    t.forward(10)

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def back():
    t.setheading(180)
    t.forward(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

sindex = 0
def shapes():
    global sindex
    shape = ['turtle','arrow','square','circle','classic']
    t.shape(shape[sindex])
    sindex= (sindex+1)%5

def colorchange():
    t.color(randomColor())


mywidth = 5
def increase():
    global mywidth
    mywidth += 5
    t.width(mywidth)

def decrease():
    global mywidth
    mywidth -= 5
    t.width(mywidth)

def circle():
    t.setheading(t.heading()+10)
    t.forward(10)

size = 2
def sizeadd():
    global size
    t.shapesize(size+1)
    size+=1

def sizesub():
    global size
    t.shapesize(size+1)
    size-=1

screen = t.Screen()
screen.listen()
screen.onkeypress(move,'Right')
screen.onkeypress(up,'Up')
screen.onkeypress(down,'Down')
screen.onkeypress(back,'Left')
screen.onkeypress(shapes,'space')
screen.onkeypress(clear,'c')
screen.onkeypress(t.penup,'u')
screen.onkeypress(t.pendown,'d')
screen.onkeypress(colorchange,'x')
screen.onkeypress(increase,'w')
screen.onkeypress(decrease,'s')
screen.onkeypress(circle,'b')
screen.onkeypress(sizeadd,'r')
screen.onkeypress(sizesub,'f')

screen.mainloop()


