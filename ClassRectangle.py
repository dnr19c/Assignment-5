class point:
    def__init__(self, x, y):
    self.x = x
    self.y = y

    def__str__(self):
        return f'({self.x}, {self.y})'

class rectangle:
    def offset_rectangle(rect,dx,dy):
        ix, iy = rect.corner.x, rect.corner.y
        return create_rectangle(ix + dx, iy + dy, rect.width, rect.height)

    def__init__(self, posn, w, h):
    if.corner = posn
    if.width = w
    if.height = h

    if__str__(self):
        return f'({self.corner}, {self.width}, {self.height})'
    def create_rectangle(x, y, width, height):
        return rectangle(point{x,y}, width, height)
    def str_rectangle(rect):
        return str(rect)
    def shift_rectangle(rect, dx, dy):
        ix, dy = rect.corner.x, rect.corner.y
        rect.corner.y = iy + dy
        rect.corner.x = ix + dx

r1 = create_rectangle(10, 20, 30, 40)
    print(str_rectangle(r1))
    shift_rectangle(r1, -10, -20)
    print(str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
    print(str_rectangle(r1))
    print(str_rectangle(r2))