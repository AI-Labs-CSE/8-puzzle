import matplotlib.pyplot as plt
import BFS, DFS, Visualizer, Utilities

from AStarSearch.AStar import AStar
from State.State import State

testCases = [125340678, 618402735, 864213570, 54861732, 867254301, 87654321]  # 5 test cases
testCasesNames = ["125340678", "618402735", "864213570", "54861732", "867254301", "87654321"]


def getManhattanReport(testCase):
    astar = AStar(State(testCase),
                  State(12345678),
                  "manhattan")
    return astar.getReport()


def getEuclidianReport(testCase):
    astar = AStar(State(testCase),
                  State(12345678),
                  "euclidian")
    return astar.getReport()


def manhattanVsEuclidian():
    numberOfExpandedNodesManhattan = []
    numberOfExpandedNodesEuclidian = []
    timeOfSearchingManhattan = []
    timeOfSearchingEuclidian = []
    for testCase in testCases:
        manhattanReport = getManhattanReport(testCase)
        euclidianReport = getEuclidianReport(testCase)
        numberOfExpandedNodesManhattan.append(manhattanReport[2])
        numberOfExpandedNodesEuclidian.append(euclidianReport[2])
        timeOfSearchingManhattan.append(manhattanReport[-2])
        timeOfSearchingEuclidian.append(euclidianReport[-2])

    plt.plot(testCasesNames, numberOfExpandedNodesManhattan, label="Manhattan")
    plt.plot(testCasesNames, numberOfExpandedNodesEuclidian, label="Euclidian")
    plt.title("Number of expanded nodes for Manhattan and Euclidian")
    plt.xlabel("Test cases initial state")
    plt.legend()
    plt.ylabel("Number of expanded nodes")
    plt.savefig("NumberOfExpandedNodes.png")
    plt.show()
    plt.plot(testCasesNames, timeOfSearchingManhattan, label="Manhattan")
    plt.plot(testCasesNames, timeOfSearchingEuclidian, label="Euclidian")
    plt.title("Time of searching for Manhattan and Euclidian")
    plt.xlabel("Test cases initial state")
    plt.legend()
    plt.ylabel("Time of searching")
    plt.savefig("TimeOfSearching.png")
    plt.show()


def comparisonBetweenSearches():
    numberOfExpandedNodesManhattan = []
    numberOfExpandedNodesEuclidian = []
    numberOfExpandedNodesBFS = []
    timeOfSearchManhattan = []
    timeOfSearchEuclidean = []
    timeOfSearchBFS = []
    for testCase in testCases:
        manhattanReport = getManhattanReport(testCase)
        euclidianReport = getEuclidianReport(testCase)
        numberOfExpandedNodesManhattan.append(manhattanReport[2])
        numberOfExpandedNodesEuclidian.append(euclidianReport[2])
        numberOfExpandedNodesBFS.append(BFS.bfs(testCase, Utilities.goal_test)[1])
        timeOfSearchManhattan.append(manhattanReport[-2])
        timeOfSearchEuclidean.append(euclidianReport[-2])
        timeOfSearchBFS.append(BFS.bfs(testCase, Utilities.goal_test)[3])

    plt.plot(testCasesNames, numberOfExpandedNodesManhattan, label="A* Manhattan", marker='o')
    plt.plot(testCasesNames, numberOfExpandedNodesEuclidian, label ="A* Euclidean", marker='o')
    plt.plot(testCasesNames, numberOfExpandedNodesBFS, label="BFS", marker='o')
    plt.title("Number of expanded nodes for Manhattan and BFS")
    plt.xlabel("Test cases initial state")
    plt.legend()
    plt.ylabel("Number of expanded nodes")
    plt.show()
    plt.plot(testCasesNames, timeOfSearchManhattan, label="Manhattan", marker='o')
    plt.plot(testCasesNames, timeOfSearchEuclidean, label="Euclidian", marker='o')
    plt.plot(testCasesNames, timeOfSearchBFS, label="BFS", marker='o')
    plt.xlabel("Test cases initial state")
    plt.legend()
    plt.ylabel("Time of searching")
    plt.show()

comparisonBetweenSearches()