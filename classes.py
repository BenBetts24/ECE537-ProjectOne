import numpy
import evaluate as eval
import operator
import enum
import alphabeta as ab

class SpaceState(enum.Enum):
    EMPTY = 0
    SELF = 1
    OPPONENT = 2

class GameTree:
    def __init__(self, maxDepth = None): #, initialState):
        #self.initialState = initialState
        self.root = Node(GameState, True)
        if maxDepth is None:
            self.maxDepth = 8
        else:
            self.maxDepth = maxDepth
    
    def findBestMove(self):
        if self.root.isMaximizer:
            minimaxScores = self.root.getMinimaxScoresOfChildren(self.maxDepth)
        else:
            raise Exception("Root of tree is minimizer. Best move cannot be computed.")
        return numpy.argmax(minimaxScores)
    
    def move(self,col = None):
        if col is None:
            col = self.findBestMove()
        self.root = self.root.children[col]


class Node:
    def __init__(self, state, isMaximizer):
        self.state = state
        self.updateEvalScore()
        # self.depth = depth
        self.isMaximizer = isMaximizer
        self.isTerminal = (self.evalScore == numpy.inf) or \
            (self.evalScore == -numpy.inf) or \
            (numpy.count_nonzero(self.state.data) == numpy.size(self.state.data))
        self.children = []
    
    def updateEvalScore(self):
        self.evalScore = eval.evaluateGameState(self.state, SpaceState.SELF)

    def generateChildNodes(self):
        if self.evalScore == numpy.inf or self.evalScore == -numpy.inf:
            return
        for i in range(0,self.state.cols):            
            newState = GameState(data=self.state.data)

            if self.isMaximizer:
                isValid = newState.updateState(SpaceState.SELF, i)
            else:
                isValid = newState.updateState(SpaceState.OPPONENT, i)
            if isValid:
                self.children.append(Node(newState, not self.isMaximizer))

        self.children.sort(key=operator.attrgetter('evalScore'))

    def getMinimaxScoresOfChildren(self,maxDepth):
        scores = []
        for i in range(len(self.children)):
            scores.append(ab.alphaBeta(self.children[i], maxDepth-1, -numpy.inf, numpy.inf))
        return scores


class GameState:
    def __init__(self, data = None, rows = None, cols = None):
        if data is None:
            self.data = numpy.zeros((rows, cols))
            self.rows = rows
            self.cols = cols
        else:
            self.data = data
            self.rows = data.shape[0]
            self.cols = data.shape[1]

    def updateState(self, player, col):
        row = numpy.count_nonzero(self.data[:,col])
        if row >= self.rows:
            return False
        self.data[row, col] = player
        return True

    """def evaluateState(self):
        self.score = eval.evaluateGameState(self.state, SpaceState.SELF)
        return self.score"""


# print("Test")
