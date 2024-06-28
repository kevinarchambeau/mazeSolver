import time
import random
from draw import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        random.seed()
        self._create_cells()
        self._reset_cells_visited()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _create_cells(self):
        if self.num_rows < 1 or self.num_cols < 1:
            return None
        for i in range(self.num_cols):
            columns = []
            for j in range(self.num_rows):
                columns.append(Cell(self.win))
            self._cells.append(columns)
        # put this here for unit checks
        self._break_entrance_and_exit()

        self._break_walls_r(0, 0)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False

    def _break_walls_r(self, x, y):
        self._cells[x][y].visited = True

        while True:
            to_visit = []

            # check the neighbors
            # left side
            if x - 1 >= 0:
                if not self._cells[x - 1][y].visited:
                    to_visit.append((x - 1, y, "l"))
            # top side
            if y - 1 >= 0:
                if not self._cells[x][y - 1].visited:
                    to_visit.append((x, y - 1, "t"))
            # right side
            if x + 1 < self.num_cols:
                if not self._cells[x + 1][y].visited:
                    to_visit.append((x + 1, y, "r"))
            # bottom side
            if y + 1 < self.num_rows:
                if not self._cells[x][y + 1].visited:
                    to_visit.append((x, y + 1, "b"))

            if len(to_visit) == 0:
                return

            index = random.randrange(len(to_visit))
            next_cell = to_visit[index]
            # break the walls, need to double up here because the other wall will overwrite it
            match next_cell[2]:
                case "l":
                    self._cells[x][y].left_wall = False
                    self._cells[next_cell[0]][next_cell[1]].right_wall = False
                case "t":
                    self._cells[x][y].top_wall = False
                    self._cells[next_cell[0]][next_cell[1]].bottom_wall = False
                case "r":
                    self._cells[x][y].right_wall = False
                    self._cells[next_cell[0]][next_cell[1]].left_wall = False
                case "b":
                    self._cells[x][y].bottom_wall = False
                    self._cells[next_cell[0]][next_cell[1]].top_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
