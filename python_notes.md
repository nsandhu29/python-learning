# Python Notes

## Expressions

> Call Expressions
> Anatomy of a call expression:
>
> - operator(operand1,operand2)
> 

## String

> - Strings are objects we can run methods on strings
> - f string
>
## Loops in python

> - break
> - continue
> - else

## Class introspection

> - dir()
> - type()
> - 

## Data Structures

> - Complexity of each data structure
> - Dictionary
> - List
>   - list are unordered
>   - sorted()
>   
> - Sets is like list that don't allow duplicates.
> - tuples
> - list comprehensions
>   - very common technique
>   ```python
>   [x for x in range(10)]
>   {x for x in 'superduper' if x not in 'dp'}
>   ```
>   - mixed data structures

## Functions

> - Scope
> - Decorators
>   - item 1
>   - item 2
> - Generators
>   - Generator functions
> - Return
> - Yield
> - functions are first class objects


## Class

> - A class is like a blueprint for creating an object.
> - To create an object using your class, you call a special method named the constructor. Instantiating an object of a class is a bit like saying, “Hey Python, you remember that blueprint I gave you? Well, I’d like you to use it to make an object.”
> - Constructor \__init\__(self)
> >
> > - The self parameter automatically receives a reference to the object invoking the method. By using self, a method can invoke the object and access the attributes and methods of that object.
> > - A constructor is a special method to tell Python how to create an object of this class.
> > - A constructor is always called \__init\__ with a double underscore on each side of 'init'
>
> - Attributes:
>
> > - Objects have attributes.
>   > - Attributes are data stored inside a class or instance.
>   > - Attributes repersent the state or quality of a class or instance 
> - Getter Setter
>   > - These are methods that get and set the values of the object’s attributes.
>   > - Including getters and setters in your class is good programming etiquette, because they are useful tools for ensuring that people are using your code in the way you expect, and for minimising the risk of unexpected errors.
> - Inheritance
> - Iterators
> - \__str\__
> - Organise and structure code.
> - Maintain and plan is easy
> - Groups together data and behavior into one place
> - Class - Blueprint for object
> - Methods - Functions in class
> - Composition - Building complex objects out of other objects
> - Name mangling
> - Method resolution order
> - \__mro\__
> - Composition
> - Interface
> - Magic Methods - Python automatically associate with class methods
>   - Customize object behavior and integrate with the language
>   - Define how objects are represented as strings
>   - Control access to attribute values, both for get ans set
>   - Build in comparison and equality testing capabilities
>
> - dataclass
> - dataclass decorators and frozen
> - classmethod 
>   - Requires access to the class object to call other class methods or constructors
> - staticmethod 
>   - No access needed to either class or instance object
>   - Most likely an implementation detail of the class
>   - May be able to be moved outside the class to become a global-scope function in the module
> - Object oriented programming resources
>   - <https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/>
>     
>     How to explain object-oriented programming concepts to a 6-year-old
>   - <https://dziganto.github.io/classes/data%20science/linear%20regression/machine%20learning/object-oriented%20programming/python/Understanding-Object-Oriented-Programming-Through-Machine-Learning/>
>     
>     Understanding Object-Oriented Programming Through Machine Learning
>   - <https://www.futurelearn.com/courses/object-oriented-principles>
>   - Python 3 Object-oriented Programming: Building robust and maintainable software with object oriented design patterns in Python, 2nd Edition
>   - --Book-- Design Patterns: Elements of Reusable Object-Oriented Software


## Python object model  

## Generators, Coroutines, and Nanoservices

## Reference:
> - <http://composingprograms.com/>
> - <>