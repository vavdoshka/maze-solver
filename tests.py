import unittest
from model.maze import Maze

class Tests(unittest.TestCase):
    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )


    def test_maze_break_entrance(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_maze_visit_status(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.cells[0][0].visited,
            False,
        )
        self.assertEqual(
            m1.cells[-1][-1].visited,
            False,
        )

    def test_maze_solve(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        r = m1._solve_r(0,0)
        self.assertTrue(r)

if __name__ == "__main__":
    unittest.main()