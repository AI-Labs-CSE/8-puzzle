from queue import Queue
import time
from Utilities import print_res, to_string, neighbors


def bfs(initialState, goal_test):
    visited = set()
    frontier_set = set()
    frontier = Queue()
    parent_map = dict()
    start = time.time()
    depth = 0
    solved = False
    nodesExplored = 0

    frontier.put(initialState)
    frontier_set.add(initialState)
    parent_map[initialState] = None

    while not frontier.empty():
        # Keep track of the current size of the queue to count the depth
        size = frontier.qsize()
        for i in range(size):
            state = frontier.get()
            frontier_set.remove(state)
            visited.add(state)
            state = str(state)
            zero_idx = state.find('0')
            
            # if the number starts with 0 it will be pushed into the queue wtihout the 0 
            # so we must check for that
            if zero_idx == -1:
                state = '0' + state
                zero_idx = 0

            if goal_test(to_string(state)):
                solved = True
                break

            nodesExplored = nodesExplored + 1

            for neighbor in neighbors(state, zero_idx):
                neighbor = int(neighbor)
                if (not (neighbor in visited)) and (not (neighbor in frontier_set)):
                    frontier.put(neighbor)
                    frontier_set.add(neighbor)
                    parent_map[neighbor] = int(state)
        if solved:
            break
        depth = depth + 1
    end = time.time()
    path = generate_path_to_goal(parent_map)
    if path == None:
        print_res([], nodesExplored, depth, end - start)
        print("There is no solution!")
        return False
    print_res(path, nodesExplored, depth, end - start)
    return path

def generate_path_to_goal(parent_map):
    path = []
    if 12345678 not in parent_map:
        return None
    parent = parent_map[12345678]
    current = 12345678
    # Back track to the root node to build the path
    while parent_map[current] is not None:
        child = str(parent).find('0')
        par = str(current).find('0')
        if par == -1:
            par = 0
        if child == -1:
            child = 0
        path.append(direction(par, child))
        current = parent
        parent = parent_map[parent]
    path.reverse()
    return path

def direction(child, parent):
    if (parent - child) == -3:
        return 'Down'
    if (parent - child) == -1:
        return 'Right'
    if (parent - child) == 1:
        return 'Left'
    if (parent - child) == 3:
        return 'Up'
