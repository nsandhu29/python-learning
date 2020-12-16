from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def to_JSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def to_JSON(self):
        return f"{{\"Circle\" : {str(self.calc_area())} }}"

# class Square(GraphicShape):
#     def __init__(self, side):
#         self.side = side
#
#     def calc_area(self):
#         return self.side ** 2


# g = GraphicShape()

c = Circle(10)
print(c.calc_area())
# s = Square(3)
# print(s.calc_area())
print(c.to_JSON())
