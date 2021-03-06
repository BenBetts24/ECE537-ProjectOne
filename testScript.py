import classes as c

# maxDepth can't be much more than 4 or else it will take too long
gt = c.GameTree(maxDepth = 3)
print(gt.root.state.data)
print(gt.root.evalScore)

# Call move() without any arguments to calculate the best move using the alpha-beta pruning algorithm. 
gt.move()
# In printing, 1 represents self, -1 represents opponent
print(gt.root.state.data)
print(gt.root.evalScore)

# Call move() with an input argument to tell the game tree where to advance
gt.move(2)
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move()
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move(3)
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move()
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move(3)
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move()
print(gt.root.state.data)
print(gt.root.evalScore)

