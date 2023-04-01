import math

class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y
    
    def get_distance_from(self, other_point):
        return math.hypot(self.x - other_point.x, self.y - other_point.y)