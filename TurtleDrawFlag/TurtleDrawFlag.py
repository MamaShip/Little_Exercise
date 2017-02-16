import turtle
from time import sleep
def drawStar(x,y):
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(4)
        turtle.left(72)
        turtle.forward(4)
        turtle.right(144)
    turtle.penup()
def drawRectangle(x,y,chang,kuan):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(kuan)
    turtle.right(90)
    turtle.forward(chang)
    turtle.right(90)
    turtle.forward(kuan)
    turtle.right(90)
    turtle.forward(chang)
    turtle.right(90)
    turtle.penup()

#drawRectangle(0,0,182,340)
turtle.pencolor('red')
for i in range(0,13,2):
    turtle.fillcolor('red')
    turtle.fill(True)
    drawRectangle(0,-(i*20),20,440)
    turtle.fill(False)

turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.fill(True)
drawRectangle(0,0,140,220)
turtle.fill(False)

turtle.pencolor('white')
for j in range(8,140,30):
    for i in range(15,220,35):
        print i,j
        turtle.fillcolor('white')
        turtle.fill(True)
        drawStar(i,-j)
        turtle.fill(False)

for j in range(23,140,30):
    for i in range(32,200,35):
        print i,j
        turtle.fillcolor('white')
        turtle.fill(True)
        drawStar(i,-j)
        turtle.fill(False)

turtle.goto(-20,20)
sleep(20)
