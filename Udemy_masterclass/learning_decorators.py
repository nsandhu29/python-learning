# def outer_function(msg):
#     def inner_function():
#         print(msg)
#
#     return inner_function
#
#
# hi_func = outer_function('Hi there')
# bye_func = outer_function('Bye there')
#
# hi_func()
# bye_func()
#
#
# def decorator_function(message):
#     def wrapper_function():
#         print(message)
#
#     return wrapper_function
#
#
# hi_dec = decorator_function('Hi buddy')
# bye_dec = decorator_function('Bye_buddy')
#
# hi_dec()
# bye_dec()


def decorator_function1(original_function):
    def wrapper_function1(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function1


@decorator_function1
def display():
    print('display function ran')


@decorator_function1
def display_info(name, age):
    print(f'display info ran with arguments {name} {age}')
# dec_display = decorator_function1(display)
display_info('Navjot', 34)
