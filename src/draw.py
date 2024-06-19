from tkinter import Tk, BOTH, Canvas


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill, width=2)


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "main"
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line: Line, fill):
        line.draw(self.canvas, fill)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cell:
    def __init__(self, win):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        tl_x = self.x1
        tl_y = self.y1
        br_x = self.x2
        br_y = self.y2
        if self.left_wall:
            # from upper left to lower left
            left_line = Line(Point(tl_x, tl_y), Point(tl_x, br_y))
            self.win.draw_line(left_line, "purple")
        if self.top_wall:
            # upper left to upper right
            top_line = Line(Point(tl_x, tl_y), Point(br_x, tl_y))
            self.win.draw_line(top_line, "purple")
        if self.right_wall:
            # upper right to lower right
            right_line = Line(Point(br_x, tl_y), Point(br_x, br_y))
            self.win.draw_line(right_line, "purple")
        if self.bottom_wall:
            # bottom right to lower right
            bottom_line = Line(Point(tl_x, br_y), Point(br_x, br_y))
            self.win.draw_line(bottom_line, "purple")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        start_center_x = self.x2 - (self.x2 - self.x1) / 2
        start_center_y = self.y2 - (self.y2 - self.y1) / 2
        end_center_x = to_cell.x2 - (to_cell.x2 - to_cell.x1) / 2
        end_center_y = to_cell.y2 - (to_cell.y2 - to_cell.y1) / 2
        line = Line(Point(start_center_x, start_center_y), Point(end_center_x, end_center_y))
        self.win.draw_line(line, color)

