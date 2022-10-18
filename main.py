import BFS, DFS, Visualizer, Utilities

if __name__ == '__main__':
    # type = input("For BFS Enter 1.\nFor DFS Enter 2.\bFor A* with manhattan distance Enter 3.\For A* with euclidean distance Enter 4.")
    # if type == 1:
    #     BFS.bfs()
    # elif type == 2:
    #     DFS.dfs()
    # elif type == 3:
    # elif type == 4:
    # else:
    #     print("Wrong input")
    
    
    # Get the input from the user, change its format to the appropriate one to be used inside the search methods
    initial_state = input("Enter the initial state: ").replace(",", "")
    # Call the required technique and store the result
    res = DFS.dfs(int(initial_state), Utilities.goal_test)
    # If the result isn't false (there is a solution) pass the result and the initial state to the visualizer
    if res != False:
        Visualizer.visualize(initial_state, res)