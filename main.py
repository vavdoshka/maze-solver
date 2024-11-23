from ui.window import Window
from model.maze import Maze

def main():
    win = Window(800, 600)
    x1 = 15
    y1 = 10
    num_rows = 12
    num_colums = 16
    cell_size = 48
    m = Maze(x1, y1, num_rows, num_colums, cell_size, cell_size, win)
    m._solve_r(0, 0)
    win.wait_for_close()

if __name__ == "__main__":
    main()