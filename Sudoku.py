import tkinter as tk
import SudokuSolver

class Sudoku:
    def __init__(self, window):
        self.window = window
        self.grid = self.default_sudoku_grid()
        self.add_content_to_window()
        self.show_window()
    
    def show_window(self):
        self.window.mainloop()
        
    def add_content_to_window(self, size_of_grid:int = 9):
        for x in range(size_of_grid):
            for y in range(size_of_grid):
                frame = tk.Frame(master = self.window)
    
    def default_sudoku_grid(self):
        return [[0 for i in range(9)] for i in range(9)]

if __name__ == "__main__":
    window = tk.Tk()
    Sudoku(window)