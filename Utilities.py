
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
