import math


class Point:
    color = None

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x, self.y, self.color

    def set_color(self, color):
        self.color = color


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r  # радиус

    def __str__(self):
        return self.x, self.y, self.r, self.color

    def area(self, ar):
        return math.pi * self.r ** 2

    def set_radius(self, val):
        self.r = val


class Sphere(Circle):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def volume(self):
        return 4 * math.pi * self.r ** 2
