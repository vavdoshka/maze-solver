from model.geometry import Line, Point

class Cell:

    def __init__(self, window, seed=None):
        self.p1 = None
        self.p2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.win = window
        self.visited = False

    def draw(self):
        top_left = self.p1
        bottom_right = self.p2
    
        bottom_left = Point(top_left.x, bottom_right.y)
        top_right = Point(bottom_right.x, top_left.y)

        line = Line(top_left, bottom_left)
        self.win.draw_line(line, "black" if self.has_left_wall else "white")

        line = Line(top_right, bottom_right)
        self.win.draw_line(line, "black" if self.has_right_wall else "white")
        
        line = Line(bottom_left, bottom_right)
        self.win.draw_line(line, "black" if self.has_bottom_wall else "white")
        
        line = Line(top_left, top_right)
        self.win.draw_line(line, "black" if self.has_top_wall else "white")

    def get_center(self):
        return Point(self.p1.x + (self.p2.x - self.p1.x) / 2, self.p2.y + (self.p1.y - self.p2.y) / 2)


    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        line = Line(self.get_center(), to_cell.get_center())
        self.win.draw_line(line, fill_color="gray" if undo else "red")