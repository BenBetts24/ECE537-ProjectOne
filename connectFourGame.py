from graphics import *
import evaluate as e
import numpy

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

def updateGameState(player,col,gameState):
    row = numpy.count_nonzero(gameState[:,col])
    if row >= NUM_ROWS:
        return None
    gameState[row,col] = player
    return gameState



win = GraphWin("Window",WIN_WIDTH,WIN_HEIGHT)

rect = Rectangle(Point(0,0),Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE))
rect.setOutline("blue")
rect.setFill("blue")
rect.draw(win)

rect = Rectangle(Point(NUM_COLS*GRID_SIZE,NUM_ROWS*GRID_SIZE),Point(WIN_WIDTH,WIN_HEIGHT))
rect.setOutline("white")
rect.setFill("white")
rect.draw(win)

gameState = numpy.zeros((NUM_ROWS,NUM_COLS))

for rowIdx in range(NUM_ROWS):
    for colIdx in range(NUM_COLS):
        cir = Circle(Point((colIdx+0.5)*GRID_SIZE,(rowIdx+0.5)*GRID_SIZE),0.35*GRID_SIZE)
        cir.setOutline("black")
        cir.setFill("white")
        cir.draw(win)


isPlayer1 = True

while True:
    try:
        pt = win.getMouse()
    except:
        break
    if pt.getY() > NUM_ROWS*GRID_SIZE:
        win.close()
        break
    else:
        col = int(pt.getX()/GRID_SIZE)
        row = numpy.count_nonzero(gameState[:,col])
        if row >= NUM_ROWS:
            continue
        if isPlayer1:
            player = 1
            gameState[row,col] = 1
            color = "red"
            isPlayer1 = False
            drawPiece(row,col,color,win)

        else:
            player = 2
            gameState[row,col] = 2
            color = "yellow"
            isPlayer1 = True
            drawPiece(row,col,color,win)
    msg = "%.2f" % e.evaluateGameState(gameState,1)
    print(msg)


