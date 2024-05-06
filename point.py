from random import randint


class Point:
    def __init__(self, x: int = None, y: int = None):
        self.x = x if x else randint(10, 50)
        self.y = y if y else randint(10, 50)

    def __str__(self):
        return f"[{self.x};{self.y}]"

    def __repr__(self):
        return f"точка: {self.__str__()}"

    def __add__(self, other: int):
        return Point(self.x + other, self.y + other)
