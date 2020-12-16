from decimal import *
a = 7
b = 7*3
c = 6/2
d = .1 + .1 + .1 - .3  # doesn't gives zero accuracy and precision?
e = Decimal('.10')  # Use decimal class when dealing with money
f = Decimal('.30')
g = e + e + e - f  # This gives answer zero
h = float(g)
print('a is {}'.format(a))
print('b is {}'.format(b))
print('c is {}'.format(c))
print('d is {}'.format(d))
print('g is {}'.format(g))
print('h is {}'.format(h))
print(type(a))
print(type(g))
print(type(h))

# Boolean types for logical values and evaluation
x = True
print('x is {}'.format(x))
print(type(x))

# None type it is used to represent absence of values
y = None
print('y is {}'.format(y))
print(type(y))

# Sequence types
# Defining list
x_ls = [1, 2, 3, 4, 5]
# Changing values in list
x_ls[4] = 42
# Printing elements of list
for i in x_ls:
    print('i in list is {}'.format(i))

# Defining tuple : tuple is immutable we can't change values
x_tu = (1, 2, 3, 4, 5)
# Accessing elements of tuple
for i in x_tu:
    print('i in tuple is {}'.format(i))

# Defining sequence of type range from 0 to 5 : range is immutable
x_seq = range(5)
for i in x_seq:
    print('i in range is {}'.format(i))
print(type(x_seq))

# Defining sequence of type range from 0 to 5 with steps 2: range is immutable
y = range(5, 10, 2)
for i in y:
    print('i is {}'.format(i))

# Dictionary is searchable sequence of key and value pairs
x_dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# Accessing keys in dictionary
for i in x_dic:
    print('i in dic is {}'.format(i))
# Accessing keys and values in dictionary, this gives tuples of key, value pair
for k, v in x_dic.items():
    print('k is {}, v is {}'.format(k, v))
# Dictionaries are mutable
x_dic['three'] = 42
for k, v in x_dic.items():
    print('k is {}, v is {}'.format(k, v))

x1 = (1, 'two', 3.0, [4, 'four'], 5)
x2 = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x1))
print(id(x1))  # id returns the unique ids of various objects
print(id(x2))
print(id(x1[0]))
print(id(x2[0]))

# knowing type
if isinstance(x1, tuple):
    print('Yes')
else:
    print('No')

# python class introspection
# In computer programming, introspection is the ability to determine the type of an
# object at runtime. It is one of Python’s strengths. Everything in Python is an
# object and we can examine those objects. Python ships with a few built-in functions
# and modules to help us.
print(dir(x1))  # gives the names of all the methods of a object

