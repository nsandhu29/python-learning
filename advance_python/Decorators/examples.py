from advance_python.Decorators.decorators import *
import math


@do_twice
def say_whee():
    print('Whee!!')


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}'
    else:
        return f'Whoa {name}! {age} already, you are growing up!'


math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


@slow_down
def count_down(from_number):
    if from_number < 1:
        print('Liftoff')
    else:
        print(from_number)
        count_down(from_number - 1)

@register
def say_hello(name):
    return f'Hello {name}'


@register
def be_awesome(name):
    return f'Yo {name}, together we are awesome'


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(plugins.items()))
    print(f'Using {greeter!r}')
    return greeter_func(name)