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
    def __init__(self, x1, y1, x2, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall

    def draw(self):
        tl_x = self.x1
        tl_y = self.y1
        br_x = self.x2
        br_y = self.y2
        if self.left_wall:
            # from upper left to lower left
            left_line = Line(Point(tl_x, tl_y), Point(tl_x, br_y))
            self.win.draw_line(left_line, "black")
        if self.top_wall:
            # upper left to upper right
            top_line = Line(Point(tl_x, tl_y), Point(br_x, tl_y))
            self.win.draw_line(top_line, "red")
        if self.right_wall:
            # upper right to lower right
            right_line = Line(Point(br_x, tl_y), Point(br_x, br_y))
            self.win.draw_line(right_line, "purple")
        if self.bottom_wall:
            # bottom right to lower right
            bottom_line = Line(Point(tl_x, br_y), Point(br_x, br_y))
            self.win.draw_line(bottom_line, "blue")
