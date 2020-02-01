import numpy
import evaluate as eval

class GameTree:
    __init__(self, initialState):
        self.initialState = initialState
        self.root = Node(self.state, 0, "max")



class Node:
    __init__(self, state, depth, role):
        self.state = state
        self.depth = depth
        self.role = role
        self.branches = numpy.array()

    def generateBranches(self):
        for i in range(0,7):
            newState = state
            self.branches.append(Node())

class GameState:
    __init__(self, state = None, rows = None, cols = None)):
        if state is None:
            self.state = numpy.zeros((rows, cols))
            self.rows = rows
            self.cols = rows
        else:
            self.state = state
            self.rows = state.shape[0]
            self.cols = state.shape[1]

    def updateState(self, player, col):
        row = numpy.count_nonzero(self.state[:,col])
        if row >= self.rows:
            return None
        self.state[row, col] = player
        return self.state

    def evaluateState(self):
        self.score = eval.evaluateGameState(self.state, 2)
        return self.score
