from math import sqrt, atan2

class Vec2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return self.__class__(self.x * factor, self.y * factor)

    def __truediv__(self, factor):
        return self.__class__(self.x / factor, self.y / factor)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def distTo(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def sqrDistTo(self, other):
        return (other.x - self.x) ** 2 + (other.y - self.y) ** 2

    def angleTo(self, other):
        return atan2(other.y - self.y, other.x - self.x)

    def tuple(self):
        """Returns tuple (int(x), int(y))"""
        return (int(self.x), int(self.y))

    def normalise(self):
        return self / abs(self)

    def perpendicular(self):
        return self.__class__(self.y, -self.x)
