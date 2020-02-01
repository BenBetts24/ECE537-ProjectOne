import numpy

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
    __init__(self, rows, cols)):
        self.state = numpy.zeros((rows, cols))
        self.rows = rows
        self.cols = cols

    def updateState(self, player, col):
        row = numpy.count_nonzero(self.state[:,col])
        if row >= self.rows:
            return None
        self.state[row, col] = player
