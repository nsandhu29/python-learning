# def my_decorator(func):
#     def wrapper():
#         print('Something is happening before function call')
#         func()
#         print('Something is happening after the function call')
#
#     return wrapper
#
#
# def say_we():
#     print('Whee!')
#
#
# say_we = my_decorator(say_we)
# #
# print(say_we)
# print(say_we())
#
# from datetime import datetime
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass
#     return wrapper
#
# def say_whee():
#     print('Wheee!!!')
#
# print(say_whee())
#
# say_whee = not_during_the_night(say_whee)
#
# print(say_whee())

# def my_decorator(func):
#     def wrapper():
#         print('Something is happening before function call')
#         func()
#         print('Something is happening after the function call')
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print('Whee!!!')
#
# print(say_whee)
# print(say_whee())

import functools
import time
import random

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do something before
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__} in {run_time:.4f} secs')
        return value
    return wrapper_timer


def debug(func):
    """Print the function signature and return values"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do something before
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k} = {v!r}' for k, v in kwargs.items()]
        signature = ','.join(args_repr + kwargs_repr)
        print(f'Calling the {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value

    return wrapper_debug


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        # Do something before
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


plugins = dict()


def register(func):
    """Register a function as plug in"""
    plugins[func.__name__] = func
    return func