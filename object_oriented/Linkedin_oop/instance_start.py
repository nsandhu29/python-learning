class Book:
    # The init method is called when the instance is created
    # and ready to ne initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret"

    # Create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def set_discount(self, amount):
        self._discount = amount


# Create instance of class
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "Jd Salinger", 234, 29.95)

# print price of book 1
print(b1.get_price())
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())
# print(b2.__secret)
print(b2._Book__secret)
