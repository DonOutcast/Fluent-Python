import math
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __bool__(self):
        return bool(self.x or self.y)

print(bool(Vector(0, 0)))

