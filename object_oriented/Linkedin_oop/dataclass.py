from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def book_info(self):
        return f'{self.title} by {self.author}'


# Create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclass implement __repr__
print(b1)

# comparing two dataclasses
print(b1 == b3)

# Change some fields
b1.title = "Anna"
b1.pages = 375
print(b1)
