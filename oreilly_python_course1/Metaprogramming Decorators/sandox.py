def func0(x, y, z):
    print(x, y, z)

def func2(x, *args):
    print(x)
    print(args)

def func3(x, **kwargs):
    print(x)
    print(kwargs)

def func4(*args, **kwargs):
    print(args)
    print(kwargs)


def func1(a,b,c,d):
    print(a,b,c,d)

args = (1,2)
kwargs = {'c':3, 'd':4}

func1(*args, **kwargs)

#wrapper functions
def add(x, y ):
    return x+y

def add_wrapper(*args, **kwargs):
    print('Wrapping!')
    return add(*args, **kwargs)
