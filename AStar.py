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
        frontier = []
        frontierSet = {self.initialState.stateSavedAsInt: 0}
        heapify(frontier)
        heappush(frontier, (AStar.getCost(self, self.initialState),
                            0,
                            0,
                            self.initialState.stateSavedAsInt,
                            self.initialState))
        while not len(frontier) == 0:
            state = heappop(frontier)[4]
            self.explored.add(state.stateSavedAsInt)
            if self.goalState.stateSavedAsInt == state.stateSavedAsInt:
                return state, maxDepth
            neighborPriority = 0
            for neighbor in state.generateChildren():
                neighborPriority += 1
                maxDepth = max(maxDepth, neighbor.depth)
                if (neighbor.stateSavedAsInt not in self.explored) and (neighbor.stateSavedAsInt not in frontierSet):
                    cost = AStar.getCost(self, neighbor)
                    heappush(frontier, (cost,
                                        neighborPriority,
                                        neighbor.depth,
                                        neighbor.stateSavedAsInt,
                                        neighbor))
                    frontierSet[neighbor.stateSavedAsInt] = cost

                elif neighbor.stateSavedAsInt not in self.explored:
                    if frontierSet[neighbor.stateSavedAsInt] > AStar.getCost(self, neighbor):
                        heappush(frontier, (AStar.getCost(self, neighbor),
                                            neighborPriority,
                                            neighbor.depth,
                                            neighbor.stateSavedAsInt,
                                            neighbor))
                        frontierSet[neighbor.stateSavedAsInt] = AStar.getCost(self, neighbor)

        return None, maxDepth

    def getCost(self, state):
        stateAsString = state.stateAsString()
        goalState = self.goalState.stateAsString()
        h = 0
        for cell in range(0, len(stateAsString)):
            if stateAsString[cell] != '0':
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
        neededState = AStar.search(self)
        runningTime = time.time() - startTime
        nodesExpanded = len(self.explored)
        searchDepth = neededState[1]
        if neededState[0] is None:
            return [], 0, nodesExpanded, searchDepth, runningTime, False
        pathToGoal = neededState[0].pathToGoal
        costOfPath = neededState[0].depth

        return pathToGoal, costOfPath, nodesExpanded, searchDepth, runningTime, True
    