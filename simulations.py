import time as timer
from datetime import datetime

def weightedAverage(old, new, total):
    oldWeight = (total - 1) / total
    newWeight = 1 / total
    return (oldWeight * old) + (newWeight * new)

def writeToFile(moves, times, nodes, gameNum, name):
    print("Writing to file...")

    # Overwrites existing file, file updated after every game
    outFile = open(name, "w")

    # Output semicolon separated for easy parsing later on
    for move in moves.keys():
        outFile.write(str(move) + ";" + str(moves[move]) + ";" + str(times[move]) + ";" + str(nodes[move]) + "\n")

    print("done")
    timer.sleep(3)

# Creating dictionaries to store move data
averageTimes = {} # Avg time spend on each move
averageNodes = {} # Avg nodes visited
moveCounts = {} # How many times that move has been played
gameNum = 0
fileName = "SimulationData/SimData-" + str(datetime.now())

while True:
    gameNum += 1

    # The next game to be run from which data will be collected
    print("Starting game " + str(gameNum))
    exec(open("./connectFourComp.py").read())

    # Keeping track of which move is being played
    computerOne = True
    moveNum = 0

    # Grabbing data from the game that was just simulated
    input = open("data.txt", "r")
    while True:
        if computerOne:
            computerOne = False
            moveNum += 1
        else:
            computerOne = True

        lineIn = input.readline()

        if lineIn != "":
            line = lineIn.split()
            time = float(line[0])
            nodes = float(line[1])

            if moveNum in moveCounts.keys():
                moveCounts[moveNum] += 1
            else:
                moveCounts[moveNum] = 1

            if moveNum in averageTimes.keys():
                averageTimes[moveNum] = weightedAverage(averageTimes[moveNum], time, moveCounts[moveNum])
            else:
                averageTimes[moveNum] = time

            if moveNum in averageNodes.keys():
                averageNodes[moveNum] = weightedAverage(averageNodes[moveNum], nodes, moveCounts[moveNum])
            else:
                averageNodes[moveNum] = nodes

        else:
            print("Finished reading data")
            break

    # Once data has been added to dicts, overwrite old file
    writeToFile(moveCounts, averageTimes, averageNodes, gameNum, fileName)
