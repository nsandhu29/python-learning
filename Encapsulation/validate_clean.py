class Typed:
    expected_type = object

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Holding:
    shares = Integer('shares')
    price = Float('price')
    name = String('name')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __setattr__(self, key, value):
        if key not in {'name', 'date', 'shares', 'price'}:
            raise AttributeError(f'No attribute {key}')
        super().__setattr__(key, value)


    @property
    def cost(self):
        return self.shares * self.price


class Readonly:
    def __init__(self, obj):
        self._obj = obj
    def __getattr__(self, item):
        return getattr(self._obj, item)
    def __setattr__(self, key, value):
        if key == '_obj':
            super().__setattr__(key, value)
        else:
            raise AttributeError('Readonly')