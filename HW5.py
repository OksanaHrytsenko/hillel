class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def contains(self, point: Point) -> bool:
        return ((point.x - self._x)**2 + (point.y - self._y)**2) < (self._radius**2)


current_point = Point(5,5)
circle = Circle(9,9,10)
print(circle.contains(current_point))
