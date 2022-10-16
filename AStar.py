from queue import PriorityQueue, Queue

from State.State import State


class AStar:
    def __init__(self, initialState, goalState):
        self.initialState = initialState
        self.goalState = goalState
        self.explored = []
        self.explored.append(initialState)

    def search(self):
        frontier = [self.initialState]
        print(frontier)
        while not len(frontier) == 0:
            state = frontier.pop(0)
            self.explored.append(state)
            print(f" visitedState is------> {state.state} \n")
            if state.state == self.goalState.state:
                return state
            for child in state.generateChildren():
                if child not in self.explored and child not in frontier:
                    frontier.append(child)
        return None

    def printPath(self, state):
        if state.parent is not None:
            self.printPath(state.parent)
        state.printState()


astar = AStar(State("250134678"), State("012345678"))
req = astar.search()
req.printState()
var = req.stepsToCurrentState
print(var)
