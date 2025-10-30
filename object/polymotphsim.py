from abc import ABC, abstractmethod


class shape:
    @abstractmethod
    def area(self):
        pass


class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class triangle(shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.base * self.height

# Circle = Circle()


shapes = [Circle(10), square(10), triangle(5, 8)]

for shape in shapes:
    print(f"the area of {shape.__class__.__name__} is {shape.area()}")
