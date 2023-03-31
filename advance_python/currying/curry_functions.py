#Currying in Python
# Currying is the technique of translating the evaluation of a function that takes multiple
# arguments into evaluating a sequence of functions
# f(x,y,z) -> f(x)(y)(z)
# After this focus on func tools??

def f(x,y):
    return x**2 + y**2

def h(x):
    def curried(y):
        return f(x,y)
    return curried

if __name__ == "__main__":
    fix10 = h(10)
    for y in range(10):
        print(f'fix10({y}) = {fix10(y)}')
        
# Lambda
car_makers = ['Ram', 'Ford', 'Honda', 'Jeep']

def car_make(car, car_maker):
    return f'{car.title()}, {car_maker}!!!'

car_announce = lambda car_maker: car_make('car made by', car_maker)

for car in car_makers:
    print(car_announce(car))
    
# Func tools
from functools import partial
car_makers = ['Ram', 'Ford', 'Honda', 'Jeep']

def car_make(car, car_maker):
    return f'{car.title()}, {car_maker}!!!'

car_announce = partial(car_make, 'car made by')
for car in car_makers:
    print(car_announce(car))


# Currying with toolz.curry
from toolz import curry
car_makers = ['Ram', 'Ford', 'Honda', 'Jeep']

@curry
def car_make(car, car_maker):
    return f'{car.title()}, {car_maker}!!!'

car_announce = car_make('car made by')

for car in car_makers:
    print(car_announce(car))
    
# Curry with syntax
## ast
