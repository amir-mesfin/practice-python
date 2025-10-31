# properties

class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f} cm"

    @property
    def height(self):
        return f"{self._height:.2f} cm"
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

rectangle1 = rectangle(3, 4)
rectangle1.width = 10
print(rectangle1.width)
print(rectangle1.height)
del rectangle1.width
# print(rectangle1.width)  # This will raise an AttributeError since width is deleted
del rectangle1.height
# print(rectangle1.height)  # This will raise an AttributeError since height is deleted
