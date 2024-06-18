from draw import Window, Line, Point, Cell

win = Window(800, 600)
line = Line(Point(50,50), Point(400,400))
win.draw_line(line, "blue")
cell = Cell(10, 10, 50, 50, win, True, True, True, True)
cell.draw()
cell = Cell(55, 10, 95, 50, win, True, True, True, True)
cell.draw()
win.wait_for_close()
