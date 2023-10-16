class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x:int, y:int, radius:int):
        self._x = x
        self._y = y
        self._radius = radius

    def contains(self, point: Point) -> bool:
        return ((point.x - self._x)**2 + (point.y - self._y)**2) < (self._radius**2)


current_point = Point(6,8)
circle = Circle(9,9,10)
print(circle.contains(current_point))
