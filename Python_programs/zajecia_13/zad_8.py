import math  

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"Wektor: ({self.x}, {self.y})"

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2
print(f"Wynik dodawania v1 + v2: {v3}")
print(f"Długość wektora v1: {v1.length()}")
print(f"Długość wektora v2: {v2.length():.2f}")