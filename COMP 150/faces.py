from graphics import *
import time

def makeFace(center, win):
    win.getMouse()
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    win.getMouse()

    eye1Center = center.clone()
    eye1Center.move(-10, 5)
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    win.getMouse()

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)

    win.getMouse()

    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)
    win.getMouse()

    noseTop = center.clone()
    noseTop.move(0, 0)
    noseLeft = noseTop.clone()
    noseLeft.move(-5, -5)
    noseRight = noseLeft.clone()
    noseRight.move(10, 0)
    nose = Polygon(noseTop, noseLeft, noseRight)
    nose.draw(win)
    win.getMouse()

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
    win.getMouse()

    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]

def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp() # make right side up coordinates!
    win.setCoords(0, 0, 200, 150)

    click = 0
    while click > 6:
        position = win.getMouse()
        centerX = position.getX()
        centerY = position.getY()
        face = makeFace(Position, win)
        click += 1

    faceList = makeFace(Point(40, 100), win)
    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05

    win.promptClose(win.getWidth()/2, 20)

main()