from math import pi
import functools
import json
import abc

#Implement interface

class ShapeInterface(metaclass=abc.ABCMeta):
    """
    Define interface for shape class.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return(hasattr(subclass, 'area') and callable(subclass.area) or NotImplemented)
    
    @abc.abstractmethod
    def area(self):
        """Calculate area of shape"""
        raise NotImplementedError
    
    
    

class Square(ShapeInterface):
    """Square shape class"""
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length**2

class Circle(ShapeInterface):
    """Circle Shape class"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius**2)


class CalculateArea:
    """Class to calculate area of given shape"""
    def __init__(self, shapes):
        self.shapes = shapes
        self.types = [f'{type(shapes[i]).__name__} {i}'for i in range(len(shapes))]
    
    def _my_decorator(func):
        """Defining Decorator to make output in same format"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            json_object = json.dumps(func(*args, **kwargs))
            return json_object
        return wrapper
    
    @_my_decorator
    def sum_shape(self):
        types = self.types
        areas = []
        for shape in self.shapes:
            assert (isinstance(shape, ShapeInterface)), "Shape out of scope ['Square', 'Circle']"
            areas.append(shape.area())
#             if isinstance(shape, ShapeInterface):
#                 areas.append(shape.area())
#                 continue
            
#             raise Exception("Shape out of scope ['Square', 'Circle']")
        return dict(zip(types,areas))

