from math import sqrt
from heapq import heapify, heappush, heappop

from State.State import State


def indexOfStateInFrontier(stateAsString, frontier):
    for i in range(0, len(frontier)):
        if frontier[i][1] == stateAsString:
            return i
    return -1


class AStar:
    maxDepth = 0
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState
        self.explored = set()

    def search(self, heuristicsType):
        # I have make priority queue of frontier to push state into it based on the cost
        # that should be equal to g(n) + h(n) cost is calculated from getCost based on heuristicsType
        frontier = []
        heapify(frontier)
        heappush(frontier, (AStar.getCost(self, self.initialState, heuristicsType),
                            self.initialState.stateAsString,
                            self.initialState))
        # We will loop till frontier is not empty to search for the solution
        while not len(frontier) == 0:
            state = heappop(frontier)[
                2]  # We accessed index 2 as in priority queue we have tuple of (cost, stateString, state)
            self.explored.add(state.stateAsString)  # Add to the set of visited elements the current state as string
            if self.goalState.stateAsString == state.stateAsString:  # If we found the needed state, so we are done and return the state
                return state
            # case not fount we expand and generate the children of the current state
            for neighbor in state.generateChildren():
                maxDepth = max(maxDepth, neighbor.depth)
                indexInFrontier = indexOfStateInFrontier(neighbor.stateAsString, frontier)
                if not self.explored.__contains__(neighbor.stateAsString) and indexInFrontier == -1:

                    heappush(frontier, (AStar.getCost(self, neighbor, heuristicsType),
                                        neighbor.stateAsString,
                                        neighbor))
                elif indexOfStateInFrontier(neighbor.stateAsString, frontier) != -1:
                    lst = list(frontier[indexInFrontier])
                    lst[0] = min(int(lst[0]), AStar.getCost(self, neighbor, heuristicsType))
                    frontier[indexInFrontier] = tuple(lst)
                    heapify(frontier)

        return None

    def printPath(self, state):
        if state.parent is not None:
            self.printPath(state.parent)
        state.printState()

    # we will assume that the cost of one move will be 1
    def getCost(self, state, heuristicsType):
        stateAsString = state.stateAsString
        goalState = self.goalState.stateAsString
        h = 0
        for i in range(0, len(stateAsString)):
            currentCellX = int(int(goalState[i]) / int(sqrt(len(stateAsString))))
            goalX = int(int(stateAsString[i]) / int(sqrt(len(stateAsString))))
            currentCellY = int(goalState[i]) % int(sqrt(len(stateAsString)))
            goalY = int(stateAsString[i]) % int(sqrt(len(stateAsString)))
            if heuristicsType == "manhattan":
                h += abs(currentCellX - goalX) + abs(currentCellY - goalY)
            else:
                h += sqrt((currentCellX - goalX) ** 2 + (currentCellY - goalY) ** 2)

        return int(state.depth + h)


astar = AStar(State("413026758"), State("012345678"))
req = astar.search("7")
req.printState()
var = req.pathToGoal
print(var)
