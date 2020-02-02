import classes as c

gt = c.GameTree(maxDepth = 3)
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move()
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move(2)
print(gt.root.state.data)
print(gt.root.evalScore)

gt.move()
print(gt.root.state.data)
print(gt.root.evalScore)