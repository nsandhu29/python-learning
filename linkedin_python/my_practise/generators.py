#!/usr/bin/env python3

def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()


def inclusive_range(*args):
    num_args = len(args)
    start = 0
    step = 1

    # initialize parameters
    if num_args < 1:
        raise TypeError(f'expected at least 1 argument, got {num_args}')
    elif num_args == 1:
        stop = args[0]
    elif num_args == 2:
        (start, stop) = args
    elif num_args == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {num_args}')

    # generator useful for create series of values
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__": main()