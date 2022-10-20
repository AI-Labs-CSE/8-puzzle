import BFS, DFS, Visualizer, Utilities
from AStar import AStar
from State import State

def valid_initial_state(state):
    allowed = {"0", "1", "2", "3", "4", "5", "6", "7", "8"}
    for char in state:
        if char not in allowed:
            return False
        allowed.remove(char)
    return len(allowed) == 0

def main():
    # Get the input from the user, change its format to the appropriate one to be used inside the search methods
    # Call the required technique and store the result
    # If the result isn't false (there is a solution) pass the result and the initial state to the visualizer
    print("For BFS Enter 1\nFor DFS Enter 2\nFor A* with manhattan distance Enter 3\nFor A* with euclidean distance Enter 4")
    type = str(input("Choose a method: "))
    if type == "1":
        initial_state = input("Enter the initial state ex(1,0,2,3,4,5,6,7,8): ").replace(",", "")
        if not valid_initial_state(initial_state):
            print("Not valid initial state!")
            return
        res = BFS.bfs(int(initial_state), Utilities.goal_test)
        if res != False:
            Visualizer.visualize(initial_state, res[0])
    elif type == "2":
        initial_state = input("Enter the initial state: ").replace(",", "")
        if not valid_initial_state(initial_state):
            print("Not valid initial state!")
            return
        res = DFS.dfs(int(initial_state), Utilities.goal_test)
        if res != False:
            Visualizer.visualize(initial_state, res[0])
    elif type == "3":
        initial_state = input("Enter the initial state: ").replace(",", "")
        if not valid_initial_state(initial_state):
            print("Not valid initial state!")
            return
        aStar = AStar(State(int(initial_state)), State(12345678), "manhattan")
        res = aStar.getReport()
        Utilities.print_res(res[0], res[2], res[3], res[4])
        if res[5] != False:
            Visualizer.visualize(initial_state, res[0])
        else:
            print("There is no solution!")
    elif type == "4":
        initial_state = input("Enter the initial state: ").replace(",", "")
        if not valid_initial_state(initial_state):
            print("Not valid initial state!")
            return
        aStar = AStar(State(int(initial_state)), State(12345678), "euclidian")
        res = aStar.getReport()
        Utilities.print_res(res[0], res[2], res[3], res[4])
        if res[5] != False:
            Visualizer.visualize(initial_state, res[0])
        else:
            print("There is no solution!")
    else:
        print("Wrong input")

if __name__ == '__main__':
    main()
    