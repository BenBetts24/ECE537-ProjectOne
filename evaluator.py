from evaluate import evaluateGameState
from evaluate import SpaceState
import numpy

class evaluator:

    def __init__(self):
        self.seenStates = dict()

    def evaluate(self,gameStateMatrix):
        # convert gameStateMatrix to a unique string
        gs = numpy.copy(gameStateMatrix)
        keyString = ""
        for colIdx in range(gs.shape[1]):
            for rowIdx in range(gs.shape[0]):
                if gs[rowIdx,colIdx]==SpaceState.SELF:
                    keyString += "s"
                elif gs[rowIdx,colIdx]==SpaceState.OPPONENT:
                    keyString += "o"
                else:
                    break
            if colIdx != gs.shape[1]:
                keyString += " "
        
        # If keyString is found in seenStates, return already-calculated evluation score
        if keyString in self.seenStates:
            return self.seenStates[keyString]

        # Else compute evaluation score and append to seenStates
        else:
            evalScore = evaluateGameState(gs)
            self.seenStates[keyString] = evalScore
            return evalScore



    