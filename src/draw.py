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
