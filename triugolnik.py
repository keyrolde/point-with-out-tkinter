from typing import List
from point import Point


class Figure:
    def __init__(self, point_list: List[Point] = None):
        self.dot_list = point_list if point_list else [Point(), Point(), Point()]

    def get_point_list(self):
        result = []
        for dot in self.dot_list:
            result.append(dot.x)
            result.append(dot.y)
        return result

    def __str__(self):
        return f"{self.dot_list}"

    def __repr__(self):
        return f"{self.__class__}: {self.dot_list}"

    def __add__(self, other: int):
        return Figure([point + other for point in self.dot_list])
