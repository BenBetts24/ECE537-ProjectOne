import numpy

def evaluateGameState(gameState,player):
    if player==1:
        me = 1
        opponent = 2
    elif player==2:
        me = 2
        opponent = 1
    else:
        raise Exception("'player' must have value of 1 or 2")
    return sumPaths(gameState,me)-sumPaths(gameState,opponent)


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
    if pl == 1:
        opp = 2
    else:
        opp = 1
    score = 0
    # TODO: If all four pieces are same, return +/- inf
    for coord in pc:
        if gs[coord[0],coord[1]] == opp:
            return 0
        elif gs[coord[0],coord[1]] == pl:
            score += 1
        else:
            n = coord[1] - numpy.count_nonzero(gs[:,coord[1]])
            score += 1/(n+2)
    return score**exp