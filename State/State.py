from math import sqrt


class State:
    def __init__(self, state, stepsToCurrentState=None, parent=None):
        self.state = state
        self.stepsToCurrentState = stepsToCurrentState if stepsToCurrentState is not None else []

    def generateChildren(self):
        children = []
        for action in State.getActions(self):
            child = State.generateChild(self, action)
            childState = State(child, self.stepsToCurrentState + [action])
            children.append(childState)
        return children

    def generateChild(self, action):
        child = self.state
        index = child.index('0')
        if action == "up":
            child = child[:index - int(sqrt(len(self.state)))] + '0' + child[
                                                                       index - int(sqrt(len(self.state))) + 1:index] + \
                    child[index - int(sqrt(len(self.state)))] + child[index + 1:]
        elif action == "down":
            child = child[:index] + child[index + int(sqrt(len(self.state)))] + child[index + 1:index + int(
                sqrt(len(self.state)))] + '0' + child[index + int(sqrt(len(self.state))) + 1:]
        elif action == "left":
            child = child[:index - 1] + '0' + child[index - 1] + child[index + 1:]
        elif action == "right":
            child = child[:index] + child[index + 1] + '0' + child[index + 2:]
        return child

    def getActions(self):
        actions = []
        index = self.state.index('0')
        if index > sqrt(len(self.state)) - 1:
            actions.append("up")
        if index < len(self.state) - sqrt(len(self.state)):
            actions.append("down")
        if index % sqrt(len(self.state)) != 0:
            actions.append("left")
        if index % sqrt(len(self.state)) != sqrt(len(self.state)) - 1:
            actions.append("right")
        return actions

    def printState(self):
        for i in range(0, len(self.state)):
            print(self.state[i], end=" ")
            if i % sqrt(len(self.state)) == sqrt(len(self.state)) - 1:
                print("\n")
        print("\n")
