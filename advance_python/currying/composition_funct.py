# We define composition h of two functions f and g
# h(x) = g(f(x))

def compose(g, f):
    def h(x):
        return g(f(x))
    return h

"""
In mathematics and computer science, currying is the technique of 
breaking down the evaluation of a function that takes multiple 
arguments into evaluating a sequence of single-argument 
functions. Currying is also used in theoretical computer science, 
because it is often easier to transform multiple argument models 
into single argument models.

We will use our compose function in the next example. Let's assume,
we have a thermometer, which is not working accurately. The 
correct temperature can be calculated by applying the function 
readjust to the temperature values. Let us further assume that 
we have to convert our temperature values from Celsius to 
Fahrenheit. We can do this by applying compose to both 
functions:
The composition of two functions is generally not commutative, i.e. compose(celsius2fahrenheit, readjust) 
is different from compose(readjust, celsius2fahrenheit)
"""
def celsius2fahrenheit(t):
    return 1.8*t + 32
def readjust(t):
    return 0.9 * t - 0.5
convert = compose(readjust, celsius2fahrenheit)
print(convert(10), celsius2fahrenheit(10))

