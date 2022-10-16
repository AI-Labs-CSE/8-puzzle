from math import sqrt


class State:
    def __init__(self, stateAsString, pathToGoal=None,
                 parent=None, depth=0, costToState=1):
        self.stateAsString = stateAsString
        self.pathToGoal = pathToGoal if pathToGoal is not None else []
        self.parent = parent
        self.costToState = costToState
        self.depth = depth

    def generateChildren(self):
        children = []
        for action in State.getActions(self):
            child = State.generateChild(self, action)
            childState = State(child, pathToGoal=self.pathToGoal + [action],
                               parent=self,  depth=self.depth+1)
            children.append(childState)
        return children

    def generateChild(self, action):
        child = self.stateAsString
        index = child.index('0')
        if action == "up":
            child = child[:index - int(sqrt(len(self.stateAsString)))] + '0' + child[
                                                                       index - int(sqrt(len(self.stateAsString))) + 1:index] + \
                    child[index - int(sqrt(len(self.stateAsString)))] + child[index + 1:]
        elif action == "down":
            child = child[:index] + child[index + int(sqrt(len(self.stateAsString)))] + child[index + 1:index + int(
                sqrt(len(self.stateAsString)))] + '0' + child[index + int(sqrt(len(self.stateAsString))) + 1:]
        elif action == "left":
            child = child[:index - 1] + '0' + child[index - 1] + child[index + 1:]
        elif action == "right":
            child = child[:index] + child[index + 1] + '0' + child[index + 2:]
        return child

    def getActions(self):
        actions = []
        index = self.stateAsString.index('0')
        if index > sqrt(len(self.stateAsString)) - 1:
            actions.append("up")
        if index < len(self.stateAsString) - sqrt(len(self.stateAsString)):
            actions.append("down")
        if index % sqrt(len(self.stateAsString)) != 0:
            actions.append("left")
        if index % sqrt(len(self.stateAsString)) != sqrt(len(self.stateAsString)) - 1:
            actions.append("right")
        return actions

    def printState(self):
        for i in range(0, len(self.stateAsString)):
            print(self.stateAsString[i], end=" ")
            if i % sqrt(len(self.stateAsString)) == sqrt(len(self.stateAsString)) - 1:
                print("\n")
        print("\n")
