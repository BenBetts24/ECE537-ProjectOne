from graphics import *
import numpy
from classes import ConnectFourPlayer

def keepWindowOpen(w):
    while True:
        try:
            w.getMouse()
        except:
            break

COMP_IS_PLAYER_ONE = False

NUM_ROWS = 6
NUM_COLS = 7
GRID_SIZE = 100
BOTTOM_PAD = 100

WIN_HEIGHT = NUM_ROWS*GRID_SIZE + BOTTOM_PAD
WIN_WIDTH = NUM_COLS*GRID_SIZE


def drawPiece(r,c,color,window):
    r = NUM_ROWS-r-1
    cir = Circle(Point((c+0.5)*GRID_SIZE,(r+0.5)*GRID_SIZE),0.35*GRID_SIZE)
    cir.setFill(color)
    cir.setOutline("black")
    cir.draw(window)

win = GraphWin("Window",WIN_WIDTH,WIN_HEIGHT)

rect = Rectangle(Point(0,0),Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE))
rect.setOutline("blue")
rect.setFill("blue")
rect.draw(win)

rect = Rectangle(Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE),Point(WIN_WIDTH,WIN_HEIGHT))
rect.setOutline("white")
rect.setFill("white")
rect.draw(win)

numFilled = numpy.zeros((NUM_COLS,1))

for rowIdx in range(NUM_ROWS):
    for colIdx in range(NUM_COLS):
        cir = Circle(Point((colIdx+0.5)*GRID_SIZE,(rowIdx+0.5)*GRID_SIZE),0.35*GRID_SIZE)
        cir.setOutline("black")
        cir.setFill("white")
        cir.draw(win)

c4p = ConnectFourPlayer(1 if COMP_IS_PLAYER_ONE else 2)

color = "red"
isComputersTurn = COMP_IS_PLAYER_ONE

while True:

    if isComputersTurn:
        col = c4p.move()

    else:
        while True:
            try:
                pt = win.getMouse()
            except:
                break
            if pt.getY() > NUM_ROWS*GRID_SIZE:
                continue
            else:
                col = int(pt.getX()/GRID_SIZE)
                c4p.move(col)
                break

    row = numFilled[col]
    if row >= NUM_ROWS:
        continue
    isComputersTurn = not isComputersTurn
    drawPiece(row,col,color,win)
    color = "yellow" if color=="red" else "red" 

    numFilled[col] += 1

    # Check whether someone has won:
    score = c4p.root.evalScore

    if score == numpy.inf:
        print("You lose!")
        break
    elif score == -numpy.inf:
        print("You win!")
        break

keepWindowOpen(win)
