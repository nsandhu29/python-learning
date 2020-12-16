# Importing turtle class
from turtle import Turtle
# Importing random
from random import randint

# Creating object for turtle class and using class methods
ram = Turtle()
ram.color('brown')
ram.shape('turtle')

ram.penup()
ram.goto(-160, 100)
ram.pendown()

sham = Turtle()
mohan = Turtle()
john = Turtle()

sham.color('green')
sham.shape('turtle')
sham.penup()
sham.goto(-160, 70)
sham.pendown()

mohan.color('red')
mohan.shape('turtle')
mohan.penup()
mohan.goto(-160, 40)
mohan.pendown()

john.color('blue')
john.shape('turtle')
john.penup()
john.goto(-160, 20)
john.pendown()

for movement in range(100):
    ram.forward(randint(1, 5))
    sham.forward(randint(1, 5))
    mohan.forward(randint(1, 5))
    john.forward(randint(1, 5))

dir(john)