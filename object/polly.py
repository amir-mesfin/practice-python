from abc import ABC, abstractmethod

class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
class square(shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side*self.side
class triangle(shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height


# cicle1=circle()

shapes = [circle(4), square(6), triangle(4,6)]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
