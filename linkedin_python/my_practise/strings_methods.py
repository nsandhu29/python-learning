#!/usr/bin/env python3

# Simple string
a = 'seven'
# Using .format() method to insert values
b = 'seven {} {}'.format(8, 9)
# Assigning values fixed location and making 9 spaces
c = 'seven {1:<9} {0:>9}'.format(8, 9)
# Assigning values in double quotes and left, right align 9 spaces
d = 'seven "{1:<9}" "{0:>9}"'.format(8, 9)
# Assigning values in double quotes and fill 9 zeros on left and right
e = 'seven "{1:<09}" "{0:>09}"'.format(8, 9)
# Multiline strings
f = '''

multiline string
'''
# Running different methods on string
g = a.capitalize()
h = a.upper()
# using f string
x = 8
y = 9
i = f'seven {x} {y}'
j = f'seven {x:<9} {y:>9}'
# Using format method to print values
print('x is {}'.format(a))
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(type(a))
