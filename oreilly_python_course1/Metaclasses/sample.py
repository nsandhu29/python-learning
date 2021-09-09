x = 42
y = 'Hello'
z = 3.5

print(x.__class__)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# What class object does in python?
# name --> Point
# bases --> (object,)
# methods
