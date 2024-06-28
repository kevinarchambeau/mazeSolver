import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].top_wall)
        self.assertFalse(m1._cells[num_cols - 1][num_rows - 1].bottom_wall)

    def test_visited_reset(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                self.assertFalse(m1._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
