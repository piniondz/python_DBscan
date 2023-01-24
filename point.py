from math import sqrt


class Point:
    x: float = 0
    y: float = 0
    label: int = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_label(self, label):
        self.label = label

    def distance(self, point):
        return sqrt((self.x - point.x)**2+(self.y - point.y)**2)
