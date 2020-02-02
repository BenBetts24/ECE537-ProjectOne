''' 
Based on psuedocode from:
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
'''

import numpy

# function alphabeta(node, depth, α, β, maximizingPlayer) is
def alphaBeta(node, depth, alpha, beta):
#   if depth = 0 or node is a terminal node then
    if depth == 0 or node.isTerminal:
#       return the heuristic value of node
        return node.evalScore
#   if maximizingPlayer then
    if node.isMaximizer:
#       value := −∞
        value = -numpy.inf
#       for each child of node do
        if len(node.children) == 0:
            node.generateChildNodes()
        for childIdx in range(len(node.children)):
#           value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            value = max(value, alphaBeta(node.chidlren[childIdx], depth-1, alpha, beta))
#           α := max(α, value)
            alpha = max(alpha, value)
#           if α ≥ β then
            if alpha >= beta:
#               break (* β cut-off *)
                break
#       return value
        return value

#   else
    else:
#       value := +∞
        value = numpy.inf
#       for each child of node do
        if len(node.children) == 0:
            node.generateChildNodes()
        for childIdx in range(len(node.children)):
#           value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            value = min(value, alphaBeta(node.children[childIdx], depth-1, alpha, beta))
#           β := min(β, value)
            beta = min(beta, value)
#           if α ≥ β then
            if alpha >= beta:
#               break (* α cut-off *)
                break
#       return value
        return value