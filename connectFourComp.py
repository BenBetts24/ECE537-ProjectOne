from graphics import *
import numpy
from classes import ConnectFourPlayer
from random import seed
from random import randint

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

cOne = ConnectFourPlayer(1)
cTwo = ConnectFourPlayer(2)
color = "red"
isComputerOne = True
counter = 0
gameWon = False
seed(time.time())

if os.path.exists("data.txt"):
    os.remove("data.txt")

while True and not gameWon:

    if counter > 3:
        if isComputerOne:
            col = cOne.move()
            cTwo.move(col)
        else:
            col = cTwo.move()
            cOne.move(col)
    else:
        col = randint(0,6)
        counter += 1
        if isComputerOne:
            cOne.move(col)
            cTwo.move(col)
        else:
            cTwo.move(col)
            cOne.move(col)


    row = numFilled[col]
    if row >= NUM_ROWS:
        continue
    isComputerOne = not isComputerOne
    drawPiece(row,col,color,win)
    color = "yellow" if color=="red" else "red" 

    numFilled[col] += 1

    # Check whether someone has won:
    score = cOne.root.evalScore

    if score == numpy.inf:
        print("Computer One Wins!")
        time.sleep(3)
        gameWon = True
        break
    elif score == -numpy.inf:
        print("Computer Two Wins!")
        time.sleep(3)
        gameWon = True
        break
    elif numpy.all(numFilled==NUM_ROWS):
        gameWon = True
        print("It's a tie!")
        time.sleep(3)
        break

win.close()
#if not gameWon:
#    keepWindowOpen(win)
