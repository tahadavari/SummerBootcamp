class AreaCalculator:
    def calculate_area(self, shape):
        if shape['type'] == 'circle':
            return 3.14 * shape['radius'] ** 2
        elif shape['type'] == 'rectangle':
            return shape['width'] * shape['height']


shapes = [
    {'type': 'circle', 'radius': 5},
    {'type': 'rectangle', 'width': 4, 'height': 6}
]

calculator = AreaCalculator()
for shape in shapes:
    print(calculator.calculate_area(shape))

# after --------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    print(shape.calculate_area())
