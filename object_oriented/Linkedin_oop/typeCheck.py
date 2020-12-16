# Create book class
class Book:
    def __init__(self, title):
        self.title = title


# Create newspaper class
class Newspaper:
    def __init__(self, name):
        self.name = name


# Create instance of classes
b1 = Book("The Cather In The Rye")
b2 = Book("The Grapes of wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# Use type() to inspect object type
print(type(b1))
print(type(n1))

# Compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# use isinstance to compare specific instance to known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
# In python every class is subclass of Object
print(isinstance(n2, object))
