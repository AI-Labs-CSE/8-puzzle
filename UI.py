import tkinter as tk
from tkinter import ttk
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('8-Puzzle')
        self.resizable(False, False)
        self._center_window()

    def _center_window(self):
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


class Board(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self._app = app
        self.state = list("12534 678")
        self.board = []
        self.hole_idx = 0
        self.create_board()

    def create_board(self):
        options = {'padx': 0, 'pady': 0, 'ipadx': 10, 'ipady': 10}
        index = 0
        for i in range(3):
            for j in range(3):
                button = ttk.Button(self, text=self.state[index])
                button.grid(column=j, row=i, **options)
                self.board.append(button)
                index = index + 1

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def update_board(self):
        index = 0
        for i in range(9):
            self.board[i].config(text=self.state[index])
            index = index + 1

    def show_solution(self, path):
        new_idx = self.hole_idx
        for x in path:
            if x == "Up":
                new_idx -= 3
            elif x == "Down":
                new_idx += 3
            elif x == "Left":
                new_idx -= 1
            elif x == "Right":
                new_idx += 1

            self.state[self.hole_idx] = self.state[new_idx]
            self.state[new_idx] = ' '
            self.hole_idx = new_idx

            self.update_board()
            time.sleep(1)

    def update_button_text(self, idx, text):
        self.board[idx].config(text=text)


class OptionMenu(ttk.OptionMenu):
    def __init__(self, app):
        self.option_var = tk.StringVar(app)
        self.algorithms = ('BFS', 'DFS', 'A*')
        self._app = app
        super().__init__(
            app,
            self.option_var,
            self.algorithms[0],
            *self.algorithms,
            command=self.option_changed
        )

        # padding for widgets using the grid layout
        self.paddings = {'padx': 5, 'pady': 5}
        self.grid(column=0, row=1, sticky=tk.W, **self.paddings)
        self._create_output_label()

    def _create_output_label(self):
        self.output_label = ttk.Label(self._app, foreground='red')
        self.output_label.grid(column=1, row=1, sticky=tk.W, **self.paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'


class InitialStateFrame(ttk.Frame):
    def __init__(self, app, board):
        super().__init__(app)
        self._app = app
        self.board = board
        self._create_entry_frame()

    def _create_entry_frame(self):
        self.options = {'padx': 5, 'pady': 5}

        self._create_label()
        self._create_entry()
        self._create_run_button()

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def _create_label(self):
        self.initial_state_label = ttk.Label(self, text='Initial State')
        self.initial_state_label.grid(column=0, row=0, sticky=tk.W, **self.options)

    def _create_entry(self):
        self.initial_state = tk.StringVar()
        self.initial_state_entry = ttk.Entry(self, textvariable=self.initial_state)
        self.initial_state_entry.grid(column=1, row=0, **self.options)
        self.initial_state_entry.focus()

    def _create_run_button(self):
        self.run_button = ttk.Button(self, text='Run')
        self.run_button['command'] = self.run
        self.run_button.grid(column=2, row=0, sticky=tk.W, **self.options)

    def run(self):
        """  Handle button click event
        """
        state = self.initial_state.get()
        print(state)

        self.board.state = list(state)
        self.board.update_board()

        self.board.hole_idx = self.get_hole_idx(state)
        # TODO
        # call the algorithm here
        self.board.show_solution(["Up", "Left", "Left"])

    def get_hole_idx(self, state):
        for i in range(len(state)):
            if state[i] == ' ':
                return i
        return -1


def main():
    """Create the game's board and run its main loop."""
    app = App()
    board = Board(app)
    menu = OptionMenu(app)
    InitialStateFrame(app, board)
    app.mainloop()


if __name__ == "__main__":
    main()
