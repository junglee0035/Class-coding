import graphics
import random
win=graphics.GraphWin("Exercise 7",500,500)
win.setBackground("black")
for i in range(1):
    x= 250
    y= 250
    z= 50
    point = graphics.Point(x,y)
    circle=graphics.Circle(point,z)
    colour=graphics.color_rgb(random.randint(0,255),
                              random.randint(0,255),
                              random.randint(0,255))
    circle.setFill(colour)
    circle.draw(win)
win.getMouse()
win.close()