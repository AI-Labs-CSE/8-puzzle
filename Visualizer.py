from tkinter import *
from Utilities import get_coordinates_of


index = -1
stop = True
labels = []
position = []
path_to_goal = []
root = None

# Draw the initial state and make every move in the given array path_to_goal
def visualize(initial_state, moves):
    global labels, position, path_to_goal, root
    path_to_goal = moves
    
    root = create_root_window()
    
    labels = create_board_labels(initial_state)

    # Get the coordinates of 0 in the initial state to keep track of its movement and change its color to red
    position = get_coordinates_of("0", initial_state)
    labels[position[0]][position[1]]['fg'] = '#FF0000'
    
    Button(root, text = "Play", command = play).grid(row = 3, column = 0,  sticky = NSEW)
    Button(root, text = "Pause", command = pause).grid(row = 3, column = 2,  sticky = NSEW)
    Button(root, text = "Back", command = back).grid(row = 4, column = 0,  sticky = NSEW)
    Button(root, text = "Next", command = next).grid(row = 4, column = 2,  sticky = NSEW)
    
    root.after(1000, update)
    
    root.mainloop()
    
def create_root_window():
    """ Make a fixed sized window
    """
    root = Tk()
    root.geometry("400x400")
    root.columnconfigure(tuple(range(3)), weight = 1)
    root.rowconfigure(tuple(range(5)), weight = 1)
    return root

def create_board_labels(initial_state):
    """ Represent the labels in 2d array as a 3 * 3 grid 
        with big bold font size, initialized with the initial state
    """
    labels = []
    for i in range(0, 3):
        temp = []
        for j in range(0, 3):
            temp.append(Label(master = root, text = initial_state[i * 3 + j], font = ("Helvetica", 36, "bold")))
            temp[j].grid(row = i, column = j, sticky = NSEW)
        labels.append(temp)
    return labels

def update():
    global index, stop, path_to_goal, root
    
    if not stop:
        if index >= len(path_to_goal):
            return
        index += 1
        if index >= len(path_to_goal):
            return
        
        if path_to_goal[index] == 'Up':
            change_position(-1, 0)
        elif path_to_goal[index] == 'Down':
            change_position(1, 0)
        elif path_to_goal[index] == 'Left':
            change_position(0, -1)
        elif path_to_goal[index] == 'Right':
            change_position(0, 1)
    
    root.after(1000, update)

def change_position(row_change, col_change):
    """ Change the position of the zero with the given values,
        also change the colors between red and black
    """
    global labels, position
    labels[position[0]][position[1]]['text'] = labels[position[0] + row_change][position[1] + col_change]['text']
    labels[position[0]][position[1]]['fg'] = '#000000'
    labels[position[0] + row_change][position[1] + col_change]['text'] = '0'
    labels[position[0] + row_change][position[1] + col_change]['fg'] = '#FF0000'
    position[0] += row_change
    position[1] += col_change
    return position

def play():
    global stop
    stop = False

def pause():
    global stop
    stop = True
    
def back():
    global index, stop, path_to_goal
    stop = True
    if index < 0:
        return
    index -= 1    
    if path_to_goal[index + 1] == 'Up':
        change_position(1, 0)
    elif path_to_goal[index + 1] == 'Down':
        change_position(-1, 0)
    elif path_to_goal[index + 1] == 'Left':
        change_position(0, 1)
    elif path_to_goal[index + 1] == 'Right':
        change_position(0, -1)

def next():
    global index, stop, path_to_goal
    stop = True
    if index >= len(path_to_goal):
        return
    index += 1
    if index >= len(path_to_goal):
        return
    if path_to_goal[index] == 'Up':
        change_position(-1, 0)
    elif path_to_goal[index] == 'Down':
        change_position(1, 0)
    elif path_to_goal[index] == 'Left':
        change_position(0, -1)
    elif path_to_goal[index] == 'Right':
        change_position(0, 1)

