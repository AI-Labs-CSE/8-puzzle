from queue import Queue
import time


def goal(state):
    return state == "012345678"


def valid(i, j):
    if abs(j) == 1:
        checker = i % 3
        checker2 = (i + j) % 3
        return (abs(checker2 - checker) == 1) and (((j+i) >= 0) and ((j+1) < 9))
    else:
        return i + j >= 0 and i+j < 9


def bfs(initialState):
    #The array of all possible actions which are up down left right
    offsets = [-3, 3, -1, 1]
    visited = set()
    frontierSet = set()
    frontier = Queue()
    parentMap = dict()
    start = time.time()
    frontier.put(initialState)
    frontierSet.add(initialState)
    parentMap[initialState] = None
    depth = 0
    solved = 0
    nodesExplored = 0
    while not frontier.empty():
        #Keep track of the current size of the queue to count the depth
        size = frontier.qsize()
        for i in range(size):
            state = frontier.get()
            frontierSet.remove(state)
            nodesExplored = nodesExplored + 1
            visited.add(state)
            state = str(state)
            zeroIndex = state.find('0')
            #if the number starts with 0 it will be pushed into the queue wtihout the 0 so we must check for that
            if zeroIndex == -1:
                state = '0' + state
                zeroIndex = 0
            if goal(state):
                solved = 1
                break
            for j in offsets:
                if valid(zeroIndex, j):
                    asList = list(state)
                    asList[zeroIndex] = asList[zeroIndex+j]
                    asList[zeroIndex+j] = '0'
                    pushState = int("".join(asList))
                    if (not (pushState in visited)) and (not (pushState in frontierSet)):
                        frontier.put(pushState)
                        frontierSet.add(pushState)
                        parentMap[pushState] = int(state)
        if solved:
            break
        depth = depth + 1
    end = time.time()
    path = generateArray(parentMap)
    return depth, nodesExplored, end-start, path


def direction(child, parent):
    if (parent - child) == -3:
        return 'Down'
    if (parent - child) == -1:
        return 'Right'
    if (parent - child) == 1:
        return 'Left'
    if (parent - child) == 3:
        return 'Up'


def generateArray(parentMap):
    path = []
    if 12345678 not in parentMap:
        return None
    parent = parentMap[12345678]
    current = 12345678
    # Back track to the root node to build the path
    while parentMap[current] is not None:
        child = str(parent).find('0')
        par = str(current).find('0')
        if par == -1:
            par = 0
        if child == -1:
            child = 0
        path.append(direction(par, child))
        current = parent
        parent = parentMap[parent]
    path.reverse()
    return path
