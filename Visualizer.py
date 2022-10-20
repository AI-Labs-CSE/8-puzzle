from tkinter import *
from Utilities import get_coordinates_of

# Change the position of the zero with the given values, also change the colors between red and black
def change_position(row_change, col_change, position, labels):
    labels[position[0]][position[1]]['text'] = labels[position[0] + row_change][position[1] + col_change]['text']
    labels[position[0]][position[1]]['fg'] = '#000000'
    labels[position[0] + row_change][position[1] + col_change]['text'] = '0'
    labels[position[0] + row_change][position[1] + col_change]['fg'] = '#FF0000'
    position[0] += row_change
    position[1] += col_change
    return position

# Draw the initial state and make every move in the given array path_to_goal
def visualize(initial_state, path_to_goal):
    # Make a fixed size window
    root = Tk()
    root.geometry("400x400")
    root.columnconfigure(tuple(range(3)), weight = 1)
    root.rowconfigure(tuple(range(3)), weight = 1)
    
    # Represent the labels in 2d array as a 3 * 3 grid with big bold font size, initialized with the initial state
    labels = []
    for i in range(0, 3):
        temp = []
        for j in range(0, 3):
            temp.append(Label(master = root, text = initial_state[i * 3 + j], font = ("Helvetica", 36, "bold")))
            temp[j].grid(row = i, column = j, sticky = NSEW)
        labels.append(temp)

    # Get the coordinates of 0 in the initial state to keep track of its movement and change its color to red
    position = get_coordinates_of("0", initial_state)
    labels[position[0]][position[1]]['fg'] = '#FF0000'
    
    # Function that is called periodically with the index of the next move to apply
    def update(index):
        if index == len(path_to_goal):
            return
        
        if path_to_goal[index] == 'Up':
            change_position(-1, 0, position, labels)
        elif path_to_goal[index] == 'Down':
            change_position(1, 0, position, labels)
        elif path_to_goal[index] == 'Left':
            change_position(0, -1, position, labels)
        elif path_to_goal[index] == 'Right':
            change_position(0, 1, position, labels)
            
        root.after(1000, update, index + 1)
        
    root.after(1000, update, 0)

    root.mainloop()
    