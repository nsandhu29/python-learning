if True:
    print('if True')
elif False:
    print('elif true')
else:
    print('neither true')

x = 5
if x == 0:
    print('zero true')
elif x == 1:
    print('elif  1 true')
elif x == 2:
    print('elif 2 true')
elif x == 3:
    print('elif 3 true')
elif x == 4:
    print('elif 4 true')
elif x == 5:
    print('elif 5 true')
else:
    print('neither true')

# ternary operator
hungry = 0
x = 'Feed the bear now' if hungry else 'Do not feed the bear'
print(x)

# Arithmetic operators
# Bitwise operators
x = 0x0a
y = 0x02
z = x & y  # and operator
z1 = x | y  # or operator
z2 = x ^ y  # xor operator
z3 = x << y  # shift left operators
z4 = x >> y  # shift right operator
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # 02x --> 2 character wide leading 0 in hexdecimal
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # 08b --> 8 character wide leading 0 in binary
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z1:08b}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z2:08b}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z3:08b}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z4:08b}')
