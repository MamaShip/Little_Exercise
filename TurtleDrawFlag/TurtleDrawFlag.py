import turtle
from time import sleep
def drawStar(x,y):
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(10)
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
    drawRectangle(0,-(i*14),14,340)
    turtle.fill(False)

turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.fill(True)
drawRectangle(0,0,98,170)
turtle.fill(False)
turtle.pencolor('white')
for j in range(10,100,30):
    for i in range(5,170,25):
        print i,j
        turtle.fillcolor('white')
        turtle.fill(True)
        drawStar(i,-j)
        turtle.fill(False)

for j in range(25,100,30):
    for i in range(18,160,25):
        print i,j
        turtle.fillcolor('white')
        turtle.fill(True)
        drawStar(i,-j)
        turtle.fill(False)

turtle.goto(-20,20)
sleep(20)
