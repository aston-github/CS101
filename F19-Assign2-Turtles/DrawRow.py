'''
DrawRow.py

@author: ASTON YONG
'''
from TurtleShapes import drawOneShape, drawOneIceCream

import turtle, BoundingBox

def drawRowsOfRows(turt, func):
    '''Draws 10 rows of 10 ice cream cones of 
    increasing size'''
    size = 5
    y=-200
    for i in range(10):
        size +=1
        turt.up()
        x=-300
        turt.goto(x,y)
        turt.down()
        for i in range(10):
            turt.up()
            turt.goto(x,y)
            turt.setheading(0)
            turt.down()
            func(turt, size)
            x+=size*2
        y+=size*2

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    t = turtle.Turtle()
    t.speed(0)    
    drawRowsOfRows(t, drawOneIceCream)
    win.exitonclick()
    