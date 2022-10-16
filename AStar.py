import time
from math import sqrt
from heapq import heapify, heappush, heappop

from State.State import State


def indexOfStateInFrontier(stateAsString, frontier):
    for element in range(0, len(frontier)):
        if frontier[element][1] == stateAsString:
            return element
    return -1


class AStar:
    def __init__(self, initialState, goalState, heuristicsType="manhattan"):
        self.initialState = initialState
        self.goalState = goalState
        self.explored = set()
        self.heuristicsType = heuristicsType

    def search(self):
        maxDepth = 0
        # I have make priority queue of frontier to push state into it based on the cost
        # that should be equal to g(n) + h(n) cost is calculated from getCost based on heuristicsType
        frontier = []
        heapify(frontier)
        heappush(frontier, (AStar.getCost(self, self.initialState),
                            self.initialState.stateAsString,
                            self.initialState))
        # We will loop till frontier is not empty to search for the solution
        while not len(frontier) == 0:
            state = heappop(frontier)[
                2]  # We accessed index 2 as in priority queue we have tuple of (cost, stateString, state)
            self.explored.add(state.stateAsString)  # Add to the set of visited elements the current state as string
            if self.goalState.stateAsString == state.stateAsString:  # If we found the needed state, so we are done and return the state
                return state, maxDepth
            # case not fount we expand and generate the children of the current state
            for neighbor in state.generateChildren():
                maxDepth = max(maxDepth, neighbor.depth)
                indexInFrontier = indexOfStateInFrontier(neighbor.stateAsString, frontier)
                if not self.explored.__contains__(neighbor.stateAsString) and indexInFrontier == -1:

                    heappush(frontier, (AStar.getCost(self, neighbor),
                                        neighbor.stateAsString,
                                        neighbor))
                elif indexOfStateInFrontier(neighbor.stateAsString, frontier) != -1:
                    lst = list(frontier[indexInFrontier])
                    lst[0] = min(int(lst[0]), AStar.getCost(self, neighbor))
                    frontier[indexInFrontier] = tuple(lst)
                    heapify(frontier)

        return None

    def printPath(self, state):
        if state.parent is not None:
            self.printPath(state.parent)
        state.printState()

    # we will assume that the cost of one move will be 1
    def getCost(self, state):
        stateAsString = state.stateAsString
        goalState = self.goalState.stateAsString
        h = 0
        for cell in range(0, len(stateAsString)):
            currentCellX = int(int(goalState[cell]) / int(sqrt(len(stateAsString))))
            goalX = int(int(stateAsString[cell]) / int(sqrt(len(stateAsString))))
            currentCellY = int(goalState[cell]) % int(sqrt(len(stateAsString)))
            goalY = int(stateAsString[cell]) % int(sqrt(len(stateAsString)))
            if self.heuristicsType == "manhattan":
                h += abs(currentCellX - goalX) + abs(currentCellY - goalY)
            else:
                h += sqrt((currentCellX - goalX) ** 2 + (currentCellY - goalY) ** 2)

        return int(state.depth + h)

    def getReport(self):
        startTime = time.time()
        neededState = AStar.search(self)
        pathToGoal = neededState[0].pathToGoal
        costOfPath = neededState[0].depth
        nodesExpanded = len(self.explored)
        searchDepth = neededState[1]
        runningTime = time.time() - startTime

        return pathToGoal, costOfPath, nodesExpanded, searchDepth, runningTime

    def printReport(self):
        report = self.getReport()
        print("Path To Goal is : \n")
        print(report[0])
        print(f"\nCost To Path is : {report[1]} \n")
        print(f"Number Of Expanded nodes is : {report[2]} \n")
        print(f"Search Max Depth is : {report[3]}\n ")
        print(f"Running Time is : {report[4]}")


astar = AStar(State("054861732"), State("012345678"), "euclidian")
report = astar.getReport()
for i in report:
    print(i)