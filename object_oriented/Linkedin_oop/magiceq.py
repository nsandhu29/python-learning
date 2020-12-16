class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book")
        return(self.title == value.title and
               self.author == value.author and
               self.price == value.price)

    # the __ge__ establishes >= relationship with another object
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book")
        return self.price >= value.price

    # the __lt__ establishes < relationship
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book")
        return self.price < value.price


# Initiating book objects
b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To kill a Mockingbird", "Harper Lee", 24.95)

# check for equality
print(b1 == b3)
print(b2 == b1)

# check for greater and lesser value
print(b2 >= b1)
print(b2 < b1)

# Sort them too
books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books])