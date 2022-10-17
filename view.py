import tkinter as tk
from tkinter import ttk
import re
import time
import math


class InitialStateFrame(ttk.Frame):
    def __init__(self, container):
        self.container = container
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # initial state label
        self.initial_state_label = ttk.Label(self, text='Initial State')
        self.initial_state_label.grid(column=0, row=0, sticky=tk.W, **options)

        # initial state entry
        self.initial_state = tk.StringVar()
        self.initial_state_entry = ttk.Entry(self, textvariable=self.initial_state)
        self.initial_state_entry.grid(column=1, row=0, **options)
        self.initial_state_entry.focus()

        # run button
        self.run_button = ttk.Button(self, text='Run')
        self.run_button['command'] = self.run
        self.run_button.grid(column=2, row=0, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

        # match the initial state pattern
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **options)

    def run(self):
        """  Handle button click event
        """
        state = self.initial_state.get()
        print(state)
        if re.search("[1-8 ]{9}", state) is None:
            self.output_label['text'] = "you entered wrong state!"
            return

        TableFrame.empty_idx = self.get_empty_idx(state)
        TableFrame.state = list(state)
        if not TableFrame.created:
            frame = TableFrame(self.container)
            frame.create_board(state)
            TableFrame.created = True
        else:
            # TableFrame.update_board(state)
            TableFrame.solve(["Up", "Left", "Left"])

    def get_empty_idx(self, state):
        for i in range(len(state)):
            if state[i] == ' ':
                return i
        return -1


class OptionMenu(ttk.OptionMenu):
    def __init__(self, container):
        # set up variable
        self.option_var = tk.StringVar(container)

        # initialize data
        self.algorithms = ('BFS', 'DFS', 'A*')

        super().__init__(
            container,
            self.option_var,
            self.algorithms[0],
            *self.algorithms,
            command=self.option_changed
        )

        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(container, text='Select algorithm:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        self.grid(column=0, row=1, sticky=tk.W, **paddings)

        # output label
        self.output_label = ttk.Label(container, foreground='red')
        self.output_label.grid(column=1, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'


class TableFrame(ttk.Frame):
    board = []
    created = False
    empty_idx = 0
    state = list("")

    def __init__(self, container):
        super().__init__(container)
        OptionMenu.__instance = self

    def create_board(self, state):
        options = {'padx': 0, 'pady': 0, 'ipadx': 10, 'ipady': 10}
        index = 0
        for i in range(3):
            for j in range(3):
                puzzle_entry = ttk.Button(self, text=state[index])
                puzzle_entry.grid(column=j, row=i, **options)
                self.board.append(puzzle_entry)
                index = index + 1

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    @staticmethod
    def update_board(state):
        index = 0
        for i in range(9):
            TableFrame.board[i].configure(text=state[index])
            index = index + 1

    @staticmethod
    def solve(path):
        new_idx = TableFrame.empty_idx
        for x in path:
            if x == "Up":
                new_idx -= 3
            elif x == "Down":
                new_idx += 3
            elif x == "Left":
                new_idx -= 1
            elif x == "Right":
                new_idx += 1
            print(f'new_idx:{new_idx} empty_idx:{TableFrame.empty_idx}')

            TableFrame.board[TableFrame.empty_idx]['text'] = TableFrame.state[new_idx]
            TableFrame.board[new_idx]['text'] = ' '

            TableFrame.state[TableFrame.empty_idx] = TableFrame.state[new_idx]
            TableFrame.state[new_idx] = ' '

            TableFrame.empty_idx = new_idx
            time.sleep(1)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('8-Puzzle')
        self.center_window()
        self.resizable(False, False)

    def center_window(self):
        window_width = 600
        window_height = 400

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


if __name__ == "__main__":
    app = App()
    OptionMenu(app)
    InitialStateFrame(app)
    # keep the window displaying
    app.mainloop()
