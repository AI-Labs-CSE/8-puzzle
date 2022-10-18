import time
from Utilities import *

# Arrays represents the possible moves (change in coordinates of a certain move)
# Note: the order of moves arrays is ["Right", "Left", "Down", "Up"], will be reversed because of the stack
move_name = ["Right", "Left", "Down", "Up"]
move_row = [0, 0, 1, -1]
move_col = [1, -1, 0, 0]

# Get the linear indexing of the source and the destination and swap them
def apply_move(state, current_coordinates, new_coordinates):
    current_index = current_coordinates[0] * 3 + current_coordinates[1]
    new_index = new_coordinates[0] * 3 + new_coordinates[1]
    new_state = list(state)
    c_temp = new_state[new_index]
    new_state[new_index] = new_state[current_index]
    new_state[current_index] = c_temp
    return int("".join(new_state))

def dfs(initial_state, goal_test):
    levels_to_goal = []
    path_to_goal = []
    nodes_expanded = 0
    max_search_depth = 0
    
    start_time = time.time()
    frontier_stack = [initial_state]
    frontier_set = {initial_state}
    explored = set()
    
    while len(frontier_stack) != 0:
        state = frontier_stack.pop()
        frontier_set.remove(state)
        explored.add(state)
        
        if goal_test(to_string(state)):
            for i in levels_to_goal:
                path_to_goal.append(i[len(i) - 1])
            print_res(path_to_goal, nodes_expanded, max_search_depth, time.time() - start_time)
            return path_to_goal
        
        nodes_expanded += 1
        current_coordinates = get_coordinates_of("0", to_string(state))
        level_moves = []
        for i in range(0, 4):
            new_row = current_coordinates[0] + move_row[i]
            new_col = current_coordinates[1] + move_col[i]
            if new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3:
                new_state = apply_move(to_string(state), current_coordinates, [new_row, new_col])
                if new_state not in frontier_set and new_state not in explored:
                    frontier_stack.append(new_state)
                    frontier_set.add(new_state)
                    level_moves.append(move_name[i])
                    
        if len(level_moves) == 0:
            levels_to_goal[len(levels_to_goal) - 1].pop()
            while len(levels_to_goal) != 0 and len(levels_to_goal[len(levels_to_goal) - 1]) == 0:
                levels_to_goal.pop()
                if len(levels_to_goal) > 0:
                    levels_to_goal[len(levels_to_goal) - 1].pop()
        else:
            levels_to_goal.append(level_moves)
            max_search_depth = max(max_search_depth, len(levels_to_goal))

    print_res(path_to_goal, nodes_expanded, max_search_depth, time.time() - start_time)
    print("There is no solution!")
    return False
