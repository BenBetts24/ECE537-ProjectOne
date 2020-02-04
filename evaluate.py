import numpy

class SpaceState:
    EMPTY = 0
    SELF = 1
    OPPONENT = -1

def findColOfDifference(A,B):
    coord = numpy.argwhere(numpy.not_equal(A,B))
    col = coord[0,1]
    return col

def evaluateGameState(gameState):
    return sumPaths(gameState,SpaceState.SELF)-sumPaths(gameState,SpaceState.OPPONENT)


def sumPaths(gameState,player):
    #pieceCoords = numpy.argwhere(gameState==player)
    totalScore = 0
    numRows, numCols = gameState.shape
    # iterate through all possible paths of 4
    # start with vertical
    for startRow in range(numRows-3):
        for startCol in range(numCols):
            pathCoords = numpy.array([[startRow,startCol],[startRow+1,startCol],[startRow+2,startCol],[startRow+3,startCol]])
            pathScore = getPathScore(pathCoords,gameState,player)
            if pathScore == numpy.inf or pathScore == -numpy.inf:
                return pathScore
            else:
                totalScore += pathScore
    # horizontal
    for startRow in range(numRows):
        for startCol in range(numCols-3):
            pathCoords = numpy.array([[startRow,startCol],[startRow,startCol+1],[startRow,startCol+2],[startRow,startCol+3]])
            pathScore = getPathScore(pathCoords,gameState,player)
            if pathScore == numpy.inf or pathScore == -numpy.inf:
                return pathScore
            else:
                totalScore += pathScore
    # diagonals
    for startRow in range(numRows-3):
        for startCol in range(numCols-3):
            # bottom left to top right
            pathCoords = numpy.array([[startRow,startCol],[startRow+1,startCol+1],[startRow+2,startCol+2],[startRow+3,startCol+3]])
            pathScore = getPathScore(pathCoords,gameState,player)
            if pathScore == numpy.inf or pathScore == -numpy.inf:
                return pathScore
            else:
                totalScore += pathScore
            # top left to bottom right
            pathCoords = numpy.array([[startRow+3,startCol],[startRow+2,startCol+1],[startRow+1,startCol+2],[startRow,startCol+3]])
            pathScore = getPathScore(pathCoords,gameState,player)
            if pathScore == numpy.inf or pathScore == -numpy.inf:
                return pathScore
            else:
                totalScore += pathScore

    return totalScore

def getPathScore(pc,gs,pl):
    exp = 2
    score = 0
    for coord in pc:
        if gs[coord[0],coord[1]] == SpaceState.EMPTY:
            n = coord[0] - numpy.count_nonzero(gs[:,coord[1]])
            score += 0.2**(n+1)
        elif gs[coord[0],coord[1]] == pl:
            score += 1
    if score == 0:
        return -numpy.inf
    elif score == 4:
        return numpy.inf
    return score**exp