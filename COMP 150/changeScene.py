import graphics
import random
win=graphics.GraphWin("Exercise 7",500,500)
win.setBackground("dark grey")
for i in range(100):
    win.getMouse()
    x=random.randint(0,500)
    y=random.randint(0,500)
    z=random.randint(1,100)
    point = graphics.Point(x,y)
    circle=graphics.Circle(point,z)
    colour=graphics.color_rgb(random.randint(0,255),
                              random.randint(0,255),
                              random.randint(0,255))
    circle.setFill(colour)
    circle.draw(win)
win.getMouse()
win.close()