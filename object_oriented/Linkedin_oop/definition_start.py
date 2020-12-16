# Create a basic class
class Book:
    # Initializer function, initializing attributes
    def __init__(self, title):
        self.title = title


# Create a instance of class
b1 = Book("Brave New World")
b2 = Book("War and Peace")

# Print the class and attributes
print(b1)
print(b1.title)