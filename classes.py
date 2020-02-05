import numpy
from evaluate import SpaceState
from evaluate import findColOfDifference
'''from evaluate import evaluateGameState'''
import evaluator as ev
import operator
from alphabeta import alphaBeta
import time

class ConnectFourPlayer:

    def __init__(self, playerNumber = 1, rows = 6, cols = 7, maxDepth = 4): #, initialState):
        #self.initialState = initialState
        self.evaluator = ev.evaluator()
        if playerNumber == 1:
            self.root = Node(GameState(rows=rows,cols=cols), True, self.evaluator)
        elif playerNumber == 2:
            self.root = Node(GameState(rows=rows,cols=cols), False, self.evaluator)
        else:
            raise Exception('playerNumber must be 1 or 2')
        self.maxDepth = maxDepth

    def findBestMove(self):
        if self.root.isMaximizer:
            minimaxScores = self.root.getMinimaxScoresOfChildren(self.maxDepth)
        else:
            raise Exception("Root of tree is minimizer (i.e. it is the opponent's turn). " + \
                "Best move cannot be computed.")

        # return numpy.argmax(minimaxScores)

        # Find column where child state matrix differs from current state matrix
        idx = numpy.argmax(minimaxScores)
        return findColOfDifference(self.root.children[idx].state.data, self.root.state.data)


    def move(self,col = None):
        if col is None:
            col = self.findBestMove()
            shouldReturn = True
        else:
            shouldReturn = False
        if len(self.root.children)==0:
            self.root.generateChildNodes()
        raiseExc = True
        for c in self.root.children:
            if findColOfDifference(c.state.data, self.root.state.data) == col:
                raiseExc = False
                self.root = c
                break
        if raiseExc:
            raise Exception('Move is not valid')

        #FOR DEBUGGING:
        #print(self.root.state.data)
        #print()
        if shouldReturn:
            return col


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
            #else:
            #    self.children.append(None)
        allScores = [c.evalScore for c in self.children]
        self.orderToSearch = sorted(range(len(self.children)), key=allScores.__getitem__)
        # self.children.sort(key=operator.attrgetter('evalScore'),reverse=True)

    def getMinimaxScoresOfChildren(self,maxDepth):
        outFile = open("data.txt", "a")
        start = time.time()
        scores = []
        if len(self.children) == 0:
            self.generateChildNodes()
        totalNumNodesVisited = 0
        for i in range(len(self.children)):
            (score, numNodesVisited) = alphaBeta(self.children[i], maxDepth-1, -numpy.inf, numpy.inf, True)
            scores.append(score)
            totalNumNodesVisited += numNodesVisited
        taken = time.time() - start
        outFile.write(str(taken) + " " + str(totalNumNodesVisited) + "\n")
        outFile.close()
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
        row = numpy.count_nonzero(self.data[:,col] != SpaceState.EMPTY)
        if row >= self.shape[0]:
            return False
        self.data[row, col] = player
        return True

    """def evaluateState(self):
        self.score = eval.evaluateGameState(self.state, SpaceState.SELF)
        return self.score"""
