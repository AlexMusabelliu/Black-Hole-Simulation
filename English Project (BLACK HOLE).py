from turtle import Turtle, Screen
import sys, math, colorsys
from random import randint

CURSOR_SIZE = 20


def move(x, y):
    """ has it follow cursor """

    t1.ondrag(None)

    t1.goto(x, y)

    screen.update()

    t1.ondrag(move)

def grow():
    """ grows t1 shape """

    global t1_size, g

    t1_size += 0.1
    t1.shapesize(t1_size / CURSOR_SIZE)
    g -= .1
    t1.color((r/255, g/255, b/255))

    screen.update()

def follow():
    """ has create()'d dots follow t1 """

    global circles, dist, phase, h, s, zx 

    s = 100
    new_circles = []
    

    for (x, y), stamp in circles:
        
        t2.clearstamp(stamp)

        t2.goto(x, y)
        
        #dist = t2.distance(t1) / 57.29577951308232 // 1
        #t2.goto(2 * (t1.xcor() + math.cos(t1.towards(t2))), 2 * (t1.ycor() + math.sin(t1.towards(t2))))

        h = t2.heading()
        t2.forward(1)
        if t2.xcor() >= 900:
            t2.goto(-900, t2.ycor())
        if t2.ycor() >= 900:
            t2.goto(t2.xcor(), -900)
        t2.setheading(t2.towards(t1))
        
        if t2.distance(t1) < t1_size * 20 // 1:
            if t2.distance(t1) > t1_size * 1.1:
                t2.forward(900/t2.distance(t1)//1)
                t2.setheading(t2.heading() + 118)
                t2.forward(5)
            else:
                t2.forward(3)
                
        t2.seth(h)
        if phase == 3:
            zx = t2.distance(t1) / t1_size
            s = s - s * zx
            if zx > 1:
                s = 0
            t2.color(colorsys.hsv_to_rgb(0, s/100, 1))
            
        
                
        
        
        if t2.distance(t1) > t1_size // 2:
            new_circles.append((t2.position(), t2.stamp())) 
        else:
            if phase != 3:
                grow()  # we ate one, make t1 fatter
            
    screen.update()

    circles = new_circles

    if circles:
        screen.ontimer(follow, 10)
    else:
        phase = 1
        produce()

def create():
    """ create()'s dots with t2 """
    global xyz
    count = 0
    nux, nuy = -400, 300

    while nuy > -400:
        t2.goto(nux, nuy)

        if t2.distance(t1) > t1_size // 2:
            xyz = randint(0,360)
            t2.setheading(xyz)
            circles.append((t2.position(), t2.stamp()))

        nux += 20
        count += 1
        if count == 40:
            nuy -= 50
            nux = -400
            count = 0

    screen.update()
    
def quit():
    screen.bye()
    sys.exit(0)

# redraw():
    

def produce():
    #create boundary of star
    global t2_size, ironmax
    t1.ondrag(None)
    t1.ht()
    t2.goto(t1.xcor(), t1.ycor())
    
    t2.color("white")
    t2.shapesize((t1_size + 4) / CURSOR_SIZE)
    t2.stamp()
    
    t2.shapesize((t1_size + 2) / CURSOR_SIZE)
    t2.color("grey")
    t2.stamp()
    
    t2_size = 4
    #t2.color("yellow")
    #start producing helium
    while t2_size < t1_size:
        
        
        t2_size += .3
        
        t2.color("white")
        t2.shapesize((t2_size + t1_size + 4) / CURSOR_SIZE)
        t2.stamp()
        
        t2.shapesize((t2_size + t1_size + 2) / CURSOR_SIZE)
        t2.color("grey")
        t2.stamp()
        
        t2.color("yellow")
        t2.shapesize(t2_size / 20)
        t2.stamp()
        
        screen.update()
        
        ironmax = t2_size
        
    t2_size = 4
    
    while t2_size < ironmax:
        t2.color("white")
        t2.shapesize((ironmax + t1_size + 4) / CURSOR_SIZE)
        t2.stamp()
        
        t2.shapesize((ironmax + t1_size + 2) / CURSOR_SIZE)
        t2.color("black")
        t2.stamp()
        
        t2.shapesize((ironmax + t1_size - t2_size) / CURSOR_SIZE)
        t2.color("grey")
        t2.stamp()
        
        t2.shapesize(ironmax / 20)
        t2.color("yellow")
        t2.stamp()
        
        t2.shapesize(t2_size / 20)
        t2.color("green")
        t2.stamp()
        
        t2_size += .3
        
        screen.update()
    supernova()
    
def supernova():
    global t2_size, ironmax, v, phase
    
    v = 100
    
    while t2_size > 1:
        t2.color("black")
        t2.shapesize((t2_size + t1_size + 4 + 2) / CURSOR_SIZE)
        t2.stamp()
        
        t2.color("white")
        t2.shapesize((t2_size + t1_size + 4) / CURSOR_SIZE)
        t2.stamp()
        
        t2.shapesize((t2_size + t1_size + 2) / CURSOR_SIZE)
        t2.color("black")
        t2.stamp()
        
        t2_size -= 2
        
        
        
        screen.update()
        
    while t2_size < 5000:
        t2.color("white")
        t2.shapesize((t2_size + t1_size + 4) / CURSOR_SIZE)
        t2.stamp()
        
        t2_size += 100
        
        screen.update()
    
    t2.color("black")
    t2.stamp()
    
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(False)
    
    phase = 3
    
    t2.shapesize(4/20)
    t2.color("white")
    
    t1.goto(0,0)
    t1.shapesize(6/20)
    
    #t1.ondrag(move)
    
    screen.update()
    
    create()
    
    follow()
    
    screen.listen()
    screen.onkeypress(quit, "Escape")
    
    screen.mainloop()


def radiate():
    global t2_size
    
# variables
t1_size = 6
circles = []
gat = []
phase = 0


screen = Screen()
screen.screensize(900, 900)
screen.bgcolor("black")
#screen.mode("standard")


t2 = Turtle('turtle', visible=False)
t2.shapesize(4 / CURSOR_SIZE)
t2.speed('fastest')
t2.color('purple')
t2.penup()
t2_size = 4
t2.radians()

t1 = Turtle('turtle')
t1.shapesize(t1_size / CURSOR_SIZE)
t1.speed('fastest')
r = 190
g = 100
b = 190
t1.color((r/255, g/255, b/255))
t1.penup()

t1.ondrag(move)

screen.tracer(False)

screen.listen()
screen.onkeypress(quit, "Escape")

create()
print(circles)
follow()
#print(phase)

screen.mainloop()