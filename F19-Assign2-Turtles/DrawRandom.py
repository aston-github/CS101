'''
DrawRandom.py

@author: ASTON YONG
'''
import turtle, BoundingBox
import random
from TurtleShapes import drawOneShape, drawOneIceCream

def drawEverywhere(turt, func):
    '''Draws squares or ice cream cones of 
    random size at random coordinates'''
    str_num = input('Input number of drawings wanted: ')
    int_num = int(str_num)    
    for i in range(int_num):
        x= random.randint(-300,300)
        y= random.randint(-150,150)
        turt.up()
        turt.goto(x,y)
        turt.down()
        size = random.randint(7,15)
        func(turt,size)
        
    
    
if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    t = turtle.Turtle()
    t.speed(0)

    str_func = input("Input 0 for drawOneShape, 1 for drawOneIceCream: ")
    int_func = int(str_func)
    if int_func == 0:
        drawEverywhere(t, drawOneShape)
    elif int_func == 1:
        drawEverywhere(t, drawOneIceCream)
      
      
    win.exitonclick()
    