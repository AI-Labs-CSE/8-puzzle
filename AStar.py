import time
from math import sqrt
from heapq import heapify, heappush, heappop

from State import State


class AStar:
    def __init__(self, initialState, goalState, heuristicsType="manhattan"):
        self.initialState = initialState
        self.goalState = goalState
        self.explored = set()
        self.heuristicsType = heuristicsType

    def search(self):
        maxDepth = 0
        # priority queue (frontier) to push state into it based on the cost
        # that should be equal to g(n) + h(n) cost is calculated from getCost based on heuristicsType
        frontier = []
        frontierSet = {self.initialState.stateSavedAsInt: 0}
        heapify(frontier)
        heappush(frontier, (self.getCost(self.initialState), 0,
                            self.initialState.stateSavedAsInt,
                            self.initialState))
        # loop till frontier is not empty to search for the solution
        while not len(frontier) == 0:
            # We accessed index 2 as in priority queue we have tuple of (cost, stateString, state)
            state = heappop(frontier)[3]
            # frontierSet.remove(state.stateAsString()

            # If we found the needed state, so we are done and return the state
            if self.goalState.stateSavedAsInt == state.stateSavedAsInt:
                return state, maxDepth

            self.explored.add(state.stateSavedAsInt)
            # case not fount we expand and generate the children of the current state
            neighborPriority = 0
            for neighbor in state.generateChildren():
                neighborPriority += 1
                maxDepth = max(maxDepth, neighbor.depth)
                if (neighbor.stateSavedAsInt not in self.explored) and (neighbor.stateSavedAsInt not in frontierSet):
                    cost = AStar.getCost(self, neighbor)
                    heappush(frontier, (cost,
                                        neighborPriority,
                                        neighbor.stateSavedAsInt,
                                        neighbor))
                    frontierSet[neighbor.stateSavedAsInt] = cost
                elif neighbor.stateSavedAsInt not in self.explored:
                    if frontierSet[neighbor.stateSavedAsInt] > self.getCost(neighbor):
                        heappush(frontier, (self.getCost(neighbor),
                                            neighborPriority,
                                            neighbor.stateSavedAsInt,
                                            neighbor))
                        frontierSet[neighbor.stateSavedAsInt] = self.getCost(neighbor)
        return None, maxDepth

    def printPath(self, state):
        if state.parent is not None:
            self.printPath(state.parent)
        state.printState()

    # Assume that the cost of one move will be 1
    def getCost(self, state):
        stateAsString = state.stateAsString()
        goalState = self.goalState.stateAsString()
        h = 0
        for cell in range(0, len(stateAsString)):
            currentCellX = int(int(goalState[cell]) / int(sqrt(len(stateAsString))))
            goalX = int(int(stateAsString[cell]) / int(sqrt(len(stateAsString))))
            currentCellY = int(goalState[cell]) % int(sqrt(len(stateAsString)))
            goalY = int(int(stateAsString[cell]) % int(sqrt(len(stateAsString))))
            if self.heuristicsType == "manhattan":
                h += abs(currentCellX - goalX) + abs(currentCellY - goalY)
            else:
                h += sqrt((currentCellX - goalX) ** 2 + (currentCellY - goalY) ** 2)

        return int(state.depth + h)

    def getReport(self):
        startTime = time.time()
        neededState = self.search()
        runningTime = time.time() - startTime
        nodesExpanded = len(self.explored)
        searchDepth = neededState[1]
        if neededState[0] is None:
            return [], 0, nodesExpanded, searchDepth, runningTime, False
        pathToGoal = neededState[0].pathToGoal
        costOfPath = neededState[0].depth

        return pathToGoal, costOfPath, nodesExpanded, searchDepth, runningTime, True

    def printReport(self):
        report = self.getReport()
        print("Path To Goal is : \n")
        print(report[0])
        print(f"\nCost To Path is : {report[1]} \n")
        print(f"Number Of Expanded nodes is : {report[2]} \n")
        print(f"Search Max Depth is : {report[3]}\n ")
        print(f"Running Time is : {report[4]}")
