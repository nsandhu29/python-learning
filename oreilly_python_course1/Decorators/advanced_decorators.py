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


# what if we want to change logging message, define format of logging message

def logformat(fmt):
    def logged(func):
        # Idea: give me function i will put logging
        # around it
        print('Adding logging to', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        return wrapper

    return logged


@logformat('CALLING {func.__name__}')
def add(x, y):
    return x + y


@logformat('Calling {func.__name__}')
def sub(x, y):
    return x - y


@logformat('Calling {func.__name__}')
def mul(x, y):
    return x * y


# we have to manually define logging for each function we can overcome this
# we can do
logged = logformat('Calling {func.__name__}')

@logged
def add1(x, y):
    return x + y

@logged
def sub1(x, y):
    return x - y

@logged
def mul1(x, y):
    return x * y