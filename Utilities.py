
# Check if the given state is the goal state
def goal_test(state):
    return state == "012345678"

# Search for s_num in the state and return its position as if it was in a 3 * 3 2d array
def get_coordinates_of(s_num, state):
    index = 0
    for char in state:
        if char == s_num:
            row = int(index / 3)
            col = index - 3 * row
            return [row, col]
        index += 1

def neighbors(state, zero_idx):
    adjacent = []
    for i in [-3, 3, -1, 1]:
        if valid(zero_idx, i):
            adjacent.append(next_state(state, zero_idx, zero_idx + i))
    return adjacent

def valid(i, j):
    if abs(j) == 1:
        checker = i % 3
        checker2 = (i + j) % 3
        return (abs(checker2 - checker) == 1) and (((j+i) >= 0) and ((j+1) < 9))
    else:
        return i + j >= 0 and i + j < 9

def next_state(state, zero_idx, new_idx):
    cur = list(state)
    cur[zero_idx] = cur[new_idx]
    cur[new_idx] = '0'
    ans = ""
    return (ans.join(cur))

# Convert int to string and add 0 at the first if it's missing a leading zero (the length of the num is 8 not 9)
def to_string(num):
    ret = str(num)
    if len(ret) == 8:
        return "0" + ret
    return ret

# Print the result (the passed arguments) in a formatted way.
def print_res(path_to_goal, nodes_expanded, max_search_depth, running_time):
    print("path_to_goal: ", end = "")
    print(path_to_goal)
    print("cost_of_path: " + str(len(path_to_goal)))
    print("nodes_expanded: " + str(nodes_expanded))
    print("search_depth: " + str(max_search_depth))
    print("running_time: " + str(running_time))
