def main():
    x = ('meow', 'grr', 'purr', 'hello', 'world')
    # kitten('meow', 'grr', 'purr')
    kitten(*x)
    y = dict(Buffy='Meow', Zilla='grr', Angel='rawr')
    kitten1(**y)


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow')


def kitten1(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f'kitten {k} says {kwargs[k]}')
    else:
        print('Meow')


# python object model
# In python there is no distinction between function and procedures
# Call by values in python in immutable objects
# Call by reference in python in mutable objects
# __name__ return name of current module
# __main__ is important it shows we are running this file, not imported.
if __name__ == "__main__": main()
