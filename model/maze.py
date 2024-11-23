import random
import time
from model.cell import Cell
from model.geometry import Point

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None

        ):
            self.x1 = x1
            self.y1 = y1
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.cell_size_x = cell_size_x
            self.cell_size_y = cell_size_y
            self.win = win
            self.cells = []
            self.seed = seed
            if self.seed is not None:
                random.seed(seed)
            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
            self._reset_cells_visited() 


    def _create_cells(self):
          for i in range(self.num_cols):
                col_cells = []
                for j in range(self.num_rows):
                      col_cells.append(Cell(self.win))
                self.cells.append(col_cells)
            
          for i in range(len(self.cells)):
                for j in range(len(self.cells[i])):
                      self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        p1, p2 = self._get_cell_left_top_and_bottom_right_points(i, j)
        cell = self.cells[i][j]
        cell.p1 = p1
        cell.p2 = p2
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
         self.cells[0][0].has_top_wall = False
         self._draw_cell(0,0)

         self.cells[-1][-1].has_bottom_wall = False
         self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _reset_cells_visited(self):
         for i in range(self.num_cols):
              for j in range(self.num_rows):
                   self.cells[i][j].visited = False

    def _break_walls_r(self, i, j):
         current_cell = self.cells[i][j]
         current_cell.visited = True
         while True:
              to_visit = []
              if i > 0 and not self.cells[i - 1][j].visited:
                  to_visit.append((i - 1, j))
              if i + 1 <= self.num_cols - 1 and not self.cells[i + 1][j].visited:
                  to_visit.append((i + 1, j))
              if j > 0 and not self.cells[i][j - 1].visited:
                  to_visit.append((i, j - 1))
              if j + 1 <= self.num_rows - 1 and not self.cells[i][j + 1].visited:
                  to_visit.append((i, j + 1))

              if not to_visit:
                   self._draw_cell(i,j)
                   return
              
              target_cell = to_visit[random.randint(0, len(to_visit) - 1)]
              
              if target_cell[0] > i:
                   current_cell.has_right_wall = False
                   self.cells[target_cell[0]][target_cell[1]].has_left_wall = False
              if target_cell[0] < i:
                   current_cell.has_left_wall = False
                   self.cells[target_cell[0]][target_cell[1]].has_right_wall = False
              if target_cell[1] < j:
                   current_cell.has_top_wall = False
                   self.cells[target_cell[0]][target_cell[1]].has_bottom_wall = False
              if target_cell[1] > j:
                   current_cell.has_bottom_wall = False
                   self.cells[target_cell[0]][target_cell[1]].has_top_wall = False
              
              self._break_walls_r(target_cell[0], target_cell[1])

    def _get_cell_left_top_and_bottom_right_points(self, i, j):
         x1 = self.x1 + i * self.cell_size_x
         y1 = self.y1 + j * self.cell_size_y
         p1 = Point(x1, y1)
         x2 = x1 + self.cell_size_x
         y2 = y1 + self.cell_size_y
         p2 = Point(x2, y2)
         return p1, p2
    
    def _solve_r(self, i,j):
         self._animate()
         self.cells[i][j].visited = True

         p1, p2 = self._get_cell_left_top_and_bottom_right_points(i, j)
         self.cells[i][j].p1 = p1
         self.cells[i][j].p2 = p2


         if i == self.num_cols - 1 and j == self.num_rows - 1:
              return True # we are done
         
         to_visit = []
         if i > 0 and not self.cells[i - 1][j].visited and not self.cells[i - 1][j].has_right_wall:
             to_visit.append((i - 1, j))
         if i + 1 <= self.num_cols - 1 and not self.cells[i + 1][j].visited and not self.cells[i + 1][j].has_left_wall:
             to_visit.append((i + 1, j))
         if j > 0 and not self.cells[i][j - 1].visited and not self.cells[i][j - 1].has_bottom_wall:
             to_visit.append((i, j - 1))
         if j + 1 <= self.num_rows - 1 and not self.cells[i][j + 1].visited and not self.cells[i][j + 1].has_top_wall:
             to_visit.append((i, j + 1))
         
         for i2,j2 in to_visit:
              
              p1, p2 = self._get_cell_left_top_and_bottom_right_points(i2, j2)
              self.cells[i2][j2].p1 = p1
              self.cells[i2][j2].p2 = p2

              self.cells[i][j].draw_move(self.cells[i2][j2])
              if not self._solve_r(i2, j2):
                self.cells[i][j].draw_move(self.cells[i2][j2], undo=True)
              else:
                   return True
                   
                   
              

         

