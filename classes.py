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
        self.branches = []

    def generateBranches(self):
        for i in range(0,7):
            newState = GameState(self.state)

            if role == "min":
                newState.updateState(1, i)
            else:
                newState.updateState(2, i)

            self.branches.append(Node(newState, self.depth + 1, "min" if self.role == "max" else "max"))

class GameState:
    __init__(self, state = None, rows = None, cols = None)):
        if state is None:
            self.state = numpy.zeros((rows, cols))
            self.rows = rows
            self.cols = rows
        else:
            self.state = state.copy()
            self.rows = state.shape[0]
            self.cols = state.shape[1]

    def updateState(self, player, col):
        row = numpy.count_nonzero(self.state[:,col])
        if row >= self.rows:
            return None
        self.state[row, col] = player
        self.score = self.evaluateState()
        return self.state.copy()

    def evaluateState(self):
        self.score = eval.evaluateGameState(self.state, 2)
        return self.score
