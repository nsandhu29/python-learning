# different ways of defining functions in python
def func(x, y, z):
    print(x, y, z)


func(1, 2, 3)


def func1(x, *args):
    print(x)
    print(args)


func1(1, 2, 3, 4, 5, 6)


def func3(x, **kwargs):
    print(x)
    print(kwargs)


func3(1, xmin=10, xmax=12)


def func4(*args, **kwargs):
    print(args)
    print(kwargs)


func4(1, 2, 3, 4)


def add(x, y):
    return x + y


def add_wrapper(*args, **kwargs):
    print('Wrapping')
    return add(*args, **kwargs)


print(add_wrapper(4, 5))
