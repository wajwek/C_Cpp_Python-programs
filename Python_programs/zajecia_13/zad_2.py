class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def __str__(self):
        return f"szerokość: {self.width}, długość: {self.length}"
    
    def area(self):
        return self.length * self.width 
    def perimeter(self):
        return 2*self.length + 2*self.width
p = Rectangle(10, 5)
print(p)
print("Pole:", p.area())
print("Obwód:", p.perimeter())