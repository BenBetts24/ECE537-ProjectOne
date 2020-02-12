import os
import sys
import numpy
from random import seed
from random import randint

from graphics import *

from classes import ConnectFourPlayer

from getConfiguration import *


def keepWindowOpen(w):
    while True:
        try:
            w.getMouse()
        except:
            break

def drawPiece(r,c,color,window):
    r = NUM_ROWS-r-1
    fall = 1.0
    
    while fall >= 0.0025:
        cir = Circle(Point((c+0.5)*GRID_SIZE,(r+0.5)*GRID_SIZE-(10-r)*GRID_SIZE*fall*fall),0.35*GRID_SIZE)
        cir.setFill(color)
        cir.setOutline("black")
        cir.draw(window)
        fall = fall - 0.05
        cir.undraw()
    
    cir = Circle(Point((c+0.5)*GRID_SIZE,(r+0.5)*GRID_SIZE),0.35*GRID_SIZE)
    cir.setFill(color)
    cir.setOutline("black")
    cir.draw(window)


COMP_IS_PLAYER_ONE = False

NUM_ROWS = 6
NUM_COLS = 7
GRID_SIZE = 100
BOTTOM_PAD = 10

WIN_HEIGHT = NUM_ROWS*GRID_SIZE + BOTTOM_PAD
WIN_WIDTH = NUM_COLS*GRID_SIZE


# Start/Settings Window
settings = getConfiguration()

if settings["player1"] == "CPU":
    COMP_IS_PLAYER_ONE = True
elif settings["player1"] == "User":
    COMP_IS_PLAYER_ONE = False

prune = True
if settings["algorithm"] == "alphabeta":
    pruning = True
elif settings["algorithm"] == "minimax":
    pruning = False


# Game Window
win = GraphWin("Connect4",WIN_WIDTH,WIN_HEIGHT)

# Board Graphic
boardColor = settings["boardStyle"]
if boardColor == "Clay":
    boardColor = "Indian Red"
if boardColor != "Wood":
    rect = Rectangle(Point(0,0),Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE))
    rect.setOutline(boardColor)
    rect.setFill(boardColor)
    rect.draw(win)
else:
    # custom background
    woodBkgnd = Image(Point(NUM_COLS*GRID_SIZE/2,NUM_ROWS*GRID_SIZE/2),'woodBkgnd.png')
    woodBkgnd.draw(win)

# Base Layer
rect = Rectangle(Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE),Point(WIN_WIDTH,WIN_HEIGHT))
rect.setOutline("white")
rect.setFill("white")
rect.draw(win)

numFilled = numpy.zeros((NUM_COLS,1))

# Backdrop
for rowIdx in range(NUM_ROWS):
    for colIdx in range(NUM_COLS):
        cir = Circle(Point((colIdx+0.5)*GRID_SIZE,(rowIdx+0.5)*GRID_SIZE),0.35*GRID_SIZE)
        cir.setOutline("black")
        cir.setFill("Moccasin")
        cir.draw(win)

# CPU vs CPU gameplay
if settings["player1"] == "CPU" and settings["player2"] == "CPU":
    cOne = ConnectFourPlayer(1)
    cTwo = ConnectFourPlayer(2)
    color = settings["player1color"]
    isComputerOne = True
    counter = 0
    gameWon = False

    while True and not gameWon:

        if counter > 3:
            if isComputerOne:
                col = cOne.move(pruning = pruning)
                cTwo.move(col)
            else:
                col = cTwo.move(pruning = pruning)
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
        color = settings["player2color"] if color==settings["player1color"] else settings["player1color"] #"yellow" if color=="red" else "red" 

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

# USER vs CPU gameplay
else:
    c4p = ConnectFourPlayer(1 if COMP_IS_PLAYER_ONE else 2)
    color = settings["player1color"]
    isComputersTurn = COMP_IS_PLAYER_ONE

    while True:

        if isComputersTurn:
            col = c4p.move(pruning=pruning)
            row = numFilled[col]

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
                    row = numFilled[col]
                    if row >= NUM_ROWS:
                        continue
                    c4p.move(col)
                    break

        
        isComputersTurn = not isComputersTurn
        drawPiece(row,col,color,win)
        color = settings["player2color"] if color==settings["player1color"] else settings["player1color"] #"yellow" if color=="red" else "red" 

        numFilled[col] += 1

        # Check whether someone has won:
        score = c4p.root.evalScore

        if score == numpy.inf:
            print("You lose!")
            replayWin = GraphWin("You lose!",200,50)
            break
        elif score == -numpy.inf:
            print("You win!")
            replayWin = GraphWin("You win!",200,50)
            break
        elif numpy.all(numFilled==NUM_ROWS):
            print("It's a tie!")
            replayWin = GraphWin("It's a tie!",200,50)
            break

replayText = Text(Point(100,25),"PLAY AGAIN")
replayText.setSize(18)
replayText.setFace("arial")
replayText.setTextColor("Royal Blue")
replayText.setStyle("bold")
replayText.draw(replayWin)
replay = False
while replay == False:
    clickR = replayWin.getMouse()
    if clickR.getX()>0 and clickR.getX()<200 and clickR.getY()>0 and clickR.getY()<50:
        replayText.setTextColor("Light Blue")
        replayWin.close()        
        replay = True

if replay == True:
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

keepWindowOpen(win)
