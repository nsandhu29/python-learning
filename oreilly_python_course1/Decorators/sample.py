# Decorators to solve problem of repetitive code
# add logging to each functions
import logging as log


def add(x, y):
    # log.debug('Calling add')
    return x + y


def sub(x, y):
    log.debug('Calling sub')
    return x - y


def mul(x, y):
    log.debug('Calling mul')
    return x * y


# Suppose we have 500 different functions and we need to add logging to
# all functions instead of doing it manually we can use decorators
# One problem using wrapper is that function wrapped looses identity and
# docs related to function. To overcome this problem we use wraps from functools
from functools import wraps


def logged(func):
    # Idea: give me function i will put logging
    # around it
    print('Adding logging to', func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


@logged
def sub(x, y):
    return x - y


@logged
def mul(x, y):
    return x * y
