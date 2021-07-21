# Notes
- glob module grab file names matching pattern
  * files = glob.glob('Data/portfolio*.csv')
  
#### Exception handling in python
- How do we know which error will occur?
- Avoid using
  ```python
except Exception as err: ```


#### Enumerate in python

#### Review Python Data types
- Tuple -> row in database packing and unpacking operation, it's not immutable
- Dictionary -> key value pairs, do fast look ups. Keys will be unique
- list -> mutable, usually with list all items are of same type.
- set -> Eliminate all duplicates, very often used for membership testing


#### Lambda function
- b = lambda x: x*10
- a = lambda x, y : x + y

#### itertools


#### sys library 
- import sys
- sys.modules['modulename'] --> check if module is imported
- del sys.modules['modulename'] --> delete module from catche
- sys.path --> execution path for python


#### python package
- Move files to one folder
- make empty file \__inti\__.py
- from \. import filename relative import statement


#### Class and Objects
- classmethods
- super
- Multiple inheritance
- Defensive programming in Inheritance --> Abstract base class to enforce existence of method
- Type check implementation
- MRO - Method resolution
- Co-operative multiple inheritance
- If more than one parent, it has to check according to order


#### Special Methods Python
- \__repr\__
- \__str\__


#### context manager
- \__enter\__
- \__exit\__

#### encapsulation
- everything is dictionary
- \@property --> Gives ways to locking down the attributes
- objects are doing dictionary manipulation
- Descriptor


#### Closure
- It will capture the variables needed
- 