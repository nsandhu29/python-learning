def add_one(number):
    """A function that adds one to the given number"""
    return number + 1


print(add_one(1))


def say_hello(name):
    return f'hello {name}'


def be_awesome(name):
    return f'Yo {name}, together we are the awesome'


def greet_bob(greeter_func):
    return greeter_func('Bob')


def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first child')

    def second_child():
        print('Printing from the second child')

    first_child()
    second_child()

print(parent())



print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print(say_hello('Navjot'))
print(be_awesome('Navjot'))
