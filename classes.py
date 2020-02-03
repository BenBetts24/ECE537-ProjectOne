import numpy
from evaluate import SpaceState
'''from evaluate import evaluateGameState'''
import evaluator as ev
import operator
from alphabeta import alphaBeta

class GameTree:
    
    def __init__(self, rows = 6, cols = 7, maxDepth = 4): #, initialState):
        #self.initialState = initialState
        self.evaluator = ev.evaluator()
        self.root = Node(GameState(rows=rows,cols=cols), True, self.evaluator)
        self.maxDepth = maxDepth
    
    def findBestMove(self):
        if self.root.isMaximizer:
            minimaxScores = self.root.getMinimaxScoresOfChildren(self.maxDepth)
        else:
            raise Exception("Root of tree is minimizer (i.e. it is the opponent's turn). " + \
                "Best move cannot be computed.")
        return numpy.argmax(minimaxScores)
    
    def move(self,col = None):
        if col is None:
            col = self.findBestMove()
        self.root = self.root.children[col]


class Node:
    def __init__(self, state, isMaximizer, evaluator=None):
        self.state = state
        if evaluator is not None:
            self.evaluator = evaluator
        else:
            self.evaluator = ev.evaluator()
        self.updateEvalScore()
        # self.depth = depth
        self.isMaximizer = isMaximizer
        self.isTerminal = (self.evalScore == numpy.inf) or \
            (self.evalScore == -numpy.inf) or \
            (numpy.count_nonzero(self.state.data) == numpy.size(self.state.data))
        self.children = []
        self.orderToSearch = []
    
    def updateEvalScore(self):
        self.evalScore = self.evaluator.evaluate(self.state.data)

    def generateChildNodes(self):
        if self.evalScore == numpy.inf or self.evalScore == -numpy.inf:
            return
        for i in range(0,self.state.shape[1]):            
            newState = GameState(data=numpy.copy(self.state.data))

            if self.isMaximizer:
                isValid = newState.updateState(SpaceState.SELF, i)
            else:
                isValid = newState.updateState(SpaceState.OPPONENT, i)
            if isValid:
                self.children.append(Node(newState, not self.isMaximizer, self.evaluator))
        
        allScores = [c.evalScore for c in self.children]
        self.orderToSearch = sorted(range(len(self.children)), key=allScores.__getitem__)
        # self.children.sort(key=operator.attrgetter('evalScore'),reverse=True)

    def getMinimaxScoresOfChildren(self,maxDepth):
        scores = []
        if len(self.children) == 0:
            self.generateChildNodes()
        for i in range(len(self.children)):
            scores.append(alphaBeta(self.children[i], maxDepth-1, -numpy.inf, numpy.inf))
        return scores


class GameState:
    def __init__(self, data = None, rows = None, cols = None):
        if data is None:
            self.data = numpy.zeros((rows, cols))
            self.shape = [rows, cols]
        else:
            self.data = data
            self.shape = data.shape

    def updateState(self, player, col):
        row = numpy.count_nonzero(self.data[:,col])
        if row >= self.shape[0]:
            return False
        self.data[row, col] = player
        return True

    """def evaluateState(self):
        self.score = eval.evaluateGameState(self.state, SpaceState.SELF)
        return self.score"""


# print("Test")
