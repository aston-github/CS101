'''
TurtleShapes.py

@author: ASTON YONG
'''

import turtle, BoundingBox
import random

def drawOneShape(turt, size):
    '''
    Draws a square with the side length of size
    input
    '''
        
    for i in range(4):
        turt.forward(size)
        turt.right(90)
        
def drawOneIceCream(turt, size):
    '''
    Draws a ice cream cone with
    scoop radius equal to size
    '''
    turt.color('brown')
    turt.forward(size*2)
    turt.right(110)
    turt.forward(size*14/5)
    turt.right(140)
    turt.forward(size*14/5)
    turt.right(110)
    turt.up()
    turt.forward(size*2)
    turt.left(90)
    turt.down()
    turt.color('red')
    turt.up()
    turt.forward(size)   
    turt.down()
    turt.circle(size)
    
    lst = ['blue', 'green']
    for color in lst:
        turt.color(color)
        turt.up()
        turt.forward(size*2)   
        turt.down()
        turt.circle(size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    ## CALL FUNCTIONS HERE
    t = turtle.Turtle()
    size = 60
    t.up()
    t.backward(100)
    t.down()
    drawOneShape(t, size)
    
    i = turtle.Turtle()
    size = 40
    i.up()
    i.forward(100)
    i.down()
    drawOneIceCream(i, size)

    win.exitonclick()
    